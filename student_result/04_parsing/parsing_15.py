#아래 코드는 달빛학사에 접속하여 세 가지 작업을 수행한다.
#1. 원하는 사람에게 원하는 내용의 메일을 보낸다.
#2. 이제까지 내가 받은 벌점에 대한 기록을 출력한다.
#3. 분실물 페이지의 1~5페이지 내의 글 제목에 지정한 키워드가 포함되면 들어가 글 내용을 긁어돈다.
import requests
from bs4 import BeautifulSoup as bs

# 로그인 정보 저장
LOGIN_INFO = {
    'id': '',
    'passwd': ''
}

# 보내고 싶은 메일 정보 저장
MAIL_INFO={
    'recvList':'1732_배민열,',
    'message':'None'
}

with requests.Session() as s:
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs(html, 'html.parser')

    csrf = soup.find('input', {'name': 'csrf_test_name'})

    LOGIN_INFO.update({'csrf_test_name': csrf['value']})

    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

    if login_req.status_code != 200:
        raise Exception('로그인 되지 않았습니다!')

    #1.원하는 사람에게 원하는 메일을 보내는 코드
    #아래의 for문으로 같은 메시지를 반복해 보낼 수 있다.
    for i in range(1):
        #페이지의 csrf_test_name의 value를 읽어와 st에 저장한다.
        #로그인 할 때와 비슷한 방식이다.
        section_board_list_data = bs(s.get('https://go.sasa.hs.kr/sms/main').text, 'html.parser')
        board_list_data = section_board_list_data.select('div.box-body input')
        st=board_list_data[0].get('value')

        #로그인 할 때와 마찬가지로 MAIL 딕셔너리에 csrf_test_name을 update한다.
        #현재 코드에서는 메신저로 보낼 내용을 csrf_test_name으로 하고있다.
        MAIL_INFO.update({'csrf_test_name': st,'message':st})
        #내가 보낸 메일의 정보를 출력한다.
        print(MAIL_INFO,'\n')
        mail_req = s.post('https://go.sasa.hs.kr/sms/main', data=MAIL_INFO)


    #2.이제껏 받은 벌점의 기록을 출력하는 코드
    section2 = bs(s.get('https://go.sasa.hs.kr/rating/rating_student_view').text, 'html.parser')
    #원하는 출력 형태를 만들기 위해 벌점 현황과 사유를 각각 board2, board3에 저장한다.
    board2 = section2.select('div.box-body td.hidden-xs')
    board3 = section2.select('div.box-body td.text-center')
    check=1
    #작업의 용이함을 위해 board2의 text와 board3의 text를 list에 옮긴다.
    list1=[]
    list2=[]
    check=100
    for j in board3:
        if(j.getText()=='벌점' or j.getText()=='상점'): check=3
        check-=1
        if(check==0): list1.append(j.getText())
        if(len(j.getText())>10): list1.append(j.getText().strip())
    
    for i in board2:
        i=list(i)
        for j in i:
            j=j.strip()
            list2.append(j)
    i=0
    j=0
    semester=2
    #몇학기에 받은 벌점인지, 이번 사유로 인해 누적된 벌점이 얼마인지 출력한다.
    while j<len(list1):
        if(len(list1[j])>10):
                if(semester%2==0):
                    print(semester//2,'학기 본관',list1[j].strip(),'\n')
                if(semester%2==1):
                    print(semester//2,'학기 기숙사',list1[j].strip(),'\n')
                j+=1
                semester+=1
        else:
            print(list2[i],',누적벌점:',list1[j])
            i+=1
            j+=1
    #지금 학기에 받은 벌점이 10점 밑이고 8점 이상이면 봉사를 하라고 출력한다.
    if(int(list1[-2])<-7 and int(list1[-2])>-10): print("벌점 위험, 빨리 봉사를 하세요.",list1[-2])
    #벌점이 10점 이상이면 이미 손쓸 수 없게 되었다고 출력한다.
    elif(int(list1[-2])<=-10): print("이미 손쓸 수 없게 되었어요.",list1[-2])

    #3.분실물 1~5페이지까지의 글을 보고 글 제목에 키워드가 포함되어 있으면 글의 내용을 긁어온다.
    print('\n')
    page=['1','2','3','4','5']
    #페이지 수에 해당하는 것이 i다.
    for i in range(5):
        #문자열 합으로 주소를 넣어준다.
        section_board_list_data = bs(s.get('https://go.sasa.hs.kr/board/lists/2/page/'+page[i]).text, 'html.parser')
        board_list_data = section_board_list_data.select('table.table tr a')
        for j in board_list_data:
            #일단 글의 내용을 긁어온다.
            board2=bs(s.get('https://go.sasa.hs.kr'+j.get('href')).text, 'html.parser')
            data2 = board2.select('div.box-body p')
            st=''
            for k in data2:
                st+=k.getText()
            j=list(j)
            #키워드가 포함되어 있는지 확인하는 if문
            if j[1].getText().find('샤프')!=-1:
                     #j[1]에는 글의 제목이 저장되어 있다.
                     #키워드를 포함한다면 글이 담긴 페이지 수와 함께 제목을 출력한다.
                     print(j[1].getText(),'page:',i)
                     #포함되어 있다면 긁어온 글의 내용을 출력한다.
                     print(st)
