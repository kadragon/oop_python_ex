print(
    """
    세종특별자치시의 세종고속시외버스터미널에 관한 통계입니다.
    사용자의 입력을 받아 각 칼럼에 대한 통계를 출력합니다.
    """
)

import csv  # csv파일 불러오기를 위한 import
import operator  # 정렬을 위한 import
from sys import exit  # 프로그램 종료를 위한 import

# 파일 불러오기를 시도. 안되면 메세지 출력 후 프로그램 종료
try:
    f = open('세종특별자치시_세종고속시외버스터미널_시간표_20170609.csv', encoding='cp949')  # 파일 지정
except FileNotFoundError:  # 파일이 없다면
    print("파일이 존재하지 않습니다.")  # 메세지 출력
    exit(0)  # 프로그램 종료
else:
    data = csv.reader(f)  # 파일을 엶

# 첫 줄을 출력하여 데이터의 구분을 보여줍니다.
for row in data:
    print("데이터는 다음과 같은 구분으로 저장돼있습니다.")
    print(row)
    break

# 통계낼 데이터를 초기화합니다.
data_selected = [1, 2, 3, 4]
print("어떤 통계를 낼지 받습니다. 칼럼 [1~8]중 4개를 선택해 주세요. 공백/문자를 입력할 시 칼럼 1, 2, 3, 4에 대한 통계를 출력합니다.")
print("선택은 \n칼럼\n칼럼\n칼럼\n칼럼\n형식으로 입력해 주세요.")
# 통계를 낼 칼럼을 입력받습니다.
try:
    for i in range(0, 4):
        data_selected[i] = int(input())
        # 입력이 칼럼 [1~8]사이의 값이 아닐 경우 오류방지를 위해 원래 값으로 재설정합니다.
        if data_selected[i] not in range(1, 9):
            data_selected[i] = i + 1
# 만약 잘못된 값이 입력되면
except ValueError:
    # 메세지를 출력합니다.
    print("공백/문자를 입력하셨습니다. 칼럼 1, 2, 3, 4 에 대한 통계입니다.")
else:
    # 제대로 된 값들이 입력되면 메세지를 출력하고
    print("통계를 낼 4가지 칼럼의 인덱스입니다.")
    # 통계를 낼 칼럼의 번호들을 보여줍니다.
    for i in range(0, 4):
        print(data_selected[i])

# index는 0부터 시작하기에 통계 처리시 용이함을 위해 사용자가 입력한 값에서 1을 빼줍니다.
for i in range(0, 4):
    data_selected[i] = data_selected[i] - 1

# 데이터 저장용 dict 입니다.
first_dict = {}
second_dict = {}
third_dict = {}
forth_dict = {}

# 한개씩 꺼내서 데이터 분석
for row in data:
    # 만약 지금까지 저장된 내용들과 다른 내용이 있다면
    if row[data_selected[0]] not in first_dict:
        first_dict.setdefault(row[data_selected[0]], 1)
        # 새롭게 저장
    else:
        # 아니면 기존 내용의 값을 +1
        first_dict[row[data_selected[0]]] += 1
    # 같은 작업을 다른 통계들에도 반복
    if row[data_selected[1]] not in second_dict:
        second_dict.setdefault(row[data_selected[1]], 1)
    else:
        second_dict[row[data_selected[1]]] += 1

    if row[data_selected[2]] not in third_dict:
        third_dict.setdefault(row[data_selected[2]], 1)
    else:
        third_dict[row[data_selected[2]]] += 1

    if row[data_selected[3]] not in forth_dict:
        forth_dict.setdefault(row[data_selected[3]], 1)
    else:
        forth_dict[row[data_selected[3]]] += 1

# operator 로 dictionary type 을 list 로 정렬
sorted_first = sorted(first_dict.items(), key=operator.itemgetter(0))  # index 기준 정렬
sorted_second = sorted(second_dict.items(), key=operator.itemgetter(0))  # index 기준 정렬
sorted_third = sorted(third_dict.items(), key=operator.itemgetter(0))  # index 기준 정렬
sorted_forth = sorted(forth_dict.items(), key=operator.itemgetter(0))  # index 기준 정렬

# 통계낸 결과 출력
print("=" * 30)  # 구분선
for i in range(0, 4):  # 각각의 칼럼에 대한 통계를 순서대로 출력
    print("칼럼", data_selected[i] + 1, "의 통계")  # 처음에 index 로서의 처리를 위해 1을 뺏기 때문에 다시 더하여 출력해줍니다.
    if i == 0:
        for row in sorted_first:  # 저장된 값에서 각각의 내용과 값을 '내용:값' 형식으로 출력해 줍니다.
            print("%s: %d" % (row[0], row[1]))  # row[0]과 row[1]은 각각 내용과 값을 의미합니다.
        print("=" * 30)
        # 같은 작업을 나머지 통게에 대해서도 반복합니다.
    elif i == 1:
        for row in sorted_second:
            print("%s: %d" % (row[0], row[1]))
        print("=" * 30)
    elif i == 2:
        for row in sorted_third:
            print("%s: %d" % (row[0], row[1]))
        print("=" * 30)
    elif i == 3:
        for row in sorted_forth:
            print("%s: %d" % (row[0], row[1]))
        print("=" * 30)

# 프로그램이 바로 끝나는 것을 막기 위한 input
wait = input()
