import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('wifi.csv', encoding='cp949')
except FileNotFoundError:
    print("No file found")
    exit(0)
else:
    data = csv.reader(f)

# 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
first_row = 0

# 데이터를 분석해서 저장할 dictionary Type
city_dict = {}
com_dict = {}
ssid_dict = {}
year_dict = {}

try:
    for row in data:
        # dict 가 선언되어 있는지 확인하여 값 설정
        # 설치시도명 통계 내기
        if row[2] not in city_dict:
            city_dict.setdefault(row[2], 1)
        else:
            city_dict[row[2]] += 1

        # 서비스제공사명 통계 내기
        if row[5] not in com_dict:
            com_dict.setdefault(row[5], 1)
        else:
            com_dict[row[5]] += 1

        # SSID 통계 내기
        if row[6] not in ssid_dict:
            ssid_dict.setdefault(row[6], 1)
        else:
            ssid_dict[row[6]] += 1

        # SSID 통계 내기
        year = (row[7])[0:4]
        if year not in year_dict:
            year_dict.setdefault(year, 1)
        else:
            year_dict[year] += 1

except:
    print("Error while reading files")


# 상위 5개의 데이터를 형식에 맞춰 출력


def print_formatted(txt, sorted_arr):
    print(txt)
    cnt = 0
    end = 5
    for row in reversed(sorted_arr):
        if row[0] == '':
            cnt += 1
            end += 1
            continue  # 데이터가 NULL이면 제거
        print("%s: %d" % (row[0], row[1]))
        cnt += 1
        if cnt == end:
            break
    print("=" * 30)


# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sorted_city = sorted(city_dict.items(), key=operator.itemgetter(1))
sorted_com = sorted(com_dict.items(), key=operator.itemgetter(1))
sorted_ssid = sorted(ssid_dict.items(), key=operator.itemgetter(1))
sorted_year = sorted(year_dict.items(), key=operator.itemgetter(1))

type_list = [sorted_city, sorted_com, sorted_ssid, sorted_year]
txt_list = ["City analysis", "Company analysis",
            "SSID analysis", "Year analysis"]

for i in range(len(type_list)):
    print_formatted(txt_list[i], type_list[i])
