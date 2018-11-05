import csv
import sys

# csv 파일 여부 확인
# 있으면 ace에 파일을 초기화
try:
    back_data = open('가구당_월평균_가계지출__전국_1인이상_실질__20181003221225.csv', encoding='cp949')
except FileNotFoundError:
    print("먼저 파일을 입력해주세요.")
    sys.exit(0)
else:
    ace = csv.reader(back_data)

# 총지출, 총소비, 최다 지출, 최소 지출의 값을 저장할 변수 선언
total_expend = 0
total_consume = 0

index = []
value = []

# 데이터를 딕 형태로 저장
consume = {}

# 최대, 최소값을 저장하기 위한 변수 선언
max = 0
min = 0

# 보고 싶은 정보 선택
i = input("choose what you want to open(1~3): ")
# 범위 외의 경우 재입력
while (i > '3' or i < '1'):
    i = input("Wrong input. Do it again: ")
# 변수를 임의로 변환 -> 표시 데이터가 csv파일의 1, 3, 5번 셀에 위치
k = 2 * int(i) - 1

for val in ace:
    # 총 지출, 총 소비와 index가 일치하면 그 값을 저장
    if val[0] == '가계지출 (원)':
        total_expend = val[1]
    if val[0] == '소비지출 (원)':
        total_consume = val[1]
    # 값이 실수로 변환가능한지 시도
    try:
        float(val[k])
    # 불가능한 경우는 가계지출항목별 밖에 없으므로 index에 저장
    except ValueError:
        index.append(val[k])
        continue
    else:
        # 실제 항목들은 0번 셀이 넘버링 되어있음
        # 0번째 셀의 첫번째가 넘버링 되어있는(정수인지) 셀만 읽기
        if val[0][0].isdigit():
            # 나중에 인덱스 저장을 위해 딕에 데이터 삽입
            consume[val[0]] = float(val[k])
            # max의 값이 초기값(0)이거나 비교하는 값이 더 크다면 교체
            # min의 값이 초기값(0)이거나 비교하는 값이 더 작다면 교체
            if max == 0 or max < float(val[k]):
                max = float(val[k])
            if min == 0 or min > float(val[k]):
                min = float(val[k])
# 저장된 max, min의 값을 바탕으로 딕에서 키를 찾아 value 리스트에 저장
for name, j in consume.items():
    if j == max:
        value.append(['MAX ' + name, max])
    if j == min:
        value.append(['MIN ' + name, min])
# 출력하는 가구의 종류
# 총 지출, 총 소비, 최다 지출, 최소 지출 출력
print(index[0])
print('Total Expend ' + total_expend)
print('Total Consume ' + total_consume)
for j in value:
    print("%s: %d" % (j[0], j[1]))
