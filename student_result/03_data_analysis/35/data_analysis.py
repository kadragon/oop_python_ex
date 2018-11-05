import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('2017_jeju_food.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 데이터를 분석해서 저장할 dictionary Type
area_dict = {}
size = {}

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
    # 업태별 통계 내기
    if row[2] not in area_dict:
        area_dict.setdefault(row[2], 1)
    else:
        area_dict[row[2]] += 1

    # 사업장 면적 통계 내기
    if row[2] not in size:
        size.setdefault(row[2], float(row[1]))
    else:
        size[row[2]] += float(row[1])

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_area = sorted(area_dict.items(), key=operator.itemgetter(1))  # value 기준
sorted_size = sorted(size.items(), key=operator.itemgetter(1))  # value 기준

print("=" * 30)
print("제주시 업태별 지점수[정렬]")
for row in sorted_area:
    print("%s: %d개" % (row[0], row[1]))
print("=" * 30)
print("제주시 업태별 사업장 면적[정렬]")
for row in sorted_size:
    print("%s: %d(m^2)" % (row[0], row[1]))

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('2017_daejeon_food.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 데이터를 분석해서 저장할 dictionary Type
area_dict = {}
size = {}

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
    # 업태별 통계 내기
    if row[2] not in area_dict:
        area_dict.setdefault(row[2], 1)
    else:
        area_dict[row[2]] += 1

    # 사업장 면적 통계 내기
    if row[2] not in size:
        size.setdefault(row[2], float(row[1]))
    else:
        size[row[2]] += float(row[1])  # 면적 합산

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_area = sorted(area_dict.items(), key=operator.itemgetter(1))  # value 기준
sorted_size = sorted(size.items(), key=operator.itemgetter(1))  # value 기준

print("=" * 30)
print("대전시 업태별 지점수[정렬]")
for row in sorted_area:
    print("%s: %d개" % (row[0], row[1]))
print("=" * 30)
print("대전시 업태별 사업장 면적[정렬]")
for row in sorted_size:
    print("%s: %d(m^2)" % (row[0], row[1]))
print("=" * 30)
