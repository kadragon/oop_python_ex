# pip install beautifulsoup4
# pip install requests
# pip install urllib.request
# pip install Pillow
# pip install tkinter

import bs4
import requests
import urllib.request
import tkinter
from PIL import Image, ImageTk


def intro():
    print('='*50)
    print('This program finds the player you want to find based on Baseball-Reference')
    print('This will return the data of the Major Leaguers (Minor Leaguers are not included)')
    print('='*50)


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어들여 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def sub_get_search_result(url):
    """
    검색 결과가 존재하는 지를 bool 형태로 반환한다
    :param url: 검색 결과 url
    :return: 검색결과가 존재하는지를 0, 1로 반환
    """
    sub_html = get_html(url)  # get_html() 을 이용해서, 대상 기사에 접속 html tag 를 가져온다.
    # bs4 parser 를 이용하여, 뽑아오기 쉽게 parsing 한다.
    sub_soup = bs4.BeautifulSoup(sub_html, 'html.parser')

    # <div class='index'> 전체를 추출한다.
    try:
        search_result = sub_soup.select('div.index')[0].getText().split()
    except IndexError:  # 선수가 아닌 Team/Franchise의 경우 값이 달라 IndexError가 발생한다
        return 2
    # 검색결과가 없는 경우 페이지는 0 hits를 출력한다. 따라서 이 0의 위치를 이용하여 결과의 존재 여부를 판별한다.
    try:
        search_result.index('0')
    except ValueError:  # 선수인 경우 0 hits가 존재하지 않으므로 ValueError가 발생한다
        return 1

    return 0


def check_valid_player(url):
    '''
    검색 결과가 선수인지를 bool 형태로 반환한다
    :param url: 검색결과 url
    :return: True or False
    '''
    result_html = get_html(url)
    result_soup = bs4.BeautifulSoup(result_html, 'html.parser')

    try:
        search_result = result_soup.select(
            'div#players div.search-item-url')[0].getText().split()
    except IndexError:
        return False

    return True


def get_player_url(url):
    '''
    플레이어 페이지의 url을 추출하여 반환한다
    :param url: 검색결과 url
    :return: 선수 페이지 url
    '''
    result_html = get_html(url)
    result_soup = bs4.BeautifulSoup(result_html, 'html.parser')

    player_part_url = result_soup.select(
        'div.search-item-url')[0].getText().split()[0]

    player_url = "https://www.baseball-reference.com/"+player_part_url
    return player_url


def get_player_image(url):
    '''
    선수의 이미지를 다운로드받는다
    :param url: 선수 페이지 url
    :return: None
    '''
    player_html = get_html(url)
    player_soup = bs4.BeautifulSoup(player_html, 'html.parser')

    # url에서 player image의 소스를 찾는다
    player_name = player_soup.select('div#meta h1')[0].getText()
    player_img_html = player_soup.find(id="meta")
    player_img_url = player_img_html.find("img")
    player_img_src = player_img_url.get("src")

    # 얻은 소스로부터 사진을 불러와 파이썬 메모리에 올린다
    data = urllib.request.urlopen(player_img_src).read()
    file_name = player_name+".png"

    # 불러온 사진을 저장한다
    with open(file_name, mode="wb") as f:
        f.write(data)

    # 라벨을 만들어 사진을 창에 띄운다
    print("Delete the label to continue")
    window = tkinter.Tk()
    window.title = player_name
    image = Image.open(file_name)
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(window, image=photo)
    label.pack()
    window.mainloop()


def get_player_data(url):
    '''
    선수 정보를 추출하여 출력한다
    :param url: 선수 페이지 url
    :return: None
    '''
    player_html = get_html(url)
    player_soup = bs4.BeautifulSoup(player_html, 'html.parser')

    # 선수의 이름, 포지션, 우타/좌타 여부, 우투/좌투 여부, 키, 몸무게, 팀을 출력한다. 팀이 없다면 다른 멘트를 출력한다.
    player_name = player_soup.select('div#meta h1')[0].getText()
    print("Player Name : " + player_name)

    player_position = player_soup.select('div#meta p')[0].getText().split()
    print("Player Position : " + " ".join(player_position[1:]))

    player_bats_throws = player_soup.select('div#meta p')[1].getText().split()
    print("Bats : " + player_bats_throws[1] +
          "\nThrows : " + player_bats_throws[4])

    player_height_weight = player_soup.select(
        'div#meta p')[2].getText().split()
    print("Player Height : " + player_height_weight[2][1:-1])
    print("Player Weight : " + player_height_weight[3][:-1])

    player_team = player_soup.select('div#meta p a')[0].getText()
    if player_team == "Born:":  # 팀이 없는 경우 그 다음 내용인 Born:이 player_team에 들어온다
        print("This player is already retired or looking for a team.")
    else:
        print("Player's Team : " + player_team)


def search_again():
    '''
    사용자가 다시 검색할 것인지를 문의한다
    :return: True or False
    '''
    return input('Do you want to search the player again? (enter yes or no) ').lower().startswith('y')


intro()

while True:
    # Baseball-Reference는 url 자체에 검색 결과를 포함하므로 이를 이용한다
    search = input("Enter the player's name ").replace(' ', '+')
    search_link = "https://www.baseball-reference.com/search/search.fcgi?hint=&search=" + \
        search + "&pid=&idx="

    if sub_get_search_result(search_link) == 1:  # 검색 결과가 검색창으로 나왔고, 결과가 존재하는 경우

        if check_valid_player(search_link):  # 결과가 선수인 경우
            player_link = get_player_url(search_link)
            get_player_data(player_link)
            get_player_image(player_link)

        else:  # 결과가 선수가 아닌 경우 ( ex) Team, Franchise 등)
            print("What you entered is not a player name. RE_ENTER the player's name")

    elif sub_get_search_result(search_link) == 0:  # 검색 결과가 없는 경우

        print("Nothing matches your answer. RE_ENTER the player's name")

    else:  # 검색 결과가 바로 선수 창으로 이어지는 경우 ( ex)Shin Soo Choo를 입력하면 바로 선수 페이지로 전환된다)

        player_link = search_link
        get_player_data(player_link)
        get_player_image(player_link)

    if search_again():

        continue
    else:

        break
