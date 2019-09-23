import csv
import operator

# csv 파일을 불러온다
try:
    f = open('전국무료와이파이표준데이터.csv', encoding='cp949')  # csv 파일 열기
except FileNotFoundError:
    print('csv 파일이 존재하지 않습니다.')
    exit(0)
else:
    data = csv.reader(f)  # csv 파일을 저장한 f를 읽기

first_row = 0  # 첫번째 줄을 출력하여 어떤 인덱스들이 있는지 확인하기 위한 변수
area = {}  # 공공와이파이가 있는 지역
comp = {}  # 공공 와이파이 제공사
fac = {}  # 공공 와이파이 설치 장소 구분
pos = {}  # 공공 와이파이 관리기관

print("<전국 공공 Wifi 현황 데이터 분석> ")
print("=" * 30)
print(
    "'지역별 공공 Wifi 현황'을 알고 싶으면 '1', '공공 Wifi 제공사 현황(상위 3사)'를 알고 싶으면 '2', '공공 Wifi 설치장소 현황'을 알고 싶으면 '3', '공공 Wifi 관리기관 현황'를 알고 싶으면 '4'를 눌러 주세요.")


def Enter():  # 입력값이 올바른지 판단하기 위한 함수
    try:
        x = int(input())
        if 1 > x or x > 4:
            print("1~4를 입력해주세요.")
            return Enter()
        else:
            return x
    except TypeError:
        print("1~4를 입력해주세요.")
        return Enter()
    except ValueError:
        print("1~4를 입력해주세요.")
        return Enter()


enter = Enter()  # 입력값을 enter 변수에 저장
print("=" * 30)

# 한 개씩 꺼내서 '지역별 공공 Wifi 현황' 데이터 분석
if enter == 1:
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            if first_row == 1:
                continue

        # dict가 선언되어 있는지 확인하여 값 설정
        # 지역 통계 내기
        if row[2] not in area:  # 지역 이름이 area 딕셔너리에 없으면
            area.setdefault(row[2], 1)  # area 딕셔너리에 키와 값을 추가
        else:  # 지역 이름이 area 딕셔너리에 있으면
            area[row[2]] += 1  # 딕셔너리 값을 1 증가

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_area = sorted(area.items(), key=operator.itemgetter(1))
    # 정렬된 list를 역순으로 저장
    sorted_area.reverse()

    print("=" * 30)
    print("[지역별 공공 Wifi 현황]")
    # 공공와이파이가 많은 지역 순으로 지역 이름과 값 출력
    for row in sorted_area:
        result = (row[0] + ':', row[1])
        print("%s : %d곳" % (row[0], row[1]))
    print("=" * 30)

# 한 개씩 꺼내서 '공공 Wifi 제공사 현황(상위 3사)' 데이터 분석
elif enter == 2:
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            if first_row == 1:
                continue

        # dict가 선언되어 있는지 확인하여 값 설정
        # 와이파이 제공사 통계
        if row[5] not in comp:  # 제공사 이름이 comp 딕셔너리에 없으면
            comp.setdefault(row[5], 1)  # comp 딕셔너리에 키와 값을 추가
        else:  # 제공사 이름이 comp 딕셔너리에 없으면
            comp[row[5]] += 1  # 딕셔너리 값을 1 증가

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_comp = sorted(comp.items(), key=operator.itemgetter(1))
    # 정렬된 list를 역순으로 저장
    sorted_comp.reverse()

    print("=" * 30)
    print("[공공 Wifi 제공사 현황(상위 3사)]")
    # 공공와이파이를 가장 많이 제공하는 회사 순으로 3번째까지 값과 함께 출력
    for i in range(3):
        print("%s : %d곳" % (sorted_comp[i][0], sorted_comp[i][1]))
    print("=" * 30)

# 한 개씩 꺼내서 '공공 Wifi 설치장소 현황' 데이터 분석
elif enter == 3:
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            if first_row == 1:
                continue

        # dict가 선언되어 있는지 확인하여 값 설정
        # 설치 장소 통계 내기
        if row[4] not in fac:  # 장소 이름이 fac 딕셔너리에 없으면
            fac.setdefault(row[4], 1)  # fac 딕셔너리에 키와 값을 추가
        else:  # 장소 이름이 fac 딕셔너리에 있으면
            fac[row[4]] += 1  # 딕셔너리 값을 1 증가

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_fac = sorted(fac.items(), key=operator.itemgetter(1))
    # 정렬된 list를 역순으로 저장
    sorted_fac.reverse()

    print("=" * 30)
    print("[공공 Wifi 설지 장소 현황]")
    # 공공와이파이가 가장 많이 설치된 순으로 장소 이름과 값 출력
    for i in range(5):
        print("%s : %d곳" % (sorted_fac[i][0], sorted_fac[i][1]))
    print("=" * 30)

# 한 개씩 꺼내서 '공공 Wifi 관리기관 현황' 데이터 분석
else:
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            if first_row == 1:
                continue

        # dict가 선언되어 있는지 확인하여 값 설정
        # 관리기관 통계 내기
        if row[10] not in pos:  # 기관 이름이 pos 딕셔너리에 없으면
            pos.setdefault(row[10], 1)  # pos 딕셔너리에 키와 값을 추가
        else:  # 장소 이름이 pos 딕셔너리에 있으면
            pos[row[10]] += 1  # 딕셔너리 값을 1 증가

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_pos = sorted(pos.items(), key=operator.itemgetter(1))
    # 정렬된 list를 역순으로 저장
    sorted_pos.reverse()

    print("=" * 30)
    print("[공공 Wifi 관리기관 현황]")
    # 공공와이파이를 가장 많이 관리하는 관리기관 순으로 이름과 값 출력
    for i in range(10):
        print("%s : %d곳" % (sorted_pos[i][0], sorted_pos[i][1]))
    print("=" * 30)
