# https://www.data.go.kr/dataset/15013109/standard.do

import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('library.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 데이터를 분석해서 저장할 dictionary Type
region_count = {}
regions_count = {}

ind = 0
longest_rent, most_rent = 0, 0

for row in data:
    ind += 1
    if ind == 1:
        continue

    region, region_detail = row[1], row[2]
    if region not in region_count:
        region_count[region] = 0
        regions_count[region] = {}
    if region_detail not in regions_count[region]:
        regions_count[region][region_detail] = 0

    region_count[region] += 1
    regions_count[region][region_detail] += 1

    longest_rent = max(longest_rent, int(row[16]))
    most_rent = max(most_rent, int(row[15]))

for key in region_count.keys():
    print('%s: %d개' % (key, region_count[key]))

print('================================')

for key in regions_count.keys():
    sorted_regions = sorted(regions_count[key].items(), key=operator.itemgetter(1))
    print('%s에서 도서관이 가장 많은 지역: %s (%d개)' % (key, sorted_regions[-1][0], sorted_regions[-1][1]))

print('================================')
print('가장 많은 대출 권수: %d권' % (most_rent))
print('가장 긴 대출기간: %d일' % (longest_rent))
