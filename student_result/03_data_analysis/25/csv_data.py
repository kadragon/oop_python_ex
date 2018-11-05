"""
Project    과제2:공공데이터분석
Author     지명금
Date       2018.09.25
"""
# 서울교통공사_승강총괄현황
# https://www.data.go.kr/dataset/15024831/fileData.do

import csv  # csv 파일 처리를 위해
from sys import exit  # 프로그램을 종료시키기 위해

# try~except문의 활용(1) :: file을 열기 위해 시도해보고, 없으면 알려주고 있으면 data로 저장
try:
    f = open("서울교통공사_승강총괄현황_20171030.csv", encoding='cp949')
except FileNotFoundError:
    print(">> 해당되는 파일이 존재하지 않습니다")
    exit(0)
else:
    data = csv.reader(f)

# 데이터의 열 개수를 세는 변수
row_cnt = 0

# 데이터에서 승강기의 이름을 저장하는 list type 변수
lift_name = {}

# data를 list type으로 변환하여 저장하기 위한 list type
origin_data = []

# 데이터를 분석해서 저장할 list type
# line_list :: 각 호선별 승강기 통계를 저장할 이중 list
# line_list[i] :: [0] 호선 번호 | [1] 엘리베이터 | [2] 에스컬레이터 | [3] 무빙워크 | [4] 휠체어리프트
# ex) line_list[3][1] = 3호선의 엘리베이터 개수 
line_list = [[0 for j in range(5)] for i in range(9)]

# lift_total :: 전체 승강기의 개수를 저장할 list (index는 lift_name 순서대로)
# lift_total :: [0]  엘리베이터 | [1] 에스컬레이터 | [2] 무빙워크 | [3] 휠체어리프트
lift_total = [0 for i in range(4)]

# no_lift :: 각 역의 승강기 종류 통계를 저장할 list
# ex) no_lift[1] = 승강기 종류가 1가지인 역의 개수
no_lift = [0 for i in range(5)]

# lift_total[i][0]의 호선 번호를 미리 채워두기 위한 for 문
for i in range(1, 9):  # data에는 1 ~ 8호선까지 호선번호가 존재함
    line_list[i][0] = i

# data에서 한 열씩 꺼내서 데이터를 분석함
for row in data:
    if row_cnt == 0:  # 첫 번째 열에는 행의 속성을 저장해두고 있으므로 분석에 예외처리
        lift_name = row[2:]
        row_cnt += 1
        continue  # 데이터 분석에 활용하지 않음(두 번째 열부터 활용함)

    origin_data.append(row)  # data를 list type으로 저장해두기 위해 row 한 줄씩 origin_data에 추가

    # try~except문의 활용(2) :: 호선번호의 길이를 확인하여 1이상인 경우 0번째 요소만 slice하여 활용하고, 아니면 그대로 이용
    # 7호선의 경우 '7'과 '7(연)'으로 표기된 경우가 있어서 아래와 같은 처리 과정이 필요함
    try:
        line = int(row[0])  # 현재 row의 역의 호선번호를 저장하는 변수 line
    except ValueError:
        line = int(row[0][0])

    # no_lift list를 위해서 역별로 승강기의 종류를 세는 변수
    lift_num = 0
    for index in range(1, 5):
        if row[index + 1] != '0':  # 해당하는 종류의 승강기가 존재한다면 lift_num += 1
            lift_num += 1
        line_list[line][index] += int(row[index + 1])
        lift_total[index - 1] += int(row[index + 1])

    # no_lift[lift_num] = lift_num가지 승강기를 가지는 역의 개수를 세는 것
    no_lift[lift_num] += 1

# line_list 리스트를 정렬하여 저장하기 위한 list type (호선별)
sorted_line = []
for i in range(1, 5):
    # line_list를 lift[i](각 승강기 종류별로) 오름차순 정렬하여 sorted_list에 추가해둠
    # ex) sorted_list[0] = lift[1]를 기준으로 오름차순 정렬한 line_list 리스트
    sorted_line.append(sorted(line_list, key=lambda lift: int(lift[i])))

# 자료분석[1]
print("=" * 55)
print(" [1] 승강기 종류별로 많이 배치된 호선")
print(" 엘리베이터 | 에스컬레이터 | 무빙워크 | 휠체어리프트")
print("=" * 55)
for i in range(1, 9):
    print("#%d:   %d호선 |        %d호선 |    %d호선 |        %d호선" % (
    i, sorted_line[0][-i][0], sorted_line[1][-i][0], sorted_line[2][-i][0], sorted_line[3][-i][0]))

# 자료분석[2]
# origin_data 리스트를 정렬하여 저장하기 위한 list type (역별)
sorted_station = []
for i in range(2, 6):
    # origin_data를 lift[i](각 승강기 종류별로) 오름차순 정렬하여 sorted_station에 추가해둠
    # ex) sorted_station[0] = lift[2]를 기준으로 오름차순 정렬한 origin_data 리스트 
    sorted_station.append(sorted(origin_data, key=lambda lift: int(lift[i])))

for num in range(1, 5):
    print("=" * 55)
    print(" [2] 승강기 종류별 지하철 역 통계 -(%d) %s" % (num, lift_name[num - 1]))
    print("=" * 55)
    for i in range(1, 6):  # 상위 5개만 출력
        print("#%d:\t%s호선::%s(%s개)" % (
        i, sorted_station[num - 1][-i][0], sorted_station[num - 1][-i][1], sorted_station[num - 1][-i][num + 1]))

# 자료분석[3]
print("=" * 55)
print(" [3] 승강기 종류별 통계")
print(" 엘리베이터 | 에스컬레이터 | 무빙워크 | 휠체어리프트")
print("=" * 55)
print("      %d개 |       %d개 |     %d개 |       %d개" % tuple(lift_total))  # list type인 lift_total을 tuple로 변환함

# 자료분석[4]
# 전체 역의 개수를 세는 변수 
total_station = 0
print("=" * 55)
print(" [4] 역별 승강기 종류 통계")
print("=" * 55)
for i in range(5):
    print("승강기 %d종류:\t%3d개의 역" % (i, no_lift[i]))
    total_station += no_lift[i]
print("-" * 55)
print("전체 역의 개수:\t%3d개의 역" % (total_station))
print("-" * 55)
