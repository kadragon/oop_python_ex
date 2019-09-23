import csv
from sys import exit

# 공공주차장 파일을 열어준다.
# 만약 파일이 없다면 try_except 구문을 이용해 에러를 방지해준다.
try:
    f = open('parkingslot.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없습니다.")
    exit(0)
else:
    data = csv.reader(f)

# 자료 분석에 필요한 list와 set이다.
# 공공주차장의 기본 이용시간, 기본 요금, 주차구획수, 관리 기관에 대한 분석을 진행한다.
standard_time = list()
standard_money = list()
standard_size = list()
standard_check = list()
my_set = {0}
my_set_money = {0}
my_set_size = {0}
my_set_check = {0}

# 입력 받은 data를 이용해 필요한 정보를 받는다.
# set을 사용하는 이유는 중복된 데이터가 필요 없고 어떤 데이터가 들어왔는지에 대한 정보만 필요하기 때문이다.
for row in data:
    # 만약 비어 있는 줄이거나 맨 앞줄이면 continue로 없애준다.
    if len(row) == 0 or row[0] == '주차장관리번호':
        continue

    # 기본 이용시간 분석에 대한 구문
    # 데이터가 대부분 숫자이다가 중간에 '-'인 데이터가 있어 오류가 발생한다.
    # try_except를 통해서 ValueError가 발생하면 아무런 작업 없이 넘어가 준다.
    try:
        t = int(row[17])

        my_set.add(t)
        standard_time.append(t)
    except ValueError:
        print("", end="")

    # 기본 이용 요금에 대한 구문
    # 이 곳에는 데이터가 대부분 숫자이다가 중간에 '-'인 데이터가 있어 오류가 발생한다.
    # try_except를 통해서 ValueError가 발생하면 아무런 작업 없이 넘어가 준다.
    try:
        m = int(row[18])
        my_set_money.add(m)
        standard_money.append(m)
    except ValueError:
        print("", end="")

    # 주차구획수에 대한 구문
    # 문제가 발생하는 데이터가 없어서 try_except가 필요 없다.
    # 구간을 100 단위로 나누기 위해 100으로 나눈 몫을 사용한다.
    s = int(row[6])
    s = s // 100
    my_set_size.add(s)
    standard_size.append(s)

    # 관리 기관에 대한 구문
    # 관리 기관은 기본적으로 문자이기 때문에 문제가 발생하지 않는다.
    c = row[26]
    my_set_check.add(c)
    standard_check.append(c)

# 파일 사용이 끝났으니 닫아준다.
f.close()

# set에 들어 있는 목록과 list에 추가되어 있는 모든 데이터 값을 이용한다.
# set에 들어있는 정보를 하나 선정하고, list의 count 함수를 이용해 몇 번 나왔는지 셀 수 있다.
# 가장 많이 나온 것과 두 번째로 많이 나온 것을, 간단하게 for문 두 번으로 뽑아낼 수 있다.
# 아래 4개의 코드 모두 같은 방식이다.
print("------시간 DATA------")
max_standard_time = -1
max_standard_time_idx = 0

for i in my_set:
    if standard_time.count(i) > max_standard_time:
        max_standard_time_idx = i
        max_standard_time = standard_time.count(i)

my_set.remove(max_standard_time_idx)

print("가장 많은 기본 시간 \t %d min. %d곳" % (max_standard_time_idx, max_standard_time))
max_standard_time = -1
max_standard_time_idx = 0

for i in my_set:
    if standard_time.count(i) > max_standard_time:
        max_standard_time_idx = i
        max_standard_time = standard_time.count(i)
print("두번째로 많은 기본 시간 \t %d min. %d곳\n" % (max_standard_time_idx, max_standard_time))

print("------요금 DATA------")
max_standard_money = -1
max_standard_money_idx = 0

for i in my_set_money:
    if standard_money.count(i) > max_standard_money:
        max_standard_money_idx = i
        max_standard_money = standard_money.count(i)

my_set_money.remove(max_standard_money_idx)

print("가장 많은 기본 요금 \t %d won. %d곳" % (max_standard_money_idx, max_standard_money))
max_standard_money = -1
max_standard_money_idx = 0

for i in my_set_money:
    if standard_money.count(i) > max_standard_money:
        max_standard_money_idx = i
        max_standard_money = standard_money.count(i)
print("두번째로 많은 기본 요금 \t %d won. %d곳\n" % (max_standard_money_idx, max_standard_money))

print("------주차구획수 DATA------")
max_standard_size = -1
max_standard_size_idx = 0
for i in my_set_size:
    if standard_size.count(i) > max_standard_size:
        max_standard_size_idx = i
        max_standard_size = standard_size.count(i)

my_set_size.remove(max_standard_size_idx)

print("가장 많은 구획수 구간 \t %d ~ %d : %d곳" % (
max_standard_size_idx * 100, (max_standard_size_idx + 1) * 100, max_standard_size))
max_standard_size = -1
max_standard_size_idx = 0

for i in my_set_size:
    if standard_size.count(i) > max_standard_size:
        max_standard_size_idx = i
        max_standard_size = standard_size.count(i)
print("두번째로 많은 구획수 구간 \t %d ~ %d : %d곳\n" % (
max_standard_size_idx * 100, (max_standard_size_idx + 1) * 100, max_standard_size))

print("------관리기관 DATA------")
max_standard_check = -1
max_standard_check_idx = 0
for i in my_set_check:
    if standard_check.count(i) > max_standard_check:
        max_standard_check_idx = i
        max_standard_check = standard_check.count(i)

my_set_check.remove(max_standard_check_idx)

print("가장 많은 주차장을 관리하는 기관 \t %s : %d곳" % (max_standard_check_idx, max_standard_size))
max_standard_check = -1
max_standard_check_idx = 0

for i in my_set_check:
    if standard_check.count(i) > max_standard_check:
        max_standard_check_idx = i
        max_standard_check = standard_check.count(i)
print("두번째로 많은 주차장을 관리하는 기관 \t %s : %d곳" % (max_standard_check_idx, max_standard_check))
