# https:

import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

try:
    ''' 
    1. '2017년_도로형태별_가해운전자차량용도별_교통사고' 이용
    - 도로형태별 교통사고 발생건수
    - 교통사고 발생건수가 많은 차종 순위 
    '''

    # file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
    try:
        f = open('17_data_traffic_accident_road_car_type.csv', encoding='cp949')
    except FileNotFoundError:
        print("파일이 없는데요?!")
        exit(0)
    else:
        data = csv.reader(f)

    # 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
    first_row = 0

    # 데이터를 분석해서 저장할 dictionary Type
    road_dict = {}
    car_dict = {}

    # 한개씩 꺼내서 데이터 분석
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는 지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
            if first_row == 1:
                continue

        # dict 가 선언되어 있는지 확인하여 값 설정
        ''' 도로형태별 교통사고 발생건수 통계 내기 '''
        if row[0] not in road_dict:
            road_dict.setdefault(row[0], int(row[4]))
        else:
            road_dict[row[0]] += int(row[4])

        ''' 교통사고 발생건수가 많은 차종 순위 통계 내기 '''
        if row[2] not in car_dict:
            car_dict.setdefault(row[2], int(row[4]))
        else:
            car_dict[row[2]] += int(row[4])

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_road = sorted(road_dict.items(), key=operator.itemgetter(0))  # index 기준
    sorted_car = sorted(car_dict.items(), key=operator.itemgetter(1), reverse=True)  # value 기준, 역순 정렬(발생건수 많은순)

    print("=" * 115)
    print("1. 도로형태별 교통사고 발생건수")
    for row in sorted_road:
        print("%s: %d" % (row[0], row[1]))
    print("=" * 35)
    print("2. 교통사고 발생건수가 많은 차종 순위")
    for i in range(5):
        print(sorted_car[i][0])
    print("=" * 80)

    '''
    2. '2017년_도로형태별_시간대별_교통사고' 이용
    - 시간대별 교통사고 발생건수
    - 부상자수가 가장 많은 도로형태 순위
    '''

    # file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
    try:
        f = open('17_data_traffic_accident_time.csv', encoding='cp949')
    except FileNotFoundError:
        print("파일이 없는데요?!")
        exit(0)
    else:
        data = csv.reader(f)

    # 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
    first_row = 0

    # 데이터를 분석해서 저장할 dictionary Type
    time_dict = {}
    injured_dict = {}

    # 한개씩 꺼내서 데이터 분석
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는 지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
            if first_row == 1:
                continue

        # dict 가 선언되어 있는지 확인하여 값 설정
        ''' 시간대별 교통사고 발생건수 통계 내기 '''
        if row[1] not in time_dict:
            time_dict.setdefault(row[1], int(row[2]))
        else:
            time_dict[row[1]] += int(row[2])

        ''' 부상자수가 가장 많은 도로형태 순위 통계 내기 '''
        if row[0] not in injured_dict:
            injured_dict.setdefault(row[0], int(row[4]))
        else:
            injured_dict[row[0]] += int(row[4])

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_time = sorted(time_dict.items(), key=operator.itemgetter(0))  # index 기준
    sorted_injured = sorted(injured_dict.items(), key=operator.itemgetter(1), reverse=True)  # value 기준, 역순 정렬(부상자수 많은순)

    print("=" * 80)
    print("3. 시간대별 교통사고 발생건수")
    for row in sorted_time:
        print("%s: %d" % (row[0], row[1]))
    print("=" * 35)
    print("4. 부상자수가 가장 많은 도로형태 순위")
    for i in range(5):
        print(sorted_injured[i][0])
    print("=" * 35)

except KeyboardInterrupt:
    print("왜 실행중에 괴롭히세요!")
