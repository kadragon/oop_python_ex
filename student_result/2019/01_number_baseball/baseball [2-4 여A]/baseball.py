"""
Title       캔디 야구
Reference   kadragon's code
Author      Juhyeon Yeo
Date        2019.09.21
"""
import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640  # 화면의 넓이는 640 픽셀
WINDOWHEIGHT = 480  # 화면의 높이는 480 픽셀
#               R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXTCOLOR = WHITE  # 글자색은 하양색
# Python 에서 상수처럼 사용하고 싶으면, 대문자 + _ 을 사용
digits = 3  # 맞출 정답의 길이 설정하는 것
s = 0  # s의 개수
b = 0  # b의 개수
o = 0  # o의 개수
guesses = 0  # 맞출 수 있는 기회의 개수
guess = ''  # 사용자가 추측한 숫자의 문자열
star = 0  # 별의 개수
laststar = 0  # 마지막으로 보너스 단계를 플레이했을 때 별의 개수
check_bonus = 0  # 보너스 단계를 통과한 직후 1로 바뀌는 변수


class Mon:  # 플레이어의 클래스
    def __init__(self, s, b, o, guesses, guess, star, laststar, digits, check_bonus):
        self.s = s
        self.b = b
        self.o = o
        self.guesses = guesses
        self.guess = guess
        self.star = star
        self.laststar = laststar
        self.digits = digits
        self.check_bonus = check_bonus


player = Mon(s, b, o, guesses, guess, star, laststar, digits, check_bonus)
player.s = 0
player.b = 0
player.o = 0
player.guesses = 10  # 맞출 수 있는 기회는 10번
player.star = 0
player.laststar = 0
player.digits = 3
player.check_bonus = 0


def main():  # 시작 화면
    global DISPLAYSURF, BASICFONT, BIGFONT, HINTFONT
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('nanum.ttf', 18)  # 나눔 글씨체로 설정, 크기는 18
    BIGFONT = pygame.font.Font('nanum.ttf', 70)
    HINTFONT = pygame.font.Font('nanum.ttf', 60)
    bg = pygame.image.load("img/startscreen.png")  # 시작 화면을 그림으로 가져옴
    pygame.display.set_caption('Candy Baseball')  # 창의 제목 설정
    DISPLAYSURF.blit(bg, (0, 0))  # 그림의 왼쪽 위 모서리가 (0,0)에 있음
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 200)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    # press a key to play를 화면 중앙 아래에 띄움
    pygame.mixer.init()
    pygame.mixer.music.load('./music/theme.mp3')
    pygame.mixer.music.play()
    while checkForKeyPress() == None:
        pygame.display.update()  # 키보드를 누르면 다음 화면으로 넘어감
    while True:
        mainScreen()


def mainScreen():  # 게임 설명이 나오는 화면
    bg = pygame.image.load("img/instruction.png")
    DISPLAYSURF.blit(bg, (0, 0))
    while checkForKeyPress() == None:
        pygame.display.update()
    gameScreen()
    pygame.mixer.music.stop()


