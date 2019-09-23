import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    f = open('csv_data_libraty.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)
