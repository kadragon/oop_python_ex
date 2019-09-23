import csv  # csv import
import operator  # dict 정렬
from sys import exit  # 프로그램 종료

# data 열기

try:
    f = open('전국무료와이파이표준데이터.csv', encoding='cp949')
except FileNotFoundError:
    print("No File T_T")
    exit(0)
else:
    data = csv.reader(f)

comp_dict = {}  # 서비스 제공사
place_dict = {}  # 시설군
city_dict = {}  # 시도
siz = 0  # 서비스 제공사 dict의 사이즈
psiz = 0  # 시설군 dict의 사이즈
csiz = 0  # 시도 dict의 사이즈

for row in data:
    if row[5] == "서비스제공사명": continue  # 첫 번째 line에는 이름이 기술되어 있으므로 pass
    if row[5] not in comp_dict:  # dict 생성
        siz += 1
        comp_dict.setdefault(row[5], 1)
    else:
        comp_dict[row[5]] += 1  # 이미 있는 경우 값 +1

    if row[4] not in place_dict:  # dict 생성
        psiz += 1
        place_dict.setdefault(row[4], 1)
    else:
        place_dict[row[4]] += 1  # 이미 있는 경우 값 +1

    if row[2] not in city_dict:  # dict 생성
        csiz += 1
        city_dict.setdefault(row[2], 1)
    else:
        city_dict[row[2]] += 1  # 이미 있는 경우 값+1

# 값에 따라 정렬
sorted_comp = sorted(comp_dict.items(), key=operator.itemgetter(1))
sorted_place = sorted(place_dict.items(), key=operator.itemgetter(1))
sorted_city = sorted(city_dict.items(), key=operator.itemgetter(1))

print("가장 많은 무료 와이파이를 설치한 업체:", sorted_comp[siz - 1][0], ',', sorted_comp[siz - 1][1], "개")  # dict의 마지막 위치에 존재
print("가장 많은 무료 와이파이가 설치된 시설군:", sorted_place[psiz - 1][0], ',', sorted_place[psiz - 1][1], "개")  # dict의 마지막 위치에 존재
f.close()  # 파일 닫기

# 파일 다시 열기
try:
    f = open('전국무료와이파이표준데이터.csv', encoding='cp949')
except FileNotFoundError:
    print("No File T_T")
    exit(0)
else:
    data = csv.reader(f)

# 값 비교를 통해 위도가 가장 높은 지역을 찾는다.

maxlong = 0
maxplace = ' '
for row2 in data:
    try:
        if float(row2[12]) < 90 and maxlong < float(row2[12]):  # 위도 없는 경우 99.999999로 되어 있어서 제외
            maxplace = row2[0]
            maxlong = float(row2[12])
    except ValueError:  # 숫자가 아닌 것을 float로 변환하려 할 경우 ValueError가 나타남
        continue
print("가장 높은 위도에 설치된 와이파이: ", maxplace, ',', maxlong)  # 출력

print("시도별 무료 와이파이 개수 랭킹(개)")  # 랭킹은 길기 때문에 가장 마지막에 출력
cnt = 17
while cnt > 0:
    print(18 - cnt, ":", sorted_city[cnt - 1][0], ',', sorted_city[cnt - 1][1])
    cnt -= 1