def gameScreen():  # 게임을 플레이하는 화면
    pygame.mixer.music.play()
    bg = pygame.image.load("img/mainground.png")  # 게임 플레이 배경 화면
    bbg = pygame.image.load("img/bonusground.png")  # 보너스 단계 배경 화면
    cover = pygame.image.load("img/numcover.png")  # 숫자 부분을 가리는 조각
    bcover = pygame.image.load("img/numcoverbonus.png")  # 보너스 단계에서 숫자 부분을 가리는 조각
    lose = pygame.image.load("img/losescreen.png")  # 게임에서 졌을 때 나오는 화면
    if player.digits == 3:
        DISPLAYSURF.blit(bg, (0, 0))  # 일반 단계에서 배경 화면 깔기
        pygame.mixer.music.stop()
        pygame.mixer.music.load('music/mainmenu.mp3')  # 일반 단계에서 배경 음악 깔기
        pygame.mixer.music.play()
    else:
        DISPLAYSURF.blit(bbg, (0, 0))  # 보너스 단계에서 배경 화면 깔기
        pygame.mixer.music.stop()
        pygame.mixer.music.load('music/mainmenunew.mp3')  # 보너스 단계에서 배경 음악 깔기
        pygame.mixer.music.play()

    drawGameStatus()  # 사탕 개수, 별 개수 등의 수치를 보여줌

    gameSurf = BASICFONT.render('Press \ to get 1 candy for 3 stars', True, WHITE)  # 화면의 상단에 띄우는 캡션
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (254, 27)
    DISPLAYSURF.blit(gameSurf, gameRect)
    pygame.display.update()  # 화면 업데이트
    i = player.digits - 1  # i=2이면 i가 감소하면서 2,1,0으로 3개의 수를 입력하여 3자리 수 생성 가능
    pos = [0, 0, 0, 0, 0, 0, 0]  # pos는 사용자가 입력하는 문자열이며 최대 7자리까지 가능
    while True:
        secret_num = get_secret_num(player.digits)  # 정답 생성
        print(secret_num)
        while player.guesses > 0:  # 시도 횟수가 초과하지 않았는지 확인
            inputguess(pos, i)  # 키보드로 숫자를 입력할 수 있게 하는 함수
            i = player.digits - 1  # i를 원래대로 돌려놓음
            k = 0  # k는 겹치는 수가 있는지 확인하는 변수
            for a in range(player.digits):  # 문자열에 겹치는 수가 있는지 확인
                for b in range(a):
                    if pos[a] == pos[b]:
                        k = 1  # 겹치는 수가 있으면 k=1로 바꿈
            if k == 1:
                GameCaption('Each number should be different')  # 겹치면 겹친다고 알려줌
                k = 0  # k를 원래대로 돌려놓음
            else:
                player.guess = ''
                for j in range(player.digits):
                    player.guess += str(pos[player.digits - j - 1])  # 입력한 수를 문자열로 이어줌
                concequence(player.guess, secret_num)  # 문자열의 결과를 처리하는 함수
                if player.digits == 3:
                    DISPLAYSURF.blit(cover, (150, 0))  # 일반 단계 배경에 맞는 숫자 커버를 덮음
                else:
                    DISPLAYSURF.blit(bcover, (148, 50))  # 보너스 단계 배경에 맞는 숫자 커버를 덮음
                drawGameStatus()
                if player.guess == '012':
                    GameCaption('Hi Taehee!')
                if player.guess == '901':
                    GameCaption('That is my birthday!')
                    player.star += 10
                pygame.display.update()
                player.guesses -= 1  # 한 번 추측하면 기회가 1 감소함
                if player.guesses == 0:  # 기회를 다 썼는데 실패했을 경우
                    player.guesses = 10
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/gameover.mp3')
                    pygame.mixer.music.play()
                    player.star = 0  # 별이 0개로 초기화됨
                    DISPLAYSURF.blit(lose, (0, 0))  # 패배 화면을 띄움
                    showSecretNum(secret_num)  # 비밀 숫자를 보여줌
                    pygame.display.update()
                    play_again()  # 다시 게임을 할 건지 물어보는 함수


def inputguess(pos, i):  # 키보드로 숫자를 입력할 수 있게 하는 함수
    while (i >= 0):  # i=0일 때까지 작동
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # 키보드를 눌렀을 경우 입력한 대로 pos에 들어감
                if event.key == pygame.K_0:
                    pos[i] = 0
                    i = i - 1
                elif event.key == pygame.K_1:
                    pos[i] = 1
                    i = i - 1
                elif event.key == pygame.K_2:
                    pos[i] = 2
                    i = i - 1
                elif event.key == pygame.K_3:
                    pos[i] = 3
                    i = i - 1
                elif event.key == pygame.K_4:
                    pos[i] = 4
                    i = i - 1
                elif event.key == pygame.K_5:
                    pos[i] = 5
                    i = i - 1
                elif event.key == pygame.K_6:
                    pos[i] = 6
                    i = i - 1
                elif event.key == pygame.K_7:
                    pos[i] = 7
                    i = i - 1
                elif event.key == pygame.K_8:
                    pos[i] = 8
                    i = i - 1
                elif event.key == pygame.K_9:
                    pos[i] = 9
                    i = i - 1
                elif event.key == pygame.K_BACKSLASH and player.star >= 3:  # 백슬래쉬를 눌렀고 별이 3개 이상인 경우
                    player.star -= 3  # 별이 3 감소하는 대신 기회가 1 늘어난다
                    player.guesses += 1
                    drawGameStatus()
                    pygame.display.update()
                elif event.key == pygame.K_ESCAPE:  # Esc 를 눌렀을 경우
                    terminate()  # 종료 함수
                else:
                    continue  # 위의 어떤 경우도 아니면 아무 일도 일어나지 않는다


def get_secret_num(num_digits):  # 비밀 숫자를 랜덤으로 생성하는 함수
    numbers = list(range(10))  # 0-9의 범위의 list 형으로 변경
    secret_number = ''  # 비밀 숫자를 초기화한다
    random.shuffle(numbers)  # list 의 값을 임의의 순서로 섞는다.
    for i in range(num_digits):  # 원하는 길이 만큼 반복하며 원하는 길이의 문자열을 만듬
        secret_number += str(numbers[i])
    return secret_number


