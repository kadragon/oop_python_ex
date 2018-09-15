import csv

# file 을 열기 위해서 시도해보고, 없으면 알려주고 있으면 data 로 변경
try:
    # 청주 온도 19040101~20180824 DATA csv
    f = open('09_csv_temp_history.csv', encoding='cp949')
except FileNotFoundError:
    print("파일이 없는데요?!")
    exit(0)
else:
    data = csv.reader(f)

# 원하는 데이터 저장을 위한 변수 선언
max_temp = 0
max_date = ''
max_temp_list = []

min_temp = 0
min_date = ''
min_temp_list = []

diff_temp = 0
diff_date = ''
diff_temp_list = []

# 데이터 형태
# ['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
# ['1967-01-01', '131', '-2.9', '-8', '0.3']

for row in data:
    # 온도 데이터가 아니거나, 잘못된 값이 들어가 있거나, 컬럼을 제외하기 위해
    if len(row) == 0 or row[0][0] not in ['1', '2'] or row[-1] == '':
        continue

    if max_temp < float(row[-1]):
        max_temp = float(row[-1])
        max_date = row[0]

    if min_temp > float(row[-1]):
        min_temp = float(row[-3])
        min_date = row[0]

    if diff_temp < float(row[-1]) - float(row[-3]):
        diff_temp = float(row[-1]) - float(row[-3])
        diff_date = row[0]

print("MAX  TEMP \t [%s] %.02f" % (max_date, max_temp))
print("MIN  TEMP \t [%s] %.02f" % (min_date, min_temp))
print("DIFF TEMP \t [%s] %.02f" % (diff_date, diff_temp))
