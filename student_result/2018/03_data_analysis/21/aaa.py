import csv
import operator
from sys import exit

# Read from CSV file
try:
    f = open('국제선_항공기스케줄.csv', encoding='cp949')
except FileNotFoundError:
    print("File not Found")
    exit(0)
else:
    data = csv.reader(f)

row_idx = 0

airport_usage = {}
plane_type = {}
airport_destination = {}
airport_from = {}
departure_time = {}

for row in data:
    row_idx += 1

    # 데이터 색인은 분석에 사용하지 않음
    # 제대로 된 데이터가 아니면 Except
    # row[4]는 비행계획시간이 int 형으로 저장
    try:
        int(row[4])
    except (ValueError, IndexError) as e:
        continue  # 데이터 색인일 때 건너뛰기

    # row = 분석할 데이터 행

    # 공항 이용횟수 통계
    # row[0] 은 출발 공항을 저장
    if row[0] not in airport_usage:
        airport_usage.setdefault(row[0], 1)
    else:
        airport_usage[row[0]] += 1

    # 비행기 기종 통계
    # row[6] 은 기종을 저장
    if row[6] not in plane_type:
        plane_type.setdefault(row[6], 1)
    else:
        plane_type[row[6]] += 1

    # 도착 공항 통계 (어느 공항으로 가장 많이 가는지)
    # row[1] 은 상대 공항, row[2]는 출도착 정보를 D(Departure), A(Arrival)로 저장
    if row[2] == 'D':  # *출도착 정보가 D,즉 출발인 경우에만 상대 공항에 도착 한 것이다
        if row[1] not in airport_destination:
            airport_destination.setdefault(row[1], 1)
        else:
            airport_destination[row[1]] += 1

    # 출발 공항 통계 (어느 공항에서 가장 많이 오는지)
    # row[1] 은 상대 공항, row[2]는 출도착 정보를 D(Departure), A(Arrival)로 저장
    if row[2] == 'A':  # *출도착 정보가 D,즉 출발인 경우에만 상대 공항에 도착 한 것이다
        if row[1] not in airport_from:
            airport_from.setdefault(row[1], 1)
        else:
            airport_from[row[1]] += 1

    # 출발시간대 통계
    # row[4]에 계획시간이 4자리 또는 3자리 숫자로 저장
    if int(int(row[4]) / 100) not in departure_time:  # int(row[4]/100)를 통해 시간(시) 별로 count
        departure_time.setdefault(int(int(row[4]) / 100), 1)
    else:
        departure_time[int(int(row[4]) / 100)] += 1

# sort
airport_usage = sorted(airport_usage.items(), key=operator.itemgetter(1))
plane_type = sorted(plane_type.items(), key=operator.itemgetter(1))
airport_destination = sorted(airport_destination.items(), key=operator.itemgetter(1))
airport_from = sorted(airport_from.items(), key=operator.itemgetter(1))
departure_time = sorted(departure_time.items(), key=operator.itemgetter(1))

# print
print("-" * 30)
print("이용률 상위 5개 공항")
for i in range(1, 6):
    print("%s: %s" % (airport_usage[-i][0], airport_usage[-i][1]))

print("-" * 30)
print("상위 5개 기종")
for i in range(1, 6):
    print("%s: %s" % (plane_type[-i][0], plane_type[-i][1]))

print("-" * 30)
print("상위 5개 도착(목적지) 공항 (상대 공항)")
for i in range(1, 6):
    print("%s: %s" % (airport_destination[-i][0], airport_destination[-i][1]))

print("-" * 30)
print("상위 5개 출발(출발지) 공항 (상대 공항)")
for i in range(1, 6):
    print("%s: %s" % (airport_from[-i][0], airport_from[-i][1]))

print("-" * 30)
print("상위 5개 출발 시간대")
for i in range(1, 6):
    print("%s시: %s" % (departure_time[-i][0], departure_time[-i][1]))