def concequence(user_guess, secret_number):
    onestar = pygame.image.load("img/winscreen1.png")  # 별 1개 있는 화면
    twostar = pygame.image.load("img/winscreen2.png")  # 별 2개 있는 화면
    threestar = pygame.image.load("img/winscreen3.png")  # 별 3개 있는 화면
    bonusstar = pygame.image.load("img/winscreenbonus.png")  # 보너스 단계를 통과했을 때 화면
    bonus = pygame.image.load("img/bonusbonus.png")  # 보너스 단계에 진입했을 때 화면
    end = pygame.image.load("img/endscreen.png")  # 별 100개를 획득했을 때 뜨는 마지막 화면
    balloon1 = pygame.image.load("img/threeout.png")  # 아웃이 3개일 때 뜨는 말풍선
    balloon2 = pygame.image.load("img/noout.png")  # 아웃이 없을 때 뜨는 말풍선
    ballooncover = pygame.image.load("img/ballooncover.png")  # 말풍선 덮는 조각
    if user_guess == secret_number:  # 사용자가 선택한 값이 정답과 같으면 승리로 결과
        pygame.mixer.music.stop()
        pygame.mixer.music.load('music/win.mp3')
        pygame.mixer.music.play()
        drawGameStatus()
        pygame.display.update()
        if player.digits == 7:  # 보너스 단계를 통과했을 경우
            DISPLAYSURF.blit(bonusstar, (0, 0))  # 통과 화면을 띄운다
            player.star += 25  # 별이 25개 증가한다
            player.check_bonus = 1  # check_bonus 변수가 1로 바뀐다
            pygame.display.update()
        elif player.guesses >= 7:  # 일반 단계를 기회가 7번 이상 남은 채로 통과했을 경우
            player.star += 3  # 별이 3개 증가한다
            DISPLAYSURF.blit(threestar, (0, 0))  # 통과 화면을 띄운다
            pygame.display.update()
        elif player.guesses >= 4:
            player.star += 2  # 별이 2개 증가한다
            DISPLAYSURF.blit(twostar, (0, 0))  # 통과 화면을 띄운다
            pygame.display.update()
        else:
            player.star += 1  # 별이 1개 증가한다
            DISPLAYSURF.blit(onestar, (0, 0))  # 통과 화면을 띄운다
            pygame.display.update()
        player.digits = 3  # 일반 단계로 설정하기 위해 자릿수를 3으로
        player.guesses = 10  # 일반 단계로 설정하기 위해 기회를 10번으로
        if player.star >= 100:  # 별 100개를 획득했을 경우
            DISPLAYSURF.blit(end, (0, 0))  # 마지막 화면을 띄운다
            while checkForKeyPress() == None:
                pygame.display.update()
            terminate()  # 키보드를 누르면 종료
        if player.star >= player.laststar + 10 and player.star <= player.laststar + 20:  # 보너스 단계를 진입할 차례인 경우
            player.digits = 7  # 보너스 단계로 설정하기 위해 자릿수를 7로
            player.guesses = 30  # 보너스 단계로 설정하기 위해 기회를 30번으로
            player.laststar = player.star  # laststar을 현재 별의 개수로 바꾼다
            DISPLAYSURF.blit(bonus, (0, 0))  # 보너스 단계 시작 화면을 띄운다
            while checkForKeyPress() == None:
                pygame.display.update()
            gameScreen()  # 키보드를 누르면 게임 화면으로 이동한다
        elif player.star > player.laststar + 20:  # 보너스 단계를 마친 경우
            player.digits = 3  # 일반 단계로 설정하기 위해 자릿수를 3으로
            player.guesses = 10  # 일반 단계로 설정하기 위해 기회를 10번으로
            player.laststar = player.star  # laststar을 현재 별의 개수로 바꾼다
            DISPLAYSURF.blit(bonusstar, (0, 0))
            while checkForKeyPress() == None:
                pygame.display.update()
        play_again()  # 플레이어가 게임을 다시 지속할지 결정

    player.s = 0  # strike 인 경우 갯수 세기
    player.b = 0  # ball  인 경우 갯수 세기
    player.o = 0  # out    인 경우 갯수 세기
    for i in range(len(player.guess)):  # 0 ~ 사용자가 선택한 문자열의 갯수
        if user_guess[i] == secret_number[i]:  # strike 인 경우
            player.s += 1
        elif user_guess[i] in secret_number:  # ball 인 경우
            player.b += 1
        else:  # out 인 경우
            player.o += 1
    if player.digits == 3:
        DISPLAYSURF.blit(ballooncover, (290, 72))
    if player.o == 3 and player.digits == 3:  # 일반 단계에서 3개가 다 아웃이면 말풍선 1
        DISPLAYSURF.blit(ballooncover, (290, 72))
        DISPLAYSURF.blit(balloon1, (300, 90))
    elif player.o == 0 and player.digits == 3:  # 일반 단계에서 3개가 다 아웃이 아니면 말풍선 2
        DISPLAYSURF.blit(ballooncover, (290, 72))
        DISPLAYSURF.blit(balloon2, (292, 125))


