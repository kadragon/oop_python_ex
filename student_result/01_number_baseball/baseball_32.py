#초기조건
import random
# import Character
import time


flowy='''
    `oooooooo/            /oooooooo`
    :sss``+++hMMMMNsssss`  -sssNMMMMMMy+``sss:
    .hmMMMhhho .::::::::::   `::::::::::` yhMMMmh.
    mmMMMMMMN..                            mMMMMMMmm
    `:NNN/```  `````NNNNNNNNNNNNNNNN`````  ```/NNN:`
    .......         .+MMMMMMMMMMMMMMMMMMMMMMMMMM+.         .......
    :/MMMMMMM:-     :/MMMMMMMMNhhhNMMMMNhhhNMMMMMMMM/:     -:MMMMMMM/:
    :+NMMMMMMMMMd   :+NMMMMMMMMMd   yMMMMy   dMMMMMMMMMN+:   dMMMMMMMMMN+:
    -omMMNoooooooo/   yMMMMMMMMMMMd   yMMMMy   dMMMMMMMMMMMy   /ooooooooNMMmo-
    +MMMMNyyyyyyy     yMMMMMMMMMMMd   yMMMMy   dMMMMMMMMMMMy     yyyyyyyNMMMM+
    +MMMMMMMMMMMMds   yMMMMMMMMMMMd   yMMMMy   dMMMMMMMMMMMy   sdMMMMMMMMMMMM+
    `...NMMMMMMMMMd   yMMMMMMo.dMMMmmmNMMMMNmmmMMMd.oMMMMMMy   dMMMMMMMMMN...`
    `mNMMMMMMd.`   mMMMMMM-   ............   -MMMMMMm   `.dMMMMMMNm`
    :dddddddd+   ydMMMMM+- .dddddddddddd. -+MMMMMdy   +dddddddd:
    ./.  `ydMMMMM/:            :/MMMMMdy`  ./.
    ooohM/    .odMMMMmoooooooooooomMMMMdo.    /Mhooo
    +sMMMMM/      -+++MMMMMMMMMMMMMMMM+++-      /MMMMMs+
    /hNMMMMh:shhy       ::::::::::::::::       yhhs:hMMMMNh/
    sMMMMd.+mNMMMmmmmm-                  -mmmmmMMMNm+.dMMMMs
    sMMMMd`oMMMMMMMMMMNNNNmmmmm``mmmmmNNNNMMMMMMMMMMo`dMMMMs
    +mmmMMMMMMMMMMNmmmmmmy            ymmmmmmNMMMMMMMMMMmmm+
    hhhhhhhhhho                          ohhhhhhhhhh
    -+++`
    .ohMMMso
    -MMMMMMm
    ddMMMMM:-
    MMMMM+.
    mNMMM+.
    -MMMMM/-
    .ydMMMMN/-
    -omMMMMy
    :+NMMms:
    mMMMM+
    smMMMMMNm-
    oN-   `+NMMMMMMMMM-  -No
    +m/. -mNMMMMMMMMNm- ./m+
    sh:- :hhhhhhhh: -:hs
    ss++++++++++++ss
    `oooooooooooo`
    '''
annoying_dog='''
    ░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
    ░█░░░░░░░░▀▄░░░░░░▄░
    █░░▀░░▀░░░░░▀▄▄░░█░█
    █░▄░█▀░▄░░░░░░░▀▀░░█
    █░░▀▀▀▀░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░█
    ░█░░▄▄░░▄▄▄▄░░▄▄░░█░
    ░█░▄▀█░▄▀░░█░▄▀█░▄▀░
    ░░▀░░░▀░░░░░▀░░░▀░░░
    '''

