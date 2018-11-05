# 데이터분석하기
# 객지과제2


import csv
from sys import exit  # 프로그램 종료 시키기

# file 을 열기 위해서 시도해보고, 없으면 알려주고, 있으면 data 로 변경
try:
    # 2017년 지역별 도서관 현황 정보 일부 발췌한 것
    f = open('지역별도서관현황_20181005221249.csv', encoding='cp949')
except FileNotFoundError:
    print("파일을 추가하고 다시 시도하십시오")
    exit(0)
else:
    data = csv.reader(f)

# 분석한 데이터 저장을 위해 변수를 선언
# 가장 도서관이 많은 지역과 그 지역의 도서관 수
max_library = 0
max_place = ''
max_library_list = []

# 가장 도서관이 적은 지역과 그 지역의 도서관 수
min_library = 1000
min_place = ''
min_library_list = []

# 도서관 당 예산 지원이 가장 많은 지역
max_money = 0
max_money_place = ''
max_money_list = []

# 도서관 당 예산 지원이 가장 적은 지역
min_money = 10000
min_money_place = ''
min_money_list = []

# 데이터 형태 참고
# ['지역', '도서관 수(관)', '1관당 결산 예산액(백만원)']
# ['서울', '160', '1021']

row_cnt = 0

# 원래 데이터를 공개할 때는 뜸을 들여야 하는거죠
print("분석한 데이터를 보려면 아무키나 입력하십시오")
# 절대 try except 문을 쓰려고 억지로 기능을 넣은 건 아닙니당ㅋㅋ
try:
    a = input()
    pass
except KeyboardInterrupt:
    print("왜 안봐잉 열심히 만들었는뎅")
    exit(0)

for row in data:
    # 첫 번째 행은 항목명이기 때문에 제외하기 위한 부분
    if row_cnt == 0:
        print(row, '\n')
        row_cnt = 1
        continue

    # 원하는 데이터가 아니거나, 잘못된 값이 들어가 있는 경우를 제외하기 위해
    if len(row) == 0 or row[0][0] == '':
        continue

    if max_library < int(row[1]):
        max_library = int(row[1])
        max_place = row[0]
        max_library_list = row

    if min_library > int(row[1]):
        min_library = int(row[1])
        min_place = row[0]
        min_library_list = row

    if max_money < int(row[2]):
        max_money = int(row[2])
        max_money_place = row[0]
        max_money_list = row

    if min_money > int(row[2]):
        min_money = int(row[2])
        min_money_place = row[0]
        min_money_list = row

# 분석 결과 출력, 선정된 도시의 정보는 모두 출력해줌
print("가장 도서관이 많은 지역은 : \t\t [%s] %4d 개" % (max_place, max_library))
print(max_library_list)
print("가장 도서관이 적은 지역은 : \t\t [%s] %4d 개" % (min_place, min_library))
print(min_library_list)
print("도서관당 예산이 가장 많은 지역은 : \t [%s] %4d 원" % (max_money_place, max_money))
print(max_money_list)
print("도서관당 예산이 가장 적은 지역은 : \t [%s] %4d 원" % (min_money_place, min_money))
print(min_money_list)