def play_again():  # 플레이어가 게임을 다시 지속할지 결정하는 함수
    GameCaption('Continue? (y,n)')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:  # n을 누르면 종료
                    terminate()
                elif event.key == pygame.K_y:  # y를 누르면 게임 화면으로 넘어감
                    gameScreen()
                else:  # 다른 키를 누르면 아무 일도 일어나지 않음
                    continue


def checkForKeyPress():  # 키를 눌렀는지 확인하는 함수
    checkForQuit()  # 그만 두는 명령을 내렸는지 확인
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def GameCaption(text):  # 화면 아래에 문장을 띄우는 함수
    cover = pygame.image.load("img/captioncover.png")  # 일반 단계에서 문장의 배경
    bcover = pygame.image.load("img/captioncoverbonus.png")  # 보너스 단계에서 문장의 배경
    wcover = pygame.image.load("img/captioncoverwin.png")  # 보너스 완료 화면에서 문장의 배경
    if player.check_bonus == 1:  # 보너스 단계를 완료했을 경우
        DISPLAYSURF.blit(wcover, (0, 398))
    elif player.digits == 3:  # 일반 단계의 경우
        DISPLAYSURF.blit(cover, (0, 398))
    else:  # 보너스 단계의 경우
        DISPLAYSURF.blit(bcover, (1, 398))
    if player.check_bonus == 1:
        pressKeySurf, pressKeyRect = makeTextObjs(text, BASICFONT, BLACK)  # 보너스 통과 화면은 밝아서 글씨 검정
        player.check_bonus = 0  # 변수 초기화
    else:
        pressKeySurf, pressKeyRect = makeTextObjs(text, BASICFONT, TEXTCOLOR)  # 나머지 화면은 글씨 하양
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 220)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()


def showSecretNum(secret_num):  # 패배했을 경우 비밀 숫자를 알려주는 함수
    gameSurf = BASICFONT.render('The secret number was %s' % secret_num, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (73, 297)
    DISPLAYSURF.blit(gameSurf, gameRect)


def drawGameStatus():  # 게임의 여러 수치를 화면에 보여주는 함수
    # 별의 개수를 보여줌
    cover = pygame.image.load("img/starcover.png")  # 일반 단계에서 별의 개수의 배경 조각
    bcover = pygame.image.load("img/starcoverbonus.png")  # 보너스 단계에서 별의 개수의 배경 조각
    if player.digits == 3:  # 일반 단계의 경우
        DISPLAYSURF.blit(cover, (60, 0))
    else:  # 보너스 단계의 경우
        DISPLAYSURF.blit(bcover, (65, 0))
    gameSurf = BASICFONT.render('X%s' % player.star, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (60, 23)
    DISPLAYSURF.blit(gameSurf, gameRect)

    # 사용자가 입력한 숫자를 보여줌
    cover = pygame.image.load("img/captioncover.png")  # 일반 단계에서 추측한 수의 배경 조각
    bcover = pygame.image.load("img/captioncoverbonus.png")  # 보너스 단계에서 추측한 수의 배경 조각
    if player.digits == 3:
        DISPLAYSURF.blit(cover, (0, 397))
    else:
        DISPLAYSURF.blit(bcover, (0, 401))
    gameSurf = BASICFONT.render('Your Guess: %s' % player.guess, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 220)
    DISPLAYSURF.blit(gameSurf, gameRect)

    # 남은 기회의 개수를 알려줌 (사탕의 개수)
    cover = pygame.image.load("img/guesscover.png")
    bcover = pygame.image.load("img/guesscoverbonus.png")
    if player.digits == 3:
        DISPLAYSURF.blit(cover, (595, 0))
    else:
        DISPLAYSURF.blit(bcover, (595, 0))
    gameSurf = BASICFONT.render('X%s' % player.guesses, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (600, 23)
    DISPLAYSURF.blit(gameSurf, gameRect)

    # S의 개수를 알려줌
    gameSurf = HINTFONT.render('| %s' % player.s, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (170, 100)
    DISPLAYSURF.blit(gameSurf, gameRect)

    # B의 개수를 알려줌
    gameSurf = HINTFONT.render('| %s' % player.b, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (170, 208)
    DISPLAYSURF.blit(gameSurf, gameRect)

    # O의 개수를 알려줌
    gameSurf = HINTFONT.render('| %s' % player.o, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.topleft = (170, 314)
    DISPLAYSURF.blit(gameSurf, gameRect)

    while checkForKeyPress() == None:
        pygame.display.update()


def checkForQuit():  # Esc 를 누르면 종료하게 해주는 함수
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def makeTextObjs(text, font, color):  # 텍스트 생성 함수
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def terminate():  # 종료 함수
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
