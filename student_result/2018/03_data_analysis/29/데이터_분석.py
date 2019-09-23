import csv

try:  # file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
    # 청주    최대 풍속(m/s)    평균 증기압(hPa)    최고 해면기압(hPa)    최저 해면기압(hPa)    2017-09-18 ~ 2018-09-17 DATA csv
    f = open('20180918121819.csv', encoding='cp949')
except FileNotFoundError:
    print("No File...")
    exit(0)
else:
    data = csv.reader(f)

# 원하는 데이터 저장을 위한 변수 선언
final_max_wind_velocity = 0
max_wind_velocity = ''

final_max_vapor = 0
max_vapor = ''

final_max_sea_level_pressure = 0
max_sea_level_pressure = ''

final_min_sea_level_pressure = 10000
min_sea_level_pressure = ''

# 데이터 형태
# ['일시', '최대 풍속(m/s)', '평균 증기압(hPa)', '최고 해면기압(hPa)', '최저 해면기압(hPa)']
# ['2017-09-18', '3.1', '16.2', '1010', '1006']

for row in data:

    try:  # date, wind_velocity, vapor, high_pressure, low_pressure 에 실수형으로 저장을 시도해보고 빈칸이거나 문자 등 숫자가 아닌 경우, 잘못된 날짜의 경우 입력을 받지 않는다.
        date = row[0]
        wind_velocity = float(row[1])
        vapor = float(row[2])
        high_pressure = float(row[3])
        low_pressure = float(row[4])
    except ValueError or len(row) == 0 or row[0][0] not in ['1', '2'] or row[-1] == '':
        if date != '일시':
            print("[%s]의 셀에 오류가 있어 입력받지 않습니다" % (date))  # 입력되지 않은 셀을 알린다. 단, 첫 행의 '일시'는 제외
        date = ''
        wind_velocity = 0
        vapor = 0
        high_pressure = 0
        low_pressure = 10000
        continue
    # 최댓값보다 크거나 최솟값보다 작은 경우(case by case) 값을 갱신한다.
    if final_max_wind_velocity < wind_velocity:
        final_max_wind_velocity = wind_velocity
        max_wind_velocity = date

    if final_max_vapor < vapor:
        final_max_vapor = vapor
        max_vapor = date

    if final_max_sea_level_pressure < high_pressure:
        final_max_sea_level_pressure = high_pressure
        max_sea_level_pressure = date

    if final_min_sea_level_pressure > low_pressure:
        final_min_sea_level_pressure = low_pressure
        min_sea_level_pressure = date

print(""" 
∩∧_∧∩ 
(　･ω･) 
 /　　ﾉ 
 しーU""")
print("최대 풍속 \t [%s] %.02f" % (max_wind_velocity, final_max_wind_velocity))
print("최고 (평균)증기압 \t [%s] %.02f" % (max_vapor, final_max_vapor))
print("최고 해면기압 \t [%s] %.02f" % (max_sea_level_pressure, final_max_sea_level_pressure))
print("최소 해면기압 \t [%s] %.02f" % (min_sea_level_pressure, final_min_sea_level_pressure))
