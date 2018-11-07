import bs4
import requests
import time

cnt = 1

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.text

def is_it_today_yesterday(date):
    t = time.localtime()
    y = time.localtime(time.time() - 86400)
    today = "%d%02d%02d" % (t.tm_year, t.tm_mon, t.tm_mday)  # 현재시간을 년, 월, 일로 구분하여 연결된 문자열로 만들어준다.
    yesterday = "%d%02d%02d" % (y.tm_year, y.tm_mon, y.tm_mday)  # 하루 전 날짜를 년, 월, 일로 구분하여 연결된 문자열로 만들어준다.
    d = date.replace('-', '').split(' ')[0]  # 받은 날짜에서 '-'를 지우고 년월일까지만 저장하자.
    if today == d or yesterday == d:
        return True
    else:
        return False



def page_indi_info(url):
    '''
    자세히보기 페이지 url을 파싱하여 유기동물 정보 출력
    '''
    global cnt

    html_indi = get_html('http://www.animal.go.kr' + url)  # 각 동물마다 자세히보기 페이지 html 얻기
    pars_indi = bs4.BeautifulSoup(html_indi, 'html.parser')  # 자세히보기 페이지 html 파싱

    info = pars_indi.select('div.bohoView table tr td')  # 유기동물의 정보에 해당하는 텍스트가 들어있는 <td>만 가져오자.

    if is_it_today_yesterday(info[6].getText()):
        info_breed_raw = info[1].getText().split()  # 품종 항목의 텍스트에 이상한 공백이 많으므로 공백을 처리하기 위한 과정
        info_breed = ''
        for i in info_breed_raw:  # 그냥 info_breed[0]를 사용한다면 품종이름에 띄어쓰기가 들어간다면 뒷 단어의 누락이 발생, 이를 막기 위해 다 붙여준다.
            info_breed = info_breed + ' ' + i
        info_breed = str(str(info_breed).split(']')[1]).split("'")[0]  # info_breed 형식이 ['[개]000']의 형식이므로 품종 이름만 가져오자.

        if len(info) == 16:  # 중성화 항목이 없는 경우가 존재. 중성화 항목이 있는경우 list 길이가 하나 더 길어지므로 따로 구분해주자.
            info_area_raw = info[15].getText().split()  # 보호 지역 항목의 텍스트가 이상한 공백이 많아 공백을 처리해주자
            info_area = ''
            for ii in info_area_raw:
                info_area += ii + ' '
            print('[{}]'.format(cnt) + '=' * 80)
            print('접수일 : ' + info[6].getText().split(' ')[0])
            print('품종 : ' + info_breed, end=' | ')
            print('색상 : ' + info[2].getText(), end=' | ')
            print('성별 : ' + info[3].getText(), end="| ")
            print('발견장소 : ' + info[0].getText().split('-')[0] + ' ' + info[0].getText().split('-')[1] + ' ' + info[5].getText())
            # 발견장소가 구체적으로 적히지 않은 경우가 많아 공고번호 '지역-지역-2018-00000'꼴의 앞자리 지역이름을 가져와 상세주소와 붙여주자.
            print('보호센터 : ' + info_area + info[13].getText() + ' (연락처 : ' + info[14].getText() + ')')
            print('자세히 보기 ☞ ' + 'http://www.animal.go.kr' + detail[1].get('href') + '\n')
            cnt += 1
        else:
            info_area_raw = info[14].getText().split()
            info_area = ''
            for ii in info_area_raw:
                info_area += ii + ' '
            print('[{}]'.format(cnt) + '=' * 80)
            print('접수일 : ' + info[6].getText())
            print('품종 : ' + info_breed, end=' | ')
            print('색상 : ' + info[2].getText(), end=' | ')
            print('성별 : ' + info[3].getText(), end="| ")
            print('발견장소 : ' + info[0].getText().split('-')[0] + ' ' + info[0].getText().split('-')[1] + ' ' + info[5].getText())
            print('보호센터 : ' + info_area + info[12].getText() + ' (연락처 : ' + info[13].getText() + ')')
            print('자세히 보기 ☞ ' + 'http://www.animal.go.kr' + detail[1].get('href') + '\n')
            cnt += 1
    else:
        pass


# 보호중유기동물 페이지에서 방문할 수 있는 목록페이지(1, 2, 3 ...)마다 url을 리스트로 반환.
abandoned_html = get_html('http://www.animal.go.kr/portal_rnl/abandonment/protection_list.jsp')
abandoned_pars = bs4.BeautifulSoup(abandoned_html, 'html.parser')
html_list = ['<a href="/portal_rnl/abandonment/protection_list.jsp"></a>'] + abandoned_pars.select('div.pagination a')

print('+'*20+' 어제도, 오늘도 유기동물들은 가족을 찾고 있어요 '+'+'*20)

for page in range(1,len(html_list)):
    page_html = get_html('http://www.animal.go.kr/portal_rnl/abandonment/protection_list.jsp?s_date=&e_date=&s_upr_cd=&s_org_cd=&s_up_kind_cd=&s_kind_cd=&s_name=&s_shelter_cd=&s_wrk_cd=&s_state=&s_state_hidden=&pagecnt='+str(page))
    page_pars = bs4.BeautifulSoup(page_html, 'html.parser')  # 보호중유기동물 페이지의 각 목록 페이지를 파싱

    # 페이지별 유기동물들의 각 자세히보기 링크가 담긴 (<div class='thumbnail01'>을 모두 검색하여 리스트로 반환.
    page_petlist = page_pars.select('div.abandarea div.thumbnail01')

    for i in page_petlist:
        detail = i.select('div.thumb_inner01 p a')
        page_indi_info(detail[1].get('href'))  # 동물별 자세히 보기 페이지 url일부를 page_indi_info()에게 넘겨줌.
