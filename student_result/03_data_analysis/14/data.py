import csv  # csv 파일 처리
import operator  # dict 정렬
from sys import exit  # 프로그램 종료
import time


def data_play():
    try:
        f = open('한국장애인고용공단_장애물_없는_생활환경(Barrier_Free)_인증_시설_정보_20180807.csv', encoding='cp949')
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
        exit(0)
    else:
        data = csv.reader(f)

    # 공공 데이터의 첫줄은 이게 어떤 데이터인지 적혀있는 칼럼줄 관리용 변수
    first_row = 0

    # 데이터를 분석 저장 dictionary Type
    area_dict = {}  # 지역
    best_no = {}  # 최우수 등급 공공 시설
    best_po = {}  # 최우수 등급 민간 시설
    year_dict = {}  # 년도

    # 한개씩 꺼내서 데이터 분석
    for row in data:
        # 첫번째 줄과 두번째 줄을 출력하여, 어떤 데이터와 어떤 값의 형태로 들어가 있는 지 확인
        if first_row < 2:
            print(row)
            first_row += 1
            # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
            if first_row == 1:
                continue

        # dict 가 선언되어 있는지 확인하여 값 설정
        # 지역 통계 내기
        if row[7] not in area_dict:
            area_dict.setdefault(row[7], 1)
        else:
            area_dict[row[7]] += 1

        # 최우수 공공 인증기관 보유 지역 찾기
        if row[6] == '최우수' and row[9] == '공공':
            if row[7] not in best_no:
                best_no.setdefault(row[7], 1)
            else:
                best_no[row[7]] += 1

        # 최우수 민간 인증기관 보유 지역 찾기
        if row[6] == '최우수' and row[9] == '민간':
            if row[7] not in best_po:
                best_po.setdefault(row[7], 1)
            else:
                best_po[row[7]] += 1

        # 년도별 인증기관 수
        if row[0] not in year_dict:
            year_dict.setdefault(row[0], 1)
        else:
            year_dict[row[0]] += 1

    # operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
    sorted_area = sorted(area_dict.items(), key=operator.itemgetter(0))  # index 기준
    sorted_best_no = sorted(best_no.items(), key=operator.itemgetter(1))  # value 기준
    sorted_best_po = sorted(best_po.items(), key=operator.itemgetter(1))  # value 기준
    sorted_year_dict = sorted(year_dict.items(), key=operator.itemgetter(0))  # index 기준

    # 최우수 공공 인증기관 최다 보유 지역 구하기
    best_no_cnt = 0  # 최다 보유 시설수
    best_no_area = []  # 최다 보유 지역의 이름과 시설수를 저장할 리스트
    for row in sorted_best_no:  # 전체 지역이 가진 최우수 등급 공공 시설 수 중 최고값을 찾기
        if row[1] > best_no_cnt:
            best_no_cnt = row[1]
    for row in sorted_best_no:  # 최고값에 해당하는 시설수를 가진 지역의 이름과 시설수를 저장
        if row[1] == best_no_cnt:
            best_no_area.append([row[0], row[1]])

    # 최우수 민간 인증기관 최다 보유 지역 구하기
    best_po_cnt = 0  # 최다 보유 시설수
    best_po_area = []  # 최다 보유 지역의 이름과 시설수를 저장할 리스트
    for row in sorted_best_po:  # 전체 지역이 가진 최우수 등급 민간 시설 수 중 최고값을 찾기
        if row[1] > best_po_cnt:
            best_po_cnt = row[1]
    for row in sorted_best_po:  # 최고값에 해당하는 시설수를 가진 지역의 이름과 시설수를 저장
        if row[1] == best_po_cnt:
            best_po_area.append([row[0], row[1]])

    print("=" * 40)
    print("[1] 지역별 BF(Barrier Free)인증기관 수")  # 지역별 인증기관 수 출력
    for row in sorted_area:
        print("%15s : %d" % (row[0], row[1]))
    print("=" * 40)
    time.sleep(1)
    print("[2] 최우수 공공 인증기관 최다 보유 지역")
    i = 0
    while i < len(best_no_area):  # 최다 보유 지역 이름, 시설 수 정보 출력
        print("%15s : %d곳" % (best_no_area[i][0], best_no_area[i][1]))
        i += 1
    print("=" * 40)
    time.sleep(1)
    print("[3] 최우수 민간 인증기관 최다 보유 지역")
    i = 0
    while i < len(best_po_area):  # 최다 보유 지역 이름, 시설 수 정보 출력
        print("%15s : %d곳" % (best_po_area[i][0], best_po_area[i][1]))
        i += 1
    print("=" * 40)
    time.sleep(1)
    print("[4] 년도별 인증기관 수 | 2018.08 까지")  # 년도별 인증기관 수 출력
    for row in sorted_year_dict:
        print("%15s : %s곳" % (row[0], row[1]))
    print("=" * 40)


# pycharm 이 아니라 python 3.7(32bit) 버전으로 Ctrl+c(KeyboardInterrtupt)를 해야 작동함  : )
try:
    data_play()
except KeyboardInterrupt:
    print('-' * 10 + "분석을 중단하고 종료하시겠습니까? yes/no", end=' : ')
    a = input().upper()
    if a == 'YES':
        exit(0)
    else:  # 종료할 의사가 분명하지 않은 것 같으니 그냥 계속 분석결과를 보여주자.
        print('-' * 10 + "분석을 다시 진행합니다.")
        time.sleep(2)
        data_play()
