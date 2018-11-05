import csv
from sys import exit


global data

try:  # 파일이 제대로 열리는지 확인
    f = open('./2017_car_accident_time_data.csv', encoding='cp949')
except FileNotFoundError:  # 파일을 찾을 수 없는 경우
    print("파일이 없습니다. 파일 이름을 다시 확인해주세요.")
    exit(0)
else:  # 파일이 제대로 열리는 경우
    print("파일 읽기에 성공했습니다.")
    data = csv.reader(f)

print("")
dict_1 = {}
temp = 'abcd'
first_row = 0
sum_1 = 0
print("데이터 형태")  # 파일 속 데이터의 형태 확인

for row in data:
    if first_row < 2:
        first_row += 1
        print(row)
        if first_row == 1:
            continue
print("")
# 포인터 위치 초기화
f.close()
f = open('2017_car_accident_time_data.csv', encoding='cp949')
data = csv.reader(f)
print("1. 도로형태에 따른 사고발생수")  # 시간대 별로 발생하는 사고를 총합하면 도로형태별 사고발생수를 얻을 수 있음
first_row = 0
for row in data:
    if first_row == 0:  # 첫번째 줄은 필요 없으므로 넘김
        first_row += 1
        continue
    else:
        if first_row == 1:  # 두번째 줄인 경우 temp에 데이터 이름 저장
            temp = row[0]
            first_row += 1
        if temp != row[0]:  # 데이터의 이름이 바뀌면 그 데이터의 총합을 dict_1에 저장
            dict_1.update({temp: sum_1})
            temp = row[0]
            sum_1 = int(row[2])
        else:  # 데이터의 이름이 같으면 같은 도로형태의 다른 시간대이므로 사고발생수를 합함
            sum_1 += int(row[2])
print(dict_1)  # 결과 출력
# 포인터 위치 초기화
print("")
f.close()
f = open('2017_car_accident_time_data.csv', encoding='cp949')
data = csv.reader(f)

print("2. 시간대별 사고 발생수")  # 다른 도로형태의 같은 시간대의 사고 발생수를 합하면 시간대별 사고 발생수를 얻을 수 있음
# 나누어진 시간대를 dict_2에 저장
dict_2 = {'00시-02시': 0, '02시-04시': 0, '04시-06시': 0, '06시-08시': 0, '08시-10시': 0, '10시-12시': 0, '12시-14시': 0,
          '14시-16시': 0, '16시-18시': 0, '18시-20시': 0, '20시-22시': 0, '22시-24시': 0}
for row in data:
    try:  # 첫줄인지 아닌지 확인
        dict_2[row[1]] += int(row[2])
    except KeyError:  # 첫줄인경우 넘김
        continue
print(dict_2)  # 결과 출력

# 포인터 위치 초기화
print("")
f.close()
f = open('2017_car_accident_time_data.csv', encoding='cp949')
data = csv.reader(f)

print("3. 사고로 인한 사망자수가 가장 많은 도로형태")  # 데이터의 사망자수를 합하여 비교하면 가장 사망자수가 많은 도로형태를 찾을 수 있음
first_row = 0
count = -1
rode_type = 'abcd'
for row in data:
    if first_row == 0:  # 첫번째 줄은 필요 없으므로 넘김
        first_row += 1
        continue
    else:
        if first_row == 1:  # 두번째 줄인 경우 temp에 데이터 이름 저장
            temp = row[0]
            first_row += 1
        if temp != row[0]:  # 데이터의 이름이 바뀌면 현재까지의 최대와 비교
            if sum_1 > count:
                count = sum_1
                rode_type = temp
            sum_1 = int(row[3])
            temp = row[0]
        else:  # 데이터의 이름이 같으면 같은 도로형태의 다른 시간대이므로 사망자수를 합함
            sum_1 += int(row[3])
print(rode_type, count, "명")  # 결과 출력

# 포인터 위치 초기화
print("")
f.close()
f = open('2017_car_accident_time_data.csv', encoding='cp949')
data = csv.reader(f)

print("4. 가장 사망자수가 많은 시간대")
#   시간대 저장
dict_4 = {'00시-02시': 0, '02시-04시': 0, '04시-06시': 0, '06시-08시': 0, '08시-10시': 0, '10시-12시': 0, '12시-14시': 0,
          '14시-16시': 0, '16시-18시': 0, '18시-20시': 0, '20시-22시': 0, '22시-24시': 0}
for row in data:  # 각 시간대별 사망자수 체크
    try:  # 첫줄인지 아닌지 확인
        dict_4[row[1]] += int(row[3])
    except KeyError:  # 첫줄인경우 넘김
        continue
max = -1
max_time = 'abcd'
for i in dict_4:  # 가장 사망자 수가 많은 시간 탐색
    if max < dict_4[i]:
        max = dict_4[i]
        max_time = i
print(max_time, max, "명")  # 결과 출력
