import csv
import sys

try:
    fp = open('data1.csv', encoding='cp949')
except FileNotFoundError:
    print('No file')
    exit(0)
else:
    data = csv.reader(fp)

i = 0
operate = 0
# 과제에서 4개 이상의 의미있는 데이터를 도출하라 하셔서 4개를 뽑아보았다.
# operate는 내가 처리한 데이터 중 무엇을 볼 것인지 정하는 변수다.
# operate는 1~4까지의 값을 가질 수 있으며 선택에 따라 아래와 같은 데이터를 보여준다.

while operate not in ['1', '2', '3', '4']:
    print('1~4까지의 숫자를 입력하세요')
    print('1: 입력으로 시작하는 품목명과 HSK품목분류, 수출입여부를 알려줍니다. ex)입력:갈치,대서양 등')
    print('2: 당해 누계 수출입중량에 비해 당월 수출입중량이 제일 큰 파일 상 인덱스, 품목, 양을 출력합니다.')
    print('3: 숫자 하나를 입력받아 그 index의 값이 가장 큰 품목과 그 양을 출력합니다. ex)입력:1')
    print('4: 입력을 받아 좋아하는 품목이면 조리형태를 HSK품목, 수출입 여부와 함께 출력합니다.')
    operate = input()

    # 데이터 도출의 첫째다.
    if operate == '1':
        find = input()
        notfound = 0
        # find라는 변수에 정보를 찾을 품목을 입력받아 저장한다.
        for row in data:
            check = 0
            # index초과가 일어나는 것을 막기 위한 if문이다.
            if len(row[3]) > len(find):
                # 처음부터 find에 해당하는 길이까지의 문자가 전부 find와 같다면 check가 그대로 0이다.
                for i in range(0, len(find), 1):
                    if row[3][i + 1] != find[i]: check = 1
                # 그래서 check가 그대로 0이면 알맞은 데이터를 찾은 것이니, 그것을 출력한다.
                if check == 0:
                    print(row[3], ',', 'HSK품목분류:', row[1], ',', row[7])
                    notfound = 1
                # 하나라도 그런 품목이 있으면 notfound의 값은 0에서 1이 된다.
        # 그래서 notfound의 값이 그대로 0일 경우 그런 품목이 없다고 출력한다.
        if notfound == 0: print('그런 품목은 없습니다')

    # 데이터 도출의 둘째다.
    if operate == '2':
        index = 2
        maxvalue = 0
        notzeroindex = 2
        printrow = 'init'
        for row in data:
            if row[0] != '기준년월':
                # data1은 당월 수출입중량을 저장하는 변수다.
                # data2는 당해 누계 수출입중량을 저장하는 변수다.
                data1 = 0
                data2 = 0
                # 당월 수출입중량과 당해 누계 수출입중량은 문자열의 형태로 저장되어 있기 때문에
                # 아래와 같이 정수로 바꾸어 data1과 data2에 저장한다.
                for i in range(0, len(row[8]) - 2, 1):
                    data1 = data1 * 10 + int(row[8][i + 1])
                for i in range(0, len(row[10]) - 2, 1):
                    data2 = data2 * 10 + int(row[10][i + 1])
                # data2가 0인 경우는 zerodivision에러가 나오기 때문에 따로 처리해 주었다.
                # 또한 data1==data2인 경우, 즉 그 해에 거래가 금월에만 일어난 경우도 따로 처리했다.
                if data2 == 0 or data1 == data2:
                    print('index:', index, row[3], row[8], row[10])
                # 위에서 처리한 예외에 해당하지 않는 경우에 당해 누계 수출입중량에 비해
                # 당월 수출입중량이 제일 큰 품목에 대한 정보를 printrow에 저장한다.
                # index도 notzeroindex에 저장해준다.
                elif maxvalue < (data1 / data2):
                    maxvalue = data1 / data2
                    printrow = row
                    notzeroindex = index
                index += 1
        print('누계 수출입중량이 0이 아니고 당월 수출입중량과 같지 않은 품목')
        # 위에서 처리된 값을 출력한다.
        print('index:', notzeroindex, printrow[3], printrow[8], printrow[10])

    # 데이터 도출의 셋째다.
    if operate == '3':
        index = 2
        maxvalue1 = 0
        notzeroindex1 = 2
        printrow1 = 'init'
        yo = ['1', '2', '3', '4']
        a = 'init'
        print('1:당월 수출입중량')
        print('2:당월 수출입미화금액')
        print('3:당해 누계 수출입중량')
        print('4:당해 누계 수출입미화금액')
        while a not in yo:
            a = input()
        # 변수 a에 1~4까지의 값을 입력받아 모든 품목에 대하여 a의 번호에 해당하는 값들끼리 비교해
        # 제일 큰 값을 가지는 품목을 출력한다.
        for row in data:
            if row[0] != '기준년월':
                # print(row)
                data1 = 0
                # 위와 마찬가지로 데이터가 문자열로 저장되어 있기 때문에 정수로 바꾸어 data1에 저장
                for i in range(0, len(row[int(a) + 7]) - 2, 1):
                    data1 = data1 * 10 + int(row[int(a) + 7][i + 1])
                # 큰 값을 maxvalue1에 저장하고 나중에 출력할 데이터를 printrow1에 저장한다.
                # 그에 해당하는 index도 notzeroindex1에 저장한다.
                if maxvalue1 < data1:
                    maxvalue1 = data1
                    printrow1 = row
                    notzeroindex1 = index
                index += 1
        # 위에서 처리한 값을 출력한다.
        print('index:', notzeroindex1, printrow1[3], printrow1[int(a) + 7])

    # 데이터 도출의 넷째다.
    if operate == '4':
        # dic이란 이름의 dictionary에 내가 좋아하는 품목과 조리 형태를 적어놓았다.
        dic = {'넙치': '회', '고등어': '구이', '새우': '튀김', '미꾸라지': '탕', '연어': '회', '조기': '구이',
               '갈치': '구이', '명란': '젓'}
        # find를 입력받아 내가 좋아하는 목록(dic)에 있으면 위에 표시한 내용들을 출력한다.
        find = 'init'
        find = input()
        try:
            dic[find]
        except KeyError:
            # dic에 find가 없으면 내가 좋아하는 게 아니라는 뜻이다.
            print('그건 내가 좋아하는 게 아니다.')
        else:
            notfound = 0
            # csv파일에서 내가 좋아하는 품목에 대한 정보를 찾는다.
            for row in data:
                check = 0
                # 파일에 있는 품목의 이름이 find보다 짧으면 밑에서 index초과가 일어날 수 있기 때문에
                # 그것을 막기위한 if문이다.
                if len(row[3]) > len(find):
                    for i in range(0, len(find), 1):
                        if row[3][i + 1] != find[i]: check = 1
                    if check == 0:
                        print(dic[find], row[3], ',', 'HSK품목분류:', row[1], ',', row[7])
                        notfound = 1
            # 내가 좋아하는 품목이 파일에 없을 경우 notfound는 그대로 0의 값을 가지기 때문에
            # 그런 품목이 없다는 것을 출력한다.
            if notfound == 0: print('그런 품목은 없습니다')
