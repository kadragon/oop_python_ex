# https://www.data.go.kr/dataset/15018781/fileData.do

import csv
import operator
from sys import exit

try:
    file = open('seoul_seocho_20180630.csv', encoding='cp949')
except FileNotFoundError:
    print("File Open Error : 404")
    exit(0)
else:
    data = csv.reader(file)


# n번째로 금연구역이 많은 분류 입력받기

def input_number():
    try:
        n = int(input('나는 __번째로 금연구역이 많은 분류를 알고 싶습니다'))
    except ValueError:
        print("정수만 입력할 수 있습니다.")
        input_number()
    else:
        return n


n = input_number()

first_row = 0

area_dict = {}

total_area = 0

tot_fee = 0
allnumber = 0

# 한개씩 꺼내서 데이터 분석
for row in data:
    # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는 지 확인
    if first_row < 2:
        print(row)
        first_row += 1
        # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
        if first_row == 1:
            continue

    # 분류별 통계 내기
    if row[4] not in area_dict:
        area_dict.setdefault(row[4], 1)
    else:
        area_dict[row[4]] += 1

    # 총 금연구역 면적
    if row[6] != '':  # 비어있지 않으면
        total_area += int(row[6])

    # 과태료 평균
    if row[7] != '':
        allnumber += 1
        tot_fee += int(row[7])

print("=" * 30)

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_area = sorted(area_dict.items(), key=operator.itemgetter(0))  # name 기준
print("[분류별 금연구역 수]")
for row in sorted_area:
    print("%s: %d" % (row[0], row[1]))
print("=" * 30)

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_area = sorted(area_dict.items(), key=operator.itemgetter(1), reverse=True)  # value 기준
try:
    print("[%d번째로 금연구역이 많은 분류]" % (int(n)))
    row = sorted_area[n - 1]
except IndexError:
    print("[Index Error]")
else:
    print("%s: %d" % (row[0], row[1]))
print("=" * 30)

print("[흡연구역 총 면적(사업체 제외)]")
print("%d m^2" % (total_area))
print("=" * 30)

tot_avg = tot_fee / allnumber
print("[과태료 평균]")
print("%.2f 원" % (tot_avg))
print("=" * 30)
