import csv  # csv 파일 처리를 위해서
import operator  # dict 정렬에 활용하기 위해서
from sys import exit  # 프로그램 종료 시키기 위해서

'''
경기도 내의 12 시군

서비스 제공사명
와이파이 SSID
설치시설 구분
단위 면적당 와이파이의 개수
'''

# 각 지자체 넓이
Area = {'가평군': 843.3, '과천시': 35.86, '광주시': 431.0, '남양주시': 458.0, '수원시': 121.0, '안성시': 554.2, '안양시': 58.46,
        '의정부시': 81.59, '이천시': 461.3, '평택시': 452.3, '포천시': 826.5, '하남시': 93.07}

# 자료 저장 공간
서비스제공사명 = {}
와이파이SSID = {}
설치시설구분 = {}
와이파이개수 = {}


class analyzer:

    def __init__(self, name):
        self.name = name

    # 각각에 대해 분석
    def get_data(self):
        # file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
        try:
            f = open('%02d.csv' % self.name, encoding='cp949')
        except FileNotFoundError:
            print("파일이 없는데요?!")
            exit(0)
        else:
            data = csv.reader(f)
            self.data = data

    def analyze(self):
        global 서비스제공사명
        global 와이파이SSID
        global 설치시설구분
        global 와이파이개수

        flag = True
        for row in self.data:
            if flag:
                flag = False
                continue

            # 서비스제공사명 찾기
            # 서비스제공사가 여러개일때
            try:
                l = row[5].split(',')
                for i in l:
                    i = i.strip()
                    if i not in 서비스제공사명:
                        서비스제공사명.setdefault(i, 1)
                    else:
                        서비스제공사명[i] += 1
            except:
                if row[5] not in 서비스제공사명:
                    서비스제공사명.setdefault(row[5], 1)
                else:
                    서비스제공사명[row[5]] += 1

            # 설치시설구분
            if row[4] not in 설치시설구분:
                설치시설구분.setdefault(row[4], 1)
            else:
                설치시설구분[row[4]] += 1

            # 와이파이 개수 찾기
            convert_list = list(Area)
            if convert_list[self.name] not in 와이파이개수:
                와이파이개수.setdefault(convert_list[self.name], 1)
            else:
                와이파이개수[convert_list[self.name]] += 1

            # 와이파이ssid
            if row[6] == '':
                continue
            if row[6] not in 와이파이SSID:
                와이파이SSID.setdefault(row[6], 1)
            else:
                와이파이SSID[row[6]] += 1


def decorator_function(out_function):
    def wrapper_function():
        print('=' * 18)
        return out_function()

    return wrapper_function


@decorator_function
def output_서비스제공사명():
    print('서비스제공사명, 개수')
    print('-' * 18)
    for res in 서비스제공사명.items():
        print(res)


@decorator_function
def output_와이파이SSID():
    print('와이파이SSID, 개수')
    print('-' * 18)
    for res in 와이파이SSID.items():
        print(res)


@decorator_function
def output_설치시설구분():
    print('설치시설구분, 개수')
    print('-' * 18)
    for res in 설치시설구분.items():
        print(res)


@decorator_function
def output_와이파이개수():
    print('지역명, 와이파이개수')
    print('-' * 18)
    for res in 와이파이개수.items():
        print(res)


for i in range(len(Area)):
    result = analyzer(i)
    result.get_data()
    result.analyze()

output_서비스제공사명()
output_와이파이SSID()
output_설치시설구분()
output_와이파이개수()
