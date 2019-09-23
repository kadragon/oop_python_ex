# https://www.data.go.kr/dataset/15013116/standard.do

import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

data = [[]]
# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    file = open('전국무료와이파이표준데이터.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없습니다.")
    exit(0)
else:
    data = csv.reader(file)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 설치시도명, 설치시설구분, 서비스제공사명이 있는 열의 번호(0부터 시작)
column_province, column_facility, column_company = -1, -1, -1
# 데이터를 분석해서 저장할 dictionary Type
province = {}
facility = {}
company = {}

# 한개씩 꺼내서 데이터 분석
for row in data:
    # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는 지 확인
    if first_row < 2:
        print(row)
        first_row += 1
        # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
        if first_row == 1:
            # 설치시도명, 설치시설구분, 서비스제공사명이 있는 열 찾기
            try:
                column_province = next(c for c in range(len(row)) if row[c] == '설치시도명')
            except StopIteration:
                pass
            try:
                column_facility = next(c for c in range(len(row)) if row[c] == '설치시설구분')
            except StopIteration:
                pass
            try:
                column_company = next(c for c in range(len(row)) if row[c] == '서비스제공사명')
            except StopIteration:
                pass
            continue

    # dict 가 선언되어 있는지 확인하여 값 설정
    # 설치시도 통계 내기
    if column_province != -1:
        if row[column_province] not in province:
            province.setdefault(row[column_province], 1)
        else:
            province[row[column_province]] += 1

    # 설치시설 통계 내기
    if column_facility != -1:
        if row[column_facility] not in facility:
            facility.setdefault(row[column_facility], 1)
        else:
            facility[row[column_facility]] += 1

    # 서비스제공사명 통계 내기
    if column_company != -1:
        if row[column_company] not in company:
            company.setdefault(row[column_company], 1)
        else:
            company[row[column_company]] += 1

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_province_1 = sorted(province.items(), key=operator.itemgetter(0))  # key 기준
sorted_province_2 = sorted(province.items(), key=operator.itemgetter(1), reverse=True)  # value 기준
sorted_facility = sorted(facility.items(), key=operator.itemgetter(1), reverse=True)  # value 기준
sorted_company = sorted(company.items(), key=operator.itemgetter(1), reverse=True)  # value 기준

print("=" * 40)
print("설치시도명")
print("=" * 40)
for row in sorted_province_1:
    print("%s: %d" % (row[0], row[1]))
print("=" * 40)
print()
print("=" * 40)
print("가장 많이 설치된 시도명")
print("%s: %d" % (sorted_province_2[0][0], sorted_province_2[0][1]))
print("가장 적게 설치된 시도명")
print("%s: %d" % (sorted_province_2[len(sorted_province_2) - 1][0], sorted_province_2[len(sorted_province_2) - 1][1]))
print("가장 많이 설치된 기관명")
print("%s: %d" % (sorted_facility[0][0], sorted_facility[0][1]))
print("가장 서비스를 많이 제공한 회사명")
print("%s: %d" % (sorted_company[0][0], sorted_company[0][1]))
print("=" * 40)
