import sys  # 프로그램 종료
import csv  # csv 파일 처리
import operator  # 정렬

try:  # file 열기 시도
    f = open('csv_data_cctv.csv', encoding='cp949')
except FileNotFoundError:  # FileNotFoundError 일 경우 프로그램 종료
    print("파일이 없는데요?!")
    sys.exit(0)
else:  # 있을 경우 csv로 data
    data = csv.reader(f)

# 저장
manage = {}  # 관리 기관
purpose = {}  # 설치 목적
quality = {}  # 카메라 화소수
total_cctv = 0  # 전체 카메라 개수

check = 0
# 한 행씩 row로 꺼내기
for row in data:
    # 첫번째 행 츨력(데이터 입력)
    if check == 0:
        print(row)
        check = 1
        continue

    # 설치 기관 통계 내기
    if row[0] not in manage:
        manage.setdefault(row[0], 1)
    else:
        manage[row[0]] += 1

    # 설치 목적 통계 내기
    if row[3] not in purpose:
        purpose.setdefault(row[3], 1)
    else:
        purpose[row[3]] += 1

    # 전국에 설치된 카메라 수
    total_cctv += int(row[4])

    # 카메라 화소수
    if row[5] not in quality:
        quality.setdefault(row[5], 1)
    else:
        quality[row[5]] += 1

# operator 를 활용하여 dictionary type 을 정렬된 list 로 변환
sort_manage = sorted(manage.items(), key=operator.itemgetter(1))  # 설치한 기관 중 상위 5개
sort_purpose = sorted(purpose.items(), key=operator.itemgetter(1))  # 설치 목적 중 상위 5개
sort_quality = sorted(quality.items(), key=operator.itemgetter(1))  # 카메라 화소수 중 최대 개수인 것

# 각 딕셔너리의 길이를 통해 상위 5개 출력
len_pur = len(sort_purpose) - 1
len_manage = len(sort_manage) - 1
len_quality = len(sort_quality) - 1

# cctv 관리 기관 출력
cnt = 0
print("cctv를 설치한 상위 기관 5개")
while cnt < 5:
    row = sort_manage[len_manage - cnt]
    print("%d위:" % (cnt + 1), "%s" % row[0], "- %d개 " % row[1])
    cnt += 1
print("=" * 30)

# cctv 설치 목적 출력
cnt = 0
print("cctv가 설치된 목적 상위 5개")
while cnt < 5:
    row = sort_purpose[len_pur - cnt]
    print("%d 위:" % (cnt + 1), "%s" % row[0], "- %d개 " % row[1])
    cnt += 1
print("=" * 30)

# cctv 설치 전체 개수 출력
print("전체 cctv 수:%d" % total_cctv)
print("=" * 30)

# 가장 보편적인 cctv 화소 수
print("가장 보편적인 cctv 화소 수: %s" % sort_quality[len_quality][0])
print("=" * 30)

# 파일에 출력한 답을 쓰기
try:
    f = open('data_cctv_csv.txt', 'w', encoding='UTF-8')
except FileNotFoundError:  # 파일이 없다면 쓰지말고 종료
    print('No File.')
    sys.exit(0)
else:  # 있다면 쓰기 시작
    # 정렬된 관리 기관 딕셔너리 입력
    f.write('=' * 15 + '관리 기관' + '=' * 15 + '\n')
    for data in sort_manage:
        f.write(data[0] + ' : ' + str(data[1]) + '\n')
    f.write('\n')
    # 정렬된 설치 목적 딕셔너리 입력
    f.write('=' * 15 + '설치 목적' + '=' * 15 + '\n')
    for data in sort_purpose:
        f.write(data[0] + ' : ' + str(data[1]) + '\n')
    f.write('\n')
    # 전체 cctv 개수 입력
    f.write('=' * 15 + '총 개수' + '=' * 15 + '\n')
    f.write(str(total_cctv) + '개')
    f.write('\n')
    # 정렬된 카메라 화소 딕셔너리 입력
    f.write('=' * 15 + '카메라 화소' + '=' * 15 + '\n')
    f.write(sort_quality[len_quality][0])
