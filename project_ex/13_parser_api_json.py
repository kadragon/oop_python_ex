import bs4
import requests
import urllib.request
from urllib import parse
import json
import matplotlib.pyplot as plt
import numpy as np

API_AUTH_KEY = "API_KEY"

"""
https://www.data.go.kr/dataset/15000581/openapi.do

3. 시도별 실시간 측정정보 조회
시도명을 검색조건으로 하여 시도별 측정소목록에 대한 
일반 항목과 CAI 최종 실시간 측정값과 지수 정보 조회 기능을 제공하는 시도별 실시간 측정정보 조회

Request Parameter
numOfRows   10      0   한 페이지 결과 수 
pageNo      1       0   페이지 번호 
sidoName    세종    1   시도 이름 (서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종) 
ver         1.3     0   버전별 상세 결과 참고문서 참조 

http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?
serviceKey=API_AUTH_KEY
&numOfRows=10
&sidoName=%EC%84%B8%EC%A2%85
&ver=1.3
"""

getCtprvnRltmMesureDnsty = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"


def make_url_getCtprvnRltmMesureDnsty(sidoName, numOfRows=10):
    return "%s?serviceKey=%s&numOfRows=%d&sidoName=%s&ver=1.3&_returnType=json" % (getCtprvnRltmMesureDnsty, API_AUTH_KEY, numOfRows, parse.quote(sidoName))


target_url = make_url_getCtprvnRltmMesureDnsty('세종', 20)

with urllib.request.urlopen(target_url) as url:
    data = json.loads(url.read().decode(url.headers.get_content_charset()))
    my_place = ''
    for sub_data in data['list']:
        if sub_data['stationName'] == '아름동':
            my_place = sub_data
            break

    data_column = list(my_place)
    no_use_column = "stationName dataTime dataTerm mangName pageNo resultCode resultMsg rnum serviceKey sidoName stationCode stationName totalCount ver _returnType"

    print("[ 실시간 공기질 정보 | %s | %s]" % (my_place['stationName'], my_place['dataTime']))
    print("[통합대기환경지수] %s 등급" % my_place['khaiGrade'])

    for column_name in data_column:
        if column_name not in no_use_column.split():
            # print("%s: %s" % (column_name, my_place[column_name]))
            if  'Grade' in column_name:
                if 'co' in column_name:
                    print("%s: \t%s등급" % ("[일산화탄소]", my_place[column_name]))
                elif 'no2' in column_name:
                    print("%s: \t%s등급" % ("[이산화질소]", my_place[column_name]))
                elif 'pm10Grade1h' in column_name:
                    print("%s: \t%s등급" % ("[PM10]", my_place[column_name]))
                elif 'pm25Grade1h' in column_name:
                    print("%s: \t%s등급" % ("[PM25]", my_place[column_name]))
                elif 'so2' in column_name:
                    print("%s: \t%s등급" % ("[아황산가스]", my_place[column_name]))
                elif 'o3' in column_name:
                    print("%s: \t%s등급" % ("[오존]", my_place[column_name]))
    
"""
https://www.data.go.kr/dataset/15000581/openapi.do

5. 시도별 실시간 평균정보 조회

시도별 측정소목록에 대한 일반 항목의 시간 및 일평균 자료 및 지역 평균 정보를 제공하는
시도별 실시간 평균정보 조회

numOfRows	    한 페이지 결과 수   4	0	10	한 페이지 결과 수
pageNo	        페이지 번호         4	0	1	페이지 번호
itemCode	    항목명	            10	1	PM10	측정항목 구분(SO2, CO, O3, NO2, PM10, PM25)
dataGubun	    자료 구분	        10	1	HOUR	요청 자료 구분(시간평균 : HOUR, 일평균 : DAILY)
searchCondition	데이터 기간	        10	0	MONTH	요청 데이터기간 (일주일 : WEEK, 한달 : MONTH)


http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?
itemCode=PM10&dataGubun=DAILY
&searchCondition=MONTH
&pageNo=1
&numOfRows=10
&ServiceKey=서비스키
"""

getCtprvnMesureList = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst"


def make_url_getCtprvnMesureList(itemCode, dataGubun, searchCondition = 'WEEK'):
    return "%s?serviceKey=%s&itemCode=%s&dataGubun=%s&searchCondition=%s&_returnType=json" % (getCtprvnMesureList, API_AUTH_KEY, itemCode, dataGubun, searchCondition)


target_url = make_url_getCtprvnMesureList('PM10', 'DAILY', 'WEEK')

with urllib.request.urlopen(target_url) as url:
    data = json.loads(url.read().decode(url.headers.get_content_charset()))
    
    sort_data = data['list'][::-1]

    in_date = []
    city_name = []
    city_air_contidion_data = []
    
    for city in list(sort_data[0]):
        if city not in "_returnType dataGubun dataTerm dataTime itemCode numOfRows pageNo resultCode resultMsg searchCondition serviceKey totalCount".split():
            city_name.append(city)

    for i in range(len(city_name)):
        city_air_contidion_data.append([])

    for sub_data in sort_data:
        in_date.append(sub_data['dataTime'][5:10])
        for city in list(city_name):
            city_air_contidion_data[city_name.index(city)].append(int(sub_data[city]))
            
    for i in range(0, len(city_name)):
        plt.plot(in_date, city_air_contidion_data[i], label=city_name[i])
    
    plt.title('PM10')
    plt.xlabel('date')
    plt.ylabel('value')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fancybox=True, shadow=True)
    plt.grid(True)

    plt.show()

    



    
        


