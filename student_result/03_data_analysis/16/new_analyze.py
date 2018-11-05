import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# 1번째 try - except 구문
try:
    f = open('new_csv.csv', encoding='cp949')  # 일단 열어봄
except FileNotFoundError:  # 없으면
    print("해당 파일이 없습니다.")  # 없다 말해주고
    exit(0)  # 시스템 종료!
else:  # 아니면
    data = csv.reader(f)  # data 변수에 잘 저장


class csv_list:  # 일일히 다 쓰기 귀찮으니 class로 작성
    def __init__(self, sorted_list):  # 리스트를 입력받음
        self.sorted_list = sorted_list
        # 2번째 try - except 구문
        try:
            self.yes_perc = self.sorted_list[1][1]  # Y의 응답 개수를 기록
            self.no_perc = self.sorted_list[0][1]  # N의 응답 개수를 기록
        except IndexError:  # 어느 하나가 0이면 IndexError 발생
            if self.sorted_list[0][0] == 'Y':  # 0번째 줄의 첫 원소가 Y면 해당 자료는 모두 Y로 차 있음. 따라서 yes_perc에 모두 몰아줌
                self.yes_perc = self.sorted_list[0][1]
                self.no_perc = 0
            else:  # 반대 경우
                self.yes_perc = 0
                self.no_perc = self.sorted_list[0][1]

    def return_percentage(self):  # 데이터 분석에서 쓰이는 함수. Y와 N 중 Y의 비율을 return해줘요
        # 3번째 try - except 구문
        try:
            return round(100 * self.yes_perc / (self.yes_perc + self.no_perc), 2)
        except ZeroDivisionError:  # 자료의 개수가 0일 경우 ZeroDivisionError가 발생할 수 있음
            print("해당 자료가 없습니다.")  # 그 경우 해당 자료가 없다고 출력
            return  # 리턴

    def num_data(self):  # 데이터 개수
        return self.yes_perc + self.no_perc

    def num_yes(self):  # Y의 개수
        return self.yes_perc


# 변수 선언
num_data = 0  # 데이터의 개수
first_row = 0  # 첫 번째 줄은 배제하기 위함
road = {}  # 길의 종류를 저장하는 Dict 타입
type = {}  # 휴게소의 종류를 저장하는 Dict 타입
gas_station = {}  # 주유소가 있는지를 저장하는 Dict 타입
rest_room = {}  # 화장실이 있는지를 저장하는 Dict 타입
food_court = {}  # 음식점이 있는지를 저장하는 Dict 타입

for row in data:
    if first_row < 1:  # 첫 줄은 배제
        first_row += 1
        continue
    num_data += 1  # 데이터의 개수를 1+
    # 각각의 경우에 대해, 이미 해당 자료가 Dictionary에 있으면 그것의 Count를 +1. 없으면 새로 만들어서 그것의 Count를 1로 만듬
    if row[1] not in road:  # 도로 종류에 대한 Dict 자료형 작성
        road.setdefault(row[1], 1)
    else:
        road[row[1]] += 1

    if row[7] not in type:  # 휴게소 종류에 대한 Dict 자료형 작성
        type.setdefault(row[7], 1)
    else:
        type[row[7]] += 1

    if row[13] not in gas_station:  # 주유소에 대한 Dict 자료형 작성
        gas_station.setdefault(row[13], 1)
    else:
        gas_station[row[13]] += 1

    if row[18] not in rest_room:  # 화장실에 대한 Dict 자료형 작성
        rest_room.setdefault(row[18], 1)
    else:
        rest_room[row[18]] += 1

    if row[22] not in food_court:  # 음식점에 대한 Dict 자료형 작성
        food_court.setdefault(row[22], 1)
    else:
        food_court[row[22]] += 1

# Dictionary 타입들을 정렬된 리스트로 변환하는 과정
sorted_road = sorted(road.items(), key=operator.itemgetter(1))  # Value 기준
sorted_type = sorted(type.items(), key=operator.itemgetter(1))  # Value 기준
sorted_gas_station = sorted(gas_station.items(), key=operator.itemgetter(0))  # Index 기준. 일반적으로 [N, Y] 순서로 정렬됨
sorted_rest_room = sorted(rest_room.items(), key=operator.itemgetter(0))  # Index 기준. 일반적으로 [N, Y] 순서로 정렬됨
sorted_food_court = sorted(food_court.items(), key=operator.itemgetter(0))  # Index 기준. 일반적으로 [N, Y] 순서로 정렬됨

sorted_gas_station = csv_list(sorted_gas_station)  # Class에 List를 입력하여 해당 List에 대입
sorted_rest_room = csv_list(sorted_rest_room)  # Class에 List를 입력하여 해당 List에 대입
sorted_food_court = csv_list(sorted_food_court)  # Class에 List를 입력하여 해당 List에 대입

# 분석 결과 출력 (총 6가지의 의미있는 결과)
print("=" * 30)
print("전국 휴게소 개수 : %d" % num_data)  # 전국의 휴게소 개수를 출력 요정도면 의미있음
print("=" * 30)
print("도로 종류")  # 도로의 종류와 그 수를 출력 요것도 의미있음
for row in sorted_road:
    print("%s : %d" % (row[0], row[1]))
print("=" * 30)
print("휴게소 종류")  # 휴게소의 종류와 그 수를 출력 이건 당연히 의미있음
for row in sorted_type:
    print("%s : %d" % (row[0], row[1]))
print("=" * 30)
# 주유소가 있는 휴게소의 비율을 출력 매우 의미있음
print("주유소가 있는 휴게소의 비율 : " + "%.2f" % sorted_gas_station.return_percentage() + "% / 100.00%",
      "(총 %d개 중 %d개)" % (sorted_gas_station.num_data(), sorted_gas_station.num_yes()))
print("=" * 30)
# 화장실이 있는 휴게소의 비율을 출력 매우 의미있음
print("화장실이 있는 휴게소의 비율 : " + "%.2f" % sorted_rest_room.return_percentage() + "% / 100.00%",
      "(총 %d개 중 %d개)" % (sorted_rest_room.num_data(), sorted_rest_room.num_yes()))
print("=" * 30)
# 음식점이 있는 휴게소의 비율을 출력 매우 의미있음
print("음식점이 있는 휴게소의 비율 : " + "%.2f" % sorted_food_court.return_percentage() + "% / 100.00%",
      "(총 %d개 중 %d개)" % (sorted_food_court.num_data(), sorted_food_court.num_yes()))
print("=" * 30)
