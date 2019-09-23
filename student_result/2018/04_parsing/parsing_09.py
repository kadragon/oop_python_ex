import bs4
import requests as rq
import webbrowser


def get_html(url):  # URL을 받아서 sorce읽는 파일
    response = rq.get(url)
    response.raise_for_status()

    return response.text


def Make_chart(soup):  # [' 순위', 제목' , '부른사람']
    N_chart_name = soup.select(
        'div._tracklist_mytrack tbody tr td a.title span.ellipsis')
    N_chart_artist = soup.select(
        'div._tracklist_mytrack tbody tr td._artist a ')
    N_chart_num = soup.select('div._tracklist_mytrack tbody tr td.ranking')
    Music_chart = []

    for i in range(50):
        temp = []
        TN_chart_name = N_chart_name[i].getText().split()
        TN_chart_artist = N_chart_artist[i].get('title')
        T_N_chart_artist = "".join(TN_chart_artist)
        T_N_chart_name = " ".join(TN_chart_name)
        T_N_chart_num = "".join(N_chart_num[i].getText().split())
        temp.append(T_N_chart_num)
        temp.append(T_N_chart_name)
        temp.append(T_N_chart_artist)
        Music_chart.append(temp)

    return Music_chart


# 차트들 정리 (Top 50)
Naver_chart_1 = get_html(
    'https://music.naver.com/listen/top100.nhn?domain=DOMESTIC&page=1')  # 네이버 음악차트
Naver_soup_1 = bs4.BeautifulSoup(Naver_chart_1, 'html.parser')
N_Music_chart_part_1 = Make_chart(Naver_soup_1)

Naver_chart_2 = get_html(
    'https://music.naver.com/listen/top100.nhn?domain=DOMESTIC&page=2')  # 네이버 음악차트
Naver_soup_2 = bs4.BeautifulSoup(Naver_chart_2, 'html.parser')


N_Music_chart_part_2 = Make_chart(Naver_soup_2)
N_Music_chart = N_Music_chart_part_1 + N_Music_chart_part_2   # 음악차트 100


while True:
    print("="*40)
    print("\n다음중 하나를 입력하시오")
    print("""    차트: Naver Music Chart를 보여줍니다.
    검색: 원하는 음악, 가수를 Top100 안에서 검색 및 youtube로 연결합니다.
    장르: 원하는 장르의 차트를 보여줍니다.
    종료: 프로그램을 종료합니다.
             """)
    command = input()

    if command == '차트':
        print("="*20)
        print("Naver Music Chart\n")
        print("순위 || 곡 제목 || 가수")
        for i in N_Music_chart:
            print(i[0], end="  ")
            print(i[1], end="  ")
            print(i[2])

    elif command == '검색':
        T = True
        while T:
            search = input("검색하고 싶은 가수 혹은 제목 중 하나를 입력하세요: ")
            print("\n%s의 검색 결과" % (search))
            flag = 0
            for i in N_Music_chart:
                if (search in i[0]) or (search in i[1]) or (search in i[2]):
                    flag = 1
                    print(i[0], end="  ")
                    print(i[1], end="  ")
                    print(i[2])

            if flag == 0:
                print("차트에서 검색결과가 없습니다.")

            if flag == 1:  # 정확하게 검색시에만 이동
                print("="*40)
                print("youtube로 연결하시겠습니까?")
                connection = input("예 or 아니오 (다른버튼을 누를 시 연결하지 않고 종료됩니다): ")
                if connection == "예" or connection == "Y" or connection == "y":
                    url = 'https://www.youtube.com/results?search_query='+search
                    webbrowser.open(url)

            print("계속 검색하겠습니까?")
            K = input("예 or 아니오")

            if K == '예':
                T = True
            else:
                T = False

    elif command == "장르":
        gerne = input("장르를 선택하시오: '발라드' '댄스' '힙합'")
        if gerne == '발라드':
            Naver_chart_ballade = get_html(
                'https://music.naver.com/listen/genre/top100.nhn?domain=DOMESTIC&genre=K01')  # 네이버 발라드 음악차트
            Naver_soup_ballade = bs4.BeautifulSoup(
                Naver_chart_ballade, 'html.parser')
            N_Music_ballade = Make_chart(Naver_soup_ballade)

            print("="*40)
            print("Naver Ballade Chart\n")
            print("순위 || 곡 제목 || 가수")
            for i in N_Music_ballade:
                print(i[0], end="  ")
                print(i[1], end="  ")
                print(i[2])

        elif gerne == '댄스':
            Naver_chart_dance = get_html(
                'https://music.naver.com/listen/genre/top100.nhn?domain=DOMESTIC&genre=K02')  # 네이버 발라드 음악차트
            Naver_soup_dance = bs4.BeautifulSoup(
                Naver_chart_dance, 'html.parser')
            N_Music_dance = Make_chart(Naver_soup_dance)

            print("="*40)
            print("Naver Dance Chart\n")
            print("순위 || 곡 제목 || 가수")
            for i in N_Music_dance:
                print(i[0], end="  ")
                print(i[1], end="  ")
                print(i[2])

        elif gerne == '힙합':
            Naver_chart_hiphop = get_html(
                'https://music.naver.com/listen/genre/top100.nhn?domain=DOMESTIC&genre=K03')  # 네이버 발라드 음악차트
            Naver_soup_hiphop = bs4.BeautifulSoup(
                Naver_chart_hiphop, 'html.parser')
            N_Music_hiphop = Make_chart(Naver_soup_hiphop)

            print("="*40)
            print("Naver Dance Hip Hop\n")
            print("순위 || 곡 제목 || 가수")
            for i in N_Music_hiphop:
                print(i[0], end="  ")
                print(i[1], end="  ")
                print(i[2])

    else:
        print("프로그램을 종료합니다!")
        break


# In[ ]:


# In[ ]:


# In[ ]:
