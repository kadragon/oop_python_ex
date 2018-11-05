'''
Date 2018.10.05
By Ho Young Choi
* 공공데이터포털이 아니라 국가통계포털에서 데이터를 찾았습니다
'''
import csv
from sys import exit


def design(s):
    print('=============')
    print(s)
    print('=============')


# 사용하는 데이터는 통계청 국가통계포털의 체육시설수 데이터 중 야구장과 축구장
try:
    file = open('체육시설수_20181005201839.csv', encoding='cp949')
except FileNotFoundError:  # 파일이 없다면 404 Not Found를 출력하고 프로그램 종료
    print('404 Not Found')
    exit(0)
else:
    data = csv.reader(file)
row = 0
sido_baseball = {}
sido_soccer = {}
sido = {}
sido_name = []
index_soccer = ' '
index_baseball = ' '
tmp = ' '
max_soccer = -99999
max_baseball = -99999
for line in data:
    row += 1
    if row < 4:  # 맨 처음 3줄은 의미 없는 줄이므로 패스
        if row == 3:  # 이 줄은 데이터의 내용을 알려주므로 패스
            print(line)
        continue
    # 소계는 중복되는 데이터이므로 패스
    if line[1] == '소계':
        continue
    # 다뤄야 할 데이터는 index상 2와 3 위치이므로 각각을 정수형으로 전환
    for i in range(2, 4):
        if line[i] == '-':
            line[i] = 0
        else:
            line[i] = int(line[i])
    if line[0] not in sido_name:  # 원래 있던 시도가 아닌 경우 새 데이터 추가
        sido_baseball[line[0]] = line[3]
        sido_soccer[line[0]] = line[2]
        sido[line[0]] = 1
        sido_name.append(line[0])
    else:  # 원래 있던 시도인 경우 본래 데이터 업데이트
        sido_baseball[line[0]] += line[3]
        sido_soccer[line[0]] += line[2]
        sido[line[0]] += 1
    if line[0] == "경기도":  # 경기도에서의 최댓값 찾기_이 때 경기도를 다른 지역으로 바꾸면 다른 지역의 최댓값 찾기 가능
        if line[2] > max_soccer:  # 전체 탐색으로 축구장 개수의 최댓값 찾기
            index_soccer = line[1]
            max_soccer = line[2]
        if line[3] > max_baseball:  # 전체 탐색으로 야구장 개수의 최댓값 찾기
            index_baseball = line[1]
            max_baseball = line[3]

design("각 시도 별 축구장 개수")
num_soccer = num_baseball = 0.0
for name in sido_name:
    print("%s : %d개" % (name, sido_soccer[name]))
design("각 시도 별 야구장 개수")
for name in sido_name:
    print("%s : %d개" % (name, sido_baseball[name]))
design("각 시도 별 축구장 개수의 평균")  # 평균은 소수점 두 자리 수까지 출력하자
for name in sido_name:
    try:
        num_soccer = sido_soccer[name] / sido[name]
    except ZeroDivisionError:
        print("400 Bad Request")  # 0으로 나눈다면 400 Bad Request를 출력하고 프로그램 종료
        exit(0)
    print("%s : %.2f개" % (name, num_soccer))  # 소수점 두 자리 수까지 출력
design("각 시도 별 야구장 개수의 평균")
for name in sido_name:
    try:
        num_baseball = sido_baseball[name] / sido[name]
    except ZeroDivisionError:
        print("400 Bad Request")
        exit(0)
    print("%s : %.2f개" % (name, num_baseball))
design("경기도에서 축구장이 가장 많은 지역")
print("%s : %d" % (index_soccer, max_soccer))
design("경기도에서 야구장이 가장 많은 지역")
print("%s : %d" % (index_baseball, max_baseball))
