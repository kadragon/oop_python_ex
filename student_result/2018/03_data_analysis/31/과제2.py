import csv  # csv 파일 처리를 위해서
import sys  # exit를 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('소상공인시장진흥공단_상가업소정보_201806_01.csv', encoding='cp949')  # 한글로 데이터 불러오기
except FileNotFoundError:
    print("파이리 없어요;;")  # 파일 에러가 나면 파일이 없다는 것을 표시후, 프로그램 종료
    sys.exit(0)
else:
    data = csv.reader(f)  # data에 파일 속 데이터를 담는다.

name = 0  # 데이터를 표시하는 첫행을 제외하기 위함.
area_dict = {}  # 서울지역에 있는 pc방의 수를 '구'단위로 세기 위한 dictionary
place_dict = {}  # 강남구에 있는 pc방의 수를 '동'단위로 세기 위한 dictionary

for row in data:
    if name == 0:
        print("<데이터 종류>\n")
        for cnt in range(38):  # 첫 행에 있는 분류 항목의 인덱스값을 표시
            print("%d : %s" % (cnt, row[cnt]))
        print()
        name += 1

    else:
        if row[8] == '인터넷PC방' and row[12] == '서울특별시':  # 서울특별시에 있는 pc방을 조사
            if row[14] not in area_dict:
                area_dict.setdefault(row[14], 1)  # dictionary에 없는 값이면 항목을 추가
            else:
                area_dict[row[14]] += 1  # dictionary에 있다면 그 수를 추가

        if row[8] == '인터넷PC방' and row[14] == '강남구':
            try:
                place_dict[row[18]] += 1  # 일단 수를 추가하도록 시도
            except KeyError:  # 그 항목이 dictionary에 없어서 'KeyError'가 뜬다면
                place_dict.setdefault(row[18], 1)  # dictionary에 항목을 추가

min_area = max_area = 'where'  # 초기값 설정
area_max = 0
area_min = 123456789  # 한 지역에 pc방이 123456789곳이 있지는 않겠지...;;

for pc in area_dict:
    if area_max < area_dict[pc]:
        area_max = area_dict[pc]  # pc방이 가장 많은 '구'의 pc방 수를 저장
        max_area = pc  # pc방이 가장 많은 '구'의 이름을 저장
    if area_min > area_dict[pc]:
        area_min = area_dict[pc]  # pc방이 가장 적은 '구'의 pc방 수를 저장
        min_area = pc  # pc방이 가장 적은 '구'의 이름을 저장

print("1. pc방이 가장 많은 서울지역은 %s로, 총 %d곳 있습니다." % (max_area, area_max))
print("2. pc방이 가장 많은 서울지역은 %s로, 총 %d곳 있습니다." % (min_area, area_min))

min_place = max_place = 'where'  # 값 초기화
place_max = 0
place_min = 123456789  # pc방 수가 123456789개가 넘는 '동'은 없으리라 믿고..

for pc in place_dict:
    if place_max < place_dict[pc]:
        place_max = place_dict[pc]  # pc방이 가장 많은 '동'의 pc방 수를 저장
        max_place = pc  # pc방이 가장 많은 '동'의 이름을 저장
    if place_min > place_dict[pc]:
        place_min = place_dict[pc]  # pc방이 가장 적은 '동'의 pc방 수를 저장
        min_place = pc  # pc방이 가장 적은 '동'의 이름을 저장

print("3. 강남구에서 pc방이 가장 많은 지역은 %s으로, 총 %d곳 있습니다." % (max_place, place_max))
print("4. 강남구에서 pc방이 가장 적은 지역은 %s으로, 총 %d곳 있습니다." % (min_place, place_min))
