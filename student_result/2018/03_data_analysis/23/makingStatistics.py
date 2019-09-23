import csv
import operator
from sys import exit

# file을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data로 변경
try:
    f = open('2017년_3월_역별_일별_시간대별_승차인원.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없어요...")
    exit(0)
else:
    data = csv.reader(f)

try:
    # 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
    first_row = 0

    # 데이터를 분석해서 저장할 set Type
    date_set = set([])
    station_set = set([])
    time_list = []
    table = {}
    # 한개씩 꺼내서 데이터 분석
    for row in data:
        if first_row < 1:
            print(row)
            for time in row[3:]:
                time_list.append(time)
            first_row += 1
            continue

        date_set.add(row[1])
        station_set.add(row[0])

    for station in station_set:
        table[station] = {}
        for time in time_list:
            table[station][time] = 0

    # 날짜와 역을 저장할 dictionary 만들기
    date_count = {}
    station_count = {}

    for date in date_set:
        date_count[date] = 0

    for station in station_set:
        station_count[station] = 0

    f = open('2017년_3월_역별_일별_시간대별_승차인원.csv', encoding='cp949')
    data = csv.reader(f)

    first_row = 0

    for row in data:
        if first_row < 1:
            first_row += 1
            continue

        row_sum = 0
        for count in row[3:]:
            row_sum += int(count.replace(',', ''))  # 숫자의 쉼표 지우기
        # 필요한걸 싹다 더하세요
        date_count[row[1]] += row_sum
        station_count[row[0]] += row_sum

    maxnumber = 0  # 승차인원이 가장 많은 날 숫자
    minnumber = 9999999999  # 승차인원이 가장 적은 날 숫자
    maxname = 'EMPTY'  # 승차인원이 가장 많은 날
    minname = 'EMPTY'  # 승차인원이 가장 적은 날

    for date in date_set:
        if date_count[date] > maxnumber:  # maxnumber보다 많으면 넣으세요
            maxnumber, maxname = date_count[date], date
        if date_count[date] < minnumber:  # minnumber보다 작으면 넣으세요
            minnumber, minname = date_count[date], date

    maxnumber2 = 0  # 승차인원이 가장 많은 역 숫자
    minnumber2 = 9999999999  # 승차인원이 가장 적은 역 숫자
    maxname2 = 'EMPTY'  # 승차인원이 가장 많은 역
    minname2 = 'EMPTY'  # 승차인원이 가장 적은 역

    for station in station_set:
        if station_count[station] > maxnumber2:  # maxnumber2보다 많으면 넣으세요
            maxnumber2, maxname2 = station_count[station], station
        if station_count[station] < minnumber2:  # minnumber2보다 작으면 넣으세요
            minnumber2, minname2 = station_count[station], station

    print('3월의 승차인원이 가장 많은 날은 %s이고, 그 인원은 %d명입니다.' % (maxname, maxnumber / 2))  # 2017년 3월 10일은 박근혜 전 대통령 탄핵일
    print('3월의 승차인원이 가장 적은 날은 %s이고, 그 인원은 %d명입니다.' % (minname, minnumber / 2))
    print('3월의 승차인원이 가장 많은 역은 %s이고, 그 인원은 %d명입니다.' % (maxname2, maxnumber2 / 2))
    print('3월의 승차인원이 가장 적은 역은 %s이고, 그 인원은 %d명입니다.' % (minname2, minnumber2 / 2))

except KeyboardInterrupt:
    print("아 왜 방해하십니까...")
