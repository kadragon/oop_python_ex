# -*- coding: utf-8 -*-
"""
Title       public_wifi (과제 2)
Author      ITSC (Taewon Kang)
Date        2018.09.28
"""

import csv
import operator
from sys import exit

try:
    csv_file = open('public_wifi.csv', encoding='cp949')  # public_wifi.csv 파일을 cp949 포맷으로 불러옴
except FileNotFoundError:
    print('파일이 없습니다. ')  # (except 1) 만약 파일이 없다면, 파일이 없다는 에러 메시지를 출력함.
    exit(0)  # 프로그램을 종료함.

else:
    data = csv.reader(csv_file)  # 파일이 있다면 불러옴

try:
    first_row = 0  # 공공 데이터의 첫 줄을 알아내기 위한 변수 (칼럼줄 관리로 사용됨)

    # Dictionary Type 으로 데이터를 분석하여 저장함.
    installed_loc = {}  # 설치된 시 (서울특별시, 부산광역시 등)
    installed_facility = {}  # 설치 시설 (관공서 등)
    service_operator = {}  # 서비스 제공사명 (통신사)
    wifi_operator = {}  # 와이파이 관리기관 명 (서울특별시 강남구청 등)

    # 한개씩 꺼내서 데이터 분석
    for row in data:
        # 첫 번째 줄과, 두 번째 줄은 컬럼과 Value 확인
        if first_row < 2:
            print(row)
            first_row += 1
            # 첫번재 줄은 컬럼이기 때문에 분석에 활용하지 않음
            if first_row == 1:
                continue

        # ====================================================
        # (1) 와이파이가 설치된 시 통계 내기

        if row[2] not in installed_loc:
            installed_loc.setdefault(row[2], 1)

        else:
            installed_loc[row[2]] += 1

        # ====================================================
        # (2) 와이파이가 설치된 시설 통계 내기

        if row[4] not in installed_facility:
            installed_facility.setdefault(row[4], 1)

        else:
            installed_facility[row[4]] += 1

        # ====================================================
        # (3) 와이파이 서비스 제공자 통계 내기

        if row[5] not in service_operator:
            service_operator.setdefault(row[5], 1)

        else:
            service_operator[row[5]] += 1

        # ====================================================
        # (4) 와이파이 관리기관명 통계 내기

        if row[10] not in wifi_operator:
            wifi_operator.setdefault(row[10], 1)

        else:
            wifi_operator[row[10]] += 1

        # ====================================================

    # 먼저, Value 기준으로 operator를 활용하여 Dictionary Type을 정렬된 List로 반환
    sorted_installed_loc = sorted(installed_loc.items(), key=operator.itemgetter(1))
    sorted_installed_facility = sorted(installed_facility.items(), key=operator.itemgetter(1))
    sorted_service_operator = sorted(service_operator.items(), key=operator.itemgetter(1))
    sorted_wifi_operator = sorted(wifi_operator.items(), key=operator.itemgetter(1))

    sorted_installed_facility.reverse()  # 상위 5개 데이터를 표시하기 위해, 4개 딕셔너리 값을 뒤집음
    sorted_installed_loc.reverse()
    sorted_service_operator.reverse()
    sorted_wifi_operator.reverse()

    print("=" * 50)
    print("설치 시별 와이파이 설치 통계")
    top = 0  # 상위 5개 데이터를 출력하였는지 확인하는 카운팅 변수
    for row in sorted_installed_loc:
        print("%s: %d" % (row[0], row[1]))  # 설치된 시, 와이파이 개수 출력
        top = top + 1
        if top >= 5: break  # 상위 5개 데이터만 표시

    print("=" * 50)
    print("설치 시설별 와이파이 설치 통계")
    top = 0  # 상위 5개 데이터를 출력하였는지 확인하는 카운팅 변수
    for row1 in sorted_installed_facility:
        print("%s: %d" % (row1[0], row1[1]))  # 설치된 시설, 와이파이 개수 출력
        top = top + 1
        if top >= 5: break  # 상위 5개 데이터만 표시

    print("=" * 50)
    print("서비스 제공사별 와이파이 설치 통계")
    top = 0  # 상위 5개 데이터를 출력하였는지 확인하는 카운팅 변수
    for row2 in sorted_service_operator:
        print("%s: %d" % (row2[0], row2[1]))  # 서비스 제공사명, 와이파이 개수 출력
        top = top + 1
        if top >= 5: break  # 상위 5개 데이터만 표시

    print("=" * 50)
    print("와이파이 관리 기관별 와이파이 설치 통계")
    top = 0  # 상위 5개 데이터를 출력하였는지 확인하는 카운팅 변수
    for row3 in sorted_wifi_operator:
        print("%s: %d" % (row3[0], row3[1]))  # 와이파이 관리 기관명, 와이파이 개수 출력
        top = top + 1
        if top >= 5: break  # 상위 5개 데이터만 표시

    print("=" * 50)
except KeyboardInterrupt:  # (except 2) 만약 Ctrl+C 등의 KeyboardInterrupt 가 감지되면,
    print('Keyboard Interrupt Detected!!!')

finally:  # 프로그램 종료 메시지 출력
    print("프로그램을 종료합니다.")
