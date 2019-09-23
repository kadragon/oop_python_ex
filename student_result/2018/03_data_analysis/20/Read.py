# https://www.data.go.kr/dataset/15021139/standard.do

import csv  # csv 파일 관련 수정
import operator  # 딕셔너리 정렬
from sys import exit  # 프로그램의 종료

# 파일이 있는지 없는지 확인하는 과정
try:
    f = open('Camping_Place.csv', encoding='cp949')
except FileNotFoundError:
    print("No File. Sorry")
    exit(0)
else:
    data = csv.reader(f)

# 첫 줄은 데이터의 범주 확인
first_row = 0

# 데이터 저장할 공간 만들기
category = {}
location = {}
safety = {}
how_many = {}
electric = {}

# 데이터 분석 (반복문, 한 줄씩)
for row in data:
    if first_row < 1:
        print(row)  # 첫 줄을 출력하자. 데이터가 들어간 형식 확인
        first_row += 1
        if first_row == 1:  # 첫 줄은 데이터가 아니므로 제외
            continue

    # 데이터를 만든다.
    # dict 선언을 확인하여 값 설정

    # 위치 통계
    temp_loc = row[5]
    temp_loc = temp_loc.split(' ')
    temp_loc = temp_loc[0]  # 주소를 지역명으로 바꾸기
    if temp_loc == '':
        temp_loc = '미분류'  # 공백에 대한 예외처리
    if temp_loc not in location:
        location.setdefault(temp_loc, 1)
    else:
        location[temp_loc] += 1

    # 분류별 통계
    if row[1] not in category:
        category.setdefault(row[1], 1)
    else:
        category[row[1]] += 1

    # 소화기 유무 통계
    fireX = row[13]
    if '소화기' in fireX:
        fireX = "소화기 비치됨"
    else:
        fireX = "소화기 비치 안됨"
    if fireX not in safety:
        safety.setdefault(fireX, 1)
    else:
        safety[fireX] += 1

    # 전기시설 유무
    electric_tmp = row[12]
    if '전기시설' in electric_tmp:
        electric_tmp = "전기시설 있음"
    else:
        electric_tmp = "전기시설 없음"
    if electric_tmp not in electric:
        electric.setdefault(electric_tmp, 1)
    else:
        electric[electric_tmp] += 1

    # 수용 인원 정리
    try:
        people = int(row[10])
    except ValueError:
        continue
    else:
        how_many.setdefault(row[0], people)

# Operator를 통해 Dict 타입을 정렬된 List로 변환한다.
sorted_class = sorted(category.items(), key=operator.itemgetter(0))  # index 기준
sorted_location = sorted(location.items(), key=operator.itemgetter(0))  # index 기준
sorted_safety = sorted(safety.items(), key=operator.itemgetter(1))  # value 기준
sorted_how_many = sorted(how_many.items(), key=operator.itemgetter(1))  # value 기준
sorted_electric = sorted(electric.items(), key=operator.itemgetter(0))  # index 기중

sorted_how_many = reversed(sorted_how_many)  # 내림차순 정렬로 바꾼다.
sorted_how_many = list(sorted_how_many)  # 리스트로 바꾼다.
sorted_how_many = sorted_how_many[0:5]  # 5개만 추린다.

# 결과를 프린트한다.
print("=" * 30)
print("야영장 분류별 개수")
for row in sorted_class:
    print("%s: %d" % (row[0], row[1]))

print("=" * 30)
print("지역별 야영장 개수")
for row in sorted_location:
    print(("%s: %d" % (row[0], row[1])))

print("=" * 30)
print("전기시설 유무")
for row in sorted_electric:
    print(("%s: %d" % (row[0], row[1])))

print("=" * 30)
print("소화기 구비 상태")
for row in sorted_safety:
    print(("%s: %d" % (row[0], row[1])))

print("=" * 30)
print("최다 수용인원 TOP 5")
for row in sorted_how_many:
    print(("%s: %d" % (row[0], row[1])))
print("=" * 30)
