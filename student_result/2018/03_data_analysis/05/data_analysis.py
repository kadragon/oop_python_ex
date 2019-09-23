# 필요한 모듈 import
import csv
import operator
from sys import exit

# 파일 open 시도
try:
    f = open('stats.csv', encoding='cp949')
except FileNotFoundError as e:  # 만약 파일이 없다면
    print(e)  # 에러를 출력하고 종료
    exit()

read = csv.reader(f)
# 산업단지	입주(개사)	가동(개사)	생산실적(억원)	수출실적(백만달러)	고용(명)	남(명)	여(명)


# 전체 자료 수, 최대 수출, 입주 기업 수, 입주기업대비 생산실적, 직원 수/성비
count = 0
maxExportDict = {'maxNum': 0, 'maxFactory': None}
factoryNum = {}
companyNum2Result = {'maxRatio': 0, 'maxFactory': None}
employeeRatio = {'employee': 0, 'man': 0, 'woman': 0}

# 데이터 변환 후 담을 리스트
data = []

# 데이터를 탐색하면서 순수 숫자로 이루어진 문자열이 있으면 int로 변환
for row in read:
    if row[0] == '':
        continue
    # print(row)
    for i in range(len(row)):

        # print(a)
        if row[i].isdigit():  # 만약 문자열 안이 int로 변환 가능하다면
            # print(a)
            row[i] = int(row[i])  # 변환
        # print(a)
    # print(row)
    data.append(row)  # 바꾼 데이터 append

# 데이터를 처음부터 탐색
for row in data:
    if count == 0:  # 첫 행은 기준이기 때문에 고려하지 않음
        count += 1
        continue
    if row[0] == '':  # 데이터가 없는 열 삭제
        continue

    if row[0] not in factoryNum:  # 입주기업수 딕셔너리에 현재 산업단지가 없다면
        factoryNum.setdefault(row[0], row[1])  # 현재 산업단지의 입주기업수를 딕셔너리에 추가함
    else:  # 아니면
        factoryNum[row[0]] += row[1]  # 입주기업수를 딕셔너리 인덱스에 더해줌

    # 현재 산업단지의 수출규모가 최대 수출규모보다 클 경우
    try:
        if row[4] > maxExportDict['maxNum']:
            maxExportDict['maxNum'] = row[4]  # 정보 수정
            maxExportDict['maxFactory'] = row[0]
    except TypeError:  # 오류가 날 경우 continue
        continue

    # 전체 직원 수, 여직원 수, 남직원 수 업데이트
    employeeRatio['employee'] += row[5]
    employeeRatio['man'] += row[6]
    employeeRatio['woman'] += row[7]

    # 현재 산업단지의 입주기업 대비 생산실적 계산
    try:
        ratio = row[3] / row[1]
    except (TypeError, ZeroDivisionError):  # 오류가 날 경우 continue
        continue
    else:  # 만약 현재 비율이 최대라면 값 업데이트
        if ratio > companyNum2Result['maxRatio']:
            companyNum2Result['maxRatio'] = ratio
            companyNum2Result['maxCompany'] = row[0]

    count += 1

# factorylist 정렬
factoryList = sorted(factoryNum.items(),
                     key=lambda x: x[1], reverse=True)

# print(factoryList)

# 결과 출력
print('가장 수출을 많이 한 산업단지는 %d 백만달러를 수출한 %s 이다.' %
      (maxExportDict['maxNum'], maxExportDict['maxFactory']))
print()
print('입주 기업 대비 생산 실적이 가장 높은 산업단지는 비율 %f 인 %s이다.' %
      (companyNum2Result['maxRatio'], companyNum2Result['maxCompany']))
print()
print('전체 고용 인원수는 %d명이며, 남성은 %d%%, 여성은 %d%%이다.' % (
    employeeRatio['employee'],
    int(employeeRatio['man'] / employeeRatio['employee'] * 100),
    int(employeeRatio['woman'] / employeeRatio['employee'] * 100)))
print()
print('입주기업 수 TOP 5')
print('=================')
for i in range(5):
    print('%s: %d개' % (factoryList[i][0], factoryList[i][1]))
