# 공공데이터 포털의 전국지진해일대피소표준데이터 이용 (https://www.data.go.kr/dataset/15025449/standard.do)

import csv
from sys import exit

try:  # 파일 존재하는지 판별하기 위함
    f = open('shelter.csv', encoding='cp949')
except FileNotFoundError:  # 파일 존재하지 않는다면
    print("파일이 존재하지 않습니다.")  # "파일이 존재하지 않습니다." 를 출력
    exit(0)  # 프로그램 종료
else:
    data = csv.reader(f)  # 파일이 존재한다면 data에 csv 데이터 저장

first_row = 0  # 첫번째 줄을 건너뛰기 위해 선언한 변수

whole_area = 0  # 전국 지진해일대피소 면적을 저장하는 변수
whole_people = 0  # 전국 지진해일대피소 수용인원을 저장하는 변수
max_area = 0  # 행정구역 중 가장 많은 지진해일대피소 면적을 저장하는 변수
max_area_index = 0  # 행정구역 중 지진해일대피소의 면적이 가장 많은 곳을 저장하는 변수
max_people = 0  # 행정구역 중 가장 많은 지진해일대피소 수용인원을 저장하는 변수
max_people_index = 0  # 행정구역 중 지진해일대피소 수용인원이 가장 많은 곳을 저장하는 변수
area_dic = {}  # 각 행정구역의 지진해일대피소 면적을 저장하기 위한 딕셔너리 변수
people_dic = {}  # 각 행정구역의 지진해일대피소 수용인원을 저장하기 위한 딕셔너리 변수
a = ["경기도", "인천광역시", "서울특별시", "강원도", "충청남도", "세종특별자치시", "대전광역시", "충청북도", "경상북도", "전라북도", "경상남도", "대구광역시", "울산광역시",
     "부산광역시", "광주광역시", "전라남도"]  # 행정구역의 이름을 저장하는 리스트
b = ['gy', 'in', 'se', 'ga', 'cn', 'sejong', 'de', 'cb', 'gb', 'jb', 'gn', 'dg', 'ul', 'bu', 'gj',
     'jn']  # 행정구역의 약자를 저장하는 리스트

area_dic = {'gy': 0, 'in': 0, 'se': 0, 'ga': 0, 'cn': 0, 'sejong': 0, 'de': 0, 'cb': 0, 'gb': 0, 'jb': 0, 'gn': 0,
            'dg': 0, 'ul': 0, 'bu': 0, 'gj': 0, 'jn': 0}  # 딕셔너리 변수 초기화
people_dic = {'gy': 0, 'in': 0, 'se': 0, 'ga': 0, 'cn': 0, 'sejong': 0, 'de': 0, 'cb': 0, 'gb': 0, 'jb': 0, 'gn': 0,
              'dg': 0, 'ul': 0, 'bu': 0, 'gj': 0, 'jn': 0}  # 딕셔너리 변수 초기화

for row in data:  # data를 한 줄씩 row에 저장
    if first_row == 0:  # 만약 첫번째 줄이라면
        first_row += 1  # first_row에 +1하고
        continue  # 두번째 줄부터 반복문 시작
    try:  # 데이터 중간중간 비어있는 곳을 건너뛰기 위해서
        whole_area += float(row[8])  # whole_area에 각 지진해일대피소 면적 더해줌
    except ValueError:  # 만약 데이터 비어있다면
        pass  # 건너뜀
    try:  # 데이터 중간중간 비어있는 곳을 건너뛰기 위해서
        whole_people += int(row[9])  # whole_people에 각 지진해일대피소 수용인원 더해줌
    except ValueError:  # 만약 데이터 비어있다면
        pass  # 건너뜀

    lc1 = row[4][0:3]  # 지진해일대피소의 위치 저장
    lc2 = row[5][0:3]  # 지진해일대피소의 위치 저장
    for i in range(0, 16):  # 어느 행정구역 속하는지 판별
        if lc1 == a[i][0:3] or lc2 == a[i][0:3]:  # 지진해일대피소가 있는 행정구역을 찾았다면
            try:  # 데이터 중간중간 비어있는 곳을 건너뛰기 위해서
                area_dic[b[i]] += float(row[8])  # 행정구역별 지진해일대피소 면적에 더해줌
                people_dic[b[i]] += int(row[9])  # 행정구역별 지진해일대피소 수용인원에 더해줌
            except ValueError:  # 데이터 비어있다면
                pass  # 건너뜀

for i in range(0, 16):  # 지진해일대피소 면적과 수용인원이 가장 많은 곳을 찾귀 위해
    if max_area < area_dic[b[i]]:  # 더 큰 값 찾았다면
        max_area = area_dic[b[i]]  # max_area 값 변경
        max_area_index = i  # index도 변경
    if max_people < people_dic[b[i]]:  # 더 큰 값 찾았다면
        max_people = people_dic[b[i]]  # max_people 값 변경
        max_people_index = i  # index도 변경

print("=============================================\n")  # 결과값 출력 시작 표시
print("우리나라 전체 지진해일대피소 면적은 %d m^2입니다." % whole_area)  # 전체 지진해일대피소 면적 출력
print("우리나라 전체 지진해일대피소 수용인원은 %d 명입니다." % whole_people)  # 전체 지진해일대피소 수용인원 출력
print("지진해일대피소의 면적이 가장 큰 행정구역은 %s입니다." % a[max_area_index])  # 지진해일대피소 면적이 가장 큰 행정구역 출력
print("지진해일대피소의 수용인원이 가장 큰 행정구역은 %s입니다." % a[max_people_index])  # 지진해일대피소 수용인원이 가장 큰 행정구역 출력
print("")
