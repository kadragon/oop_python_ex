import csv
from sys import exit

try:  # 파일 열기 - FileNotFoundError를 대비해 try-except 구문을 이용
    f = open('wifi_data.csv', encoding='cp949')
except FileNotFoundError:
    print('No such file exists!')
    exit(0)
else:
    data = csv.reader(f)

sd_dict = {}  # 각 시도 별 설치된 와이파이의 개수를 저장하기 위한 dictionary
sd_top = ['', 0]  # 가장 많은 와이파이가 설치된 시도와 그 개수를 저장하기 위한 listx
sgg_dict = {}  # 각 시군구 별 설치된 와이파이의 개수를 저장하기 위한 dictionary
sgg_top = ['', 0]  # 가장 많은 와이파이가 설치된 시군구와 그 개수를 저장하기 위한 list
type_dict = {}  # 시설의 종류 별 설치된 와이파이의 개수를 저장하기 위한 dictionary
type_top = ['', 0]  # 가장 많은 와이파이가 설치된 시설의 종류와 그 개수를 저장하기 위한 list
date_list = [[0 for i in range(12)] for j in range(19)]  # 가장 많은 와이파이가 설치된 기간을 알아보기 위한 list
date_top = [0, 0, 0]  # 가장 많은 와이파이가 설치된 연, 월과 그 개수를 저장하기 위한 list
lat = 0  # 위도의 합을 저장할 변수
lon = 0  # 경도의 합을 저장할 변수
cnt = 0  # 데이터의 개수를 저장할 변수
flag = True

for row in data:
    if flag:  # 첫 번째 줄은 건너뛴다
        flag = False
        continue

    try:  # 시도 데이터 수집
        sd_dict[row[2]] += 1
    except KeyError:  # 아직 없는 키일 경우 새로 만듦
        sd_dict[row[2]] = 1

    try:  # 시군구 데이터 수집
        sgg_dict[row[3]] += 1
    except KeyError:  # 아직 없는 키일 경우 새로 만듦
        sgg_dict[row[3]] = 1

    try:  # 시설 종류 별 데이터 수집
        type_dict[row[4]] += 1
    except KeyError:  # 아직 없는 키일 경우 새로 만듦
        type_dict[row[4]] = 1

    lat += float(row[12])
    lon += float(row[13])
    cnt += 1

    date = row[7].split('-')  # 기간 데이터 수집: 연-월 / 연.월 / 연_월 데이터를 연과 월로 분리
    if len(date) is not 2:
        date = str(date[0]).split('.')
    if len(date) is not 2:
        date = str(date[0]).split('_')

    if len(date) is 2:  # 연과 월로 올바르게 분리된 데이터일 경우
        try:
            date_list[int(date[0]) - 2000][int(date[1]) - 1] += 1
        except ValueError:
            continue
        except IndexError:  # 연: 2000~2018 / 월: 1~12가 아니면 IndexError
            continue

f.close()  # 파일 닫기

for sd in sd_dict:  # 시도 데이터 최댓값 추출
    if sd_dict[sd] > sd_top[1]:
        sd_top = [sd, sd_dict[sd]]

for sgg in sgg_dict:  # 시군구 데이터 최댓값 추출
    if sgg_dict[sgg] > sgg_top[1]:
        sgg_top = [sgg, sgg_dict[sgg]]

for my_type in type_dict:  # 시설 종류 별 데이터 최댓값 추출
    if type_dict[my_type] > type_top[1]:
        type_top = [my_type, type_dict[my_type]]

for i in range(19):  # 기간 데이터 최댓값 추출
    for j in range(12):
        if date_list[i][j] > date_top[2]:
            date_top = [i, j, date_list[i][j]]

print('가장 많은 무료와이파이가 있는 시도는 %d개의 와이파이가 있는 %s입니다!' % (sd_top[1], sd_top[0]))
print('가장 많은 무료와이파이가 있는 시군구는 %d개의 와이파이가 있는 %s입니다!' % (sgg_top[1], sgg_top[0]))
print('가장 많은 무료와이파이가 있는 시설은 %d개의 와이파이가 있는 %s입니다!' % (type_top[1], type_top[0]))
print('가장 많은 무료와이파이가 설치된 기간은 %d개의 와이파이가 설치된 %d년 %d월입니다!' % (date_top[2], date_top[0] + 2000, date_top[1] + 1))
print('모든 무료와이파이의 평균 위치는 위도 %f, 경도 %f입니다!' % (lat / cnt, lon / cnt
                                              ))
