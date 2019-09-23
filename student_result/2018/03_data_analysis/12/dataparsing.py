import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('2017년_요일별_시간대별_교통사고.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 데이터를 분석해서 저장할 dictionary Type
time_dict = {}  # 시간대별 발생건수
day_dict = {}  # 요일별 발생건수
time_dead = {}  # 시간대별 사망자수
day_dead = {}  # 요일별 사망자수
die_per_dead = {}  # 시간대별 발생건수 대비 사망자수

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
    # 시간대별 발생건수 통계 내기
    if row[0] not in time_dict:
        time_dict.setdefault(row[0], int(row[2]))
    else:
        time_dict[row[0]] += int(row[2])

    # 요일별 발생건수 통계 내기
    if row[1] not in day_dict:
        day_dict.setdefault(row[1], int(row[2]))
    else:
        day_dict[row[1]] += int(row[2])

    # 시간대별 사망자수 통계 내기
    if row[0] not in time_dead:
        time_dead.setdefault(row[0], int(row[3]))
    else:
        time_dead[row[0]] += int(row[3])

    # 요일별 사망자수 통계 내기
    if row[1] not in day_dead:
        day_dead.setdefault(row[1], int(row[3]))
    else:
        day_dead[row[1]] += int(row[3])

    # 발생건수 대비 사망자수를 구하는 과정에서 0으로 나눈 에러 잡기
    try:
        dpd = int(row[3]) / int(row[2])
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        exit(0)

    # 교통사고 발생건수 대비 사망자수 통계
    if row[0] not in die_per_dead:
        die_per_dead.setdefault(row[0], dpd)
    else:
        die_per_dead[row[0]] += dpd

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_time = sorted(time_dict.items(), key=operator.itemgetter(0))  # index(시간대별) 기준
sorted_day = sorted(day_dict.items(), key=operator.itemgetter(0))  # index(요일별) 기준
sorted_time_dead = sorted(time_dead.items(), key=operator.itemgetter(0))
sorted_day_dead = sorted(day_dead.items(), key=operator.itemgetter(0))
sorted_dpd = sorted(die_per_dead.items(), key=operator.itemgetter(1), reverse=True)

print("=" * 30)
print("시간대별 총 교통사고 발생건수")
for row in sorted_time:
    print("%s: %d회" % (row[0], row[1]))

print("=" * 30)
print("요일별 총 교통사고 발생건수")
for row in sorted_day:
    print("%s: %d회" % (row[0], row[1]))

print("=" * 30)
print("시간대별 총 사망자수")
for row in sorted_time_dead:
    print("%s: %d명" % (row[0], row[1]))

print("=" * 30)
print("요일별 총 사망자수")
for row in sorted_day_dead:
    print("%s: %d명" % (row[0], row[1]))

print("=" * 30)
print("발생건수 대비 사망자수가 가장 많은 시간대 best 5")
for i in range(5):
    print(sorted_dpd[i][0] + " : " + str(sorted_dpd[i][1]))
print("=" * 30)