papyrus='''
    +NMMMMMMMMMN+
    `/NMMMMMMMMMMMMMN+`
    `/d+ohMMMMMMMMMMMMMMm+`
    :MMMM`:hNMMMMMMMMMMMMM:
    :MMMM  osmMMdoo/+oooNM/
    :MMMM  dNMMMMNh `NNNMM/
    :MMMs  dMMMMMm+ `sMyNM/
    .oyymmmMd:yMMNmmmmy/+y-
    -y:sMMMM:.-sMMMMMM N/`
    -y`MMMMdmdmMMMMN: N.
    ` +mmmmmmmmmmdo  N.
    ss-+s:/s+-yd  N.    ```````
    :++---     sN-hN+oNy-Ns  N. `-/+ymdd+o```
    hNMMNo.      .`.-``-.`.   N./o//yds:o:dddd+:.
    yNMMMs       -`.`..`.`- -hd. .sds.`:ooooo:yddo.        .--.
    dMMMmo.    .+`s:++/s.oyMm`.smm+`/hMMMMMMh/`-ymys.-yyyo///+/.
    `.-ss+   /mMMMMm+.  ddoo+oo+oodm+`.dMy-/hNMMMMMMMMN+`-yMMNdm++.   `+s
    `:ymNMN. +. /dNMMMMm+`-..........-`+mMy.:hMMMMMMMMMMMN+ -sso..      -:`
    oNMMMNs `Nm+..+dMMMMMmm+/.``-///+mmMNh+.sMMMMMMMMMMMMM+
    oNMMMMd  dMMMm+..+dMMMMMMMmddmMMMMNddohN/+mMMMMMMMMMMMM+
    yMMMMMd  MMMMMMm+`:MN/MMMMMMMMNmhoohhMMM+`+NMMMMMMMMMMs.
    sNMMMMd  /MMMMMMMy-oNy/modNNy+syhMMMMMMMMo`.sNMMMMMNNo.
    sMMMMNo  +NMMMMMMmosm`oNyssshdooosMMMMMMMh: .osssss.
    `/dNMMN+  oNMMMMMMMmoo.NMMNNMNh+omMMMMMMMo` `odooos.
    :yy//yyy   omMMMMMMMMmmMMMMMMdosNsMMMMMd/`  .osmmo`
    .sy///       .-omMMMMMMMMMMMMMdoyMMMMdd/`    :MMMM`
    .sNMNo            ./ommmmmmmmmmmmmmd///        :MMMm`
    `mMMM+                    ``````                :MMM
    +Nyoooooooooooooooooo/    MMMMMMd:              :MMM
    `+ssdMMMMMMMMyssss/-++/  ````+s/               :MMM
    `........     +NMMMd  :do.                 -hMM
    .--/dh  mMMm/                 -N-
    `.  ...   `./ys.   mMMM+                -hh
    :mo.mmmyssdNMMMh ` dNNN/                :d``
    .yNmss.+smMMMm+.oNo.````                :d`N
    `.yMNNNNMMy``+yyymNNNs//////          :d.M
    ..shhh+``/hmmmoooyhhhdMMN          :d.M                    .-
    :dd.dMMMMMmdddyoo-          :m:h                ---oms
    /MNs`/dmMMMMNmho+           -h:-yy`  `.....-yyyymNNMNo
    /MMm  ``/+++::hNd`          `:sNmo``+dNNNNNNMMMMMMNy:`
    /MNo         -hMMd          -mNM.`/dNMMMMMMMMNNNys:`
    .sMd           :MMN/         `.-y dMMMMMMMNyyy...
    +MMd           `+MMM:             hhNMMMMMNy:::
    /mMd- ---        `+MMM:              -:yddddddd:
    +NMh `///+s.      `+mMm. ::`            ```````
    +.`````:o/  ```sN:        `o. `+do`
    .dmmms+////+mmmMy.    .:    `/hNMNo`
    -mMMmho-/osMMMM-   .oy- `::dNd/omNo
    -yNmhhysdddMMM-   .odhhdMMd/`.odmNo
    yNh+/..-yMMM-     .oNMMMhysds-oMd`
    sNMMMNNNMMM:       `+NMMMy-/dMMMh
    `:hm+...sMMN:        `oNMMNMMMd+-ooooooooo:`
    ``//////yNmmmmmMMMs.         .mMMMMy-oNMMMMMMMMMNh:
    `/ddMMMMMMMMMMMMMMMMM/          mMMMMNmMMMMMMMMMMMMMd-
    -dMMMMMMMMMMMMMMMMMMMM/          yNMMMMMMMMMMMMMMMMMMMd
    -NMMMMMMMMMMMMMMNN////.           hNNNNNNMMMMMMMMMMMMMh
    `+++++++++++++/                        .++++++++++++:
    '''

def Flowey():
    print(flowy)

def Annoying_dog():
    print(annoying_dog)

def Papyrus():
    print(papyrus)


a=list(range(10))
b=[]
c=[]
strike=0
ball=0
out=0
ans=True
g=0
flag2=True
m=0

def shuffle():
    global m
    m=0
    flag3=True
    while flag3:
        try:
            m=int(input('How Many numbers to Challenge? : '))
            flag3=False
        except ValueError:
            continue


    random.shuffle(a)
    for i in range(m):
        b.append(a[i])

    global strike
    strike=0
    global ball
    ball=0
    global out
    out=0
    global g
    g=0
    global flag2
    flag2=True

def output():
    global m
    f=True
    while f:
        global c
        flag=False
        c=input('Enter your guess : ').split()
        d=[]
        for h in range(len(c)):
            d+=list(c[h])
        c=d[:]
        if len(c)!=m:
            Character.Annoying_dog()
            print('Nonono try it again')
            continue

        try:
            c=list(map(int,c))
        except ValueError:
            Character.Annoying_dog()
            print('Nonono try it again')
            continue

        for i in range(m):
            if c[i]<0 or c[i]>9:
                Character.Annoying_dog()
                print('Nonono try it again')
                flag=True
                break

        if flag:
            continue
        f=False


def judge():
    global strike
    global ball
    global out
    global m

    for i in range(m):
        if c[i]==b[i]:
            strike+=1
            c[i]=-1

    for i in range(m):
        if c[i] in b:
            ball+=1
            c[i]=-1

    for i in range(m):
        if c[i]!=-1:
            out+=1

def consequence():
    global strike
    global ball
    global out
    global g
    global flag2

    print('strike : %d' %strike)
    print('ball : %d' %ball)
    print('out : %d' %out)

    if g>=10:
        Character.Papyrus()
        print('Neheheh, You lost the game!')
        flag2=False

    strike=0
    ball=0
    out=0

def ask_continue():
    global ans
    time.sleep(1)
    print('Do you want to continue? : ', end='')

    answer=input().lower()
    if answer=='yes' or answer=='y':
        print('Okay, Do Your Best\n\n\n')
    elif answer=='no' or answer =='n':
        print('Well.. bye bye')
        ans=False
    else:
        print('Urmm...pardon?')
        ask_continue()

def intro():
    Character.Flowey()
    time.sleep(3)
    print('\t\t\t Howdy! welcome to the game!\n')
    time.sleep(1)
    print('\t\t\t You know the rules right?\n\n')
    time.sleep(1)








#진짜 과정 시작
intro()

while ans:
    shuffle() #섞는다

    while flag2:
        g+=1 #횟수를 센다
        output() #입력을 받는다
        judge() #맞았는지 판단
        if strike==m: #맞으면
            Character.Papyrus()
            print('\t\t\tHuman! You won the game!\n\n\n\n\n')
            break
        consequence() #결과 출력

    ask_continue() #계속할것인지 물음
