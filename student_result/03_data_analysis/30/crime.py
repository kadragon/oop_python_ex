import csv

from sys import exit

try:
    # csv 파일을 연다.
    f = open('crimedata.csv', 'r', encoding='cp949')
    # 만약 예외가 발생한다면,
except Exception as ex:
    # 예외 메세지를 출력하고 종료한다.
    print(str(ex))
    exit(0)

# csv를 읽어올 수 있도록 준비한다.
data = csv.reader(f)

crimedict = {}
crimenums_type = {}
citynames = []
crimenames = []
hardcrimenames = []
linenum = 1

# csv 파일로 부터 한 줄씩 읽어온다.
for row in data:
    # indexcut: 줄에서 도시별 범죄가 나와있는 부분만 잘라낸 것.
    indexcut = row[3:]
    # 만약 첫번째 줄이라면
    if linenum == 1:
        # 줄에서 도시 이름을 하나씩 가져와서,
        for cities in indexcut:
            # citynames에 추가한다.
            citynames.append(cities)
            # crimedict에 도시 이름을 키로 하여 새로운 dict를 만든다.
            crimedict[cities] = {}
    else:
        # 범죄의 이름을 crimenames에 추가한다.
        crimenames.append(row[1])
        # 만약 범죄 유형이 강력범죄라면,
        if row[0] == '강력범죄':
            # 범죄의 이름을 hardcrimenames에 추가한다.
            hardcrimenames.append(row[1])
            # citynames에서 각각의 도시 이름을 가져온다.
        for i in range(len(citynames)):
            # 횟수를 가져오되, csv 파일 내에서 천단위를 구분하기 위해 넣은 콤마를 없앤다.
            num = indexcut[i].replace(',', '')
            # crimedict에 각 도시별로 범죄유형과 해당 유형 범죄의 횟수를 추가한다. -로 표시된 것은 0회에 해당하는 것이다.
            crimedict[citynames[i]][row[1]] = int(
                num if num.isdecimal() else 0)
    # 줄 번호를 1 늘린다.
    linenum += 1

totalcrime = 0
totalcrimemax = -1
totalcrimemin = 500000
maxname = None
minname = None

# crimenums_type: 범죄 유형별 횟수를 세기 위한 dict.
for name in crimenames:
    crimenums_type[name] = 0

# 각각의 도시에 대해,
for c in citynames:
    # crimedict에서 범죄 유형 데이터를 가져온다.
    dat = crimedict[c]
    # 그 중 값(범죄 횟수)만 가져온다.
    crimenums_city = list(dat.values())
    crime_city = 0

    for i in range(len(crimenums_city)):
        # crime_city: 각 도시별 일어난 범죄 횟수의 합
        crime_city += crimenums_city[i]
        # 각 도시에서 일어난 범죄 횟수를 다시 범죄 유형별로 정리하고 합산한다.
        crimenums_type[crimenames[i]] += crimenums_city[i]
        # 만약 그 도시에서 일어난 범죄 횟수가 최대/최소 값이라면, 도시 이름과 최대/최소 횟수를 갱신한다.
    if crime_city > totalcrimemax:
        totalcrimemax = crime_city
        maxname = c
    if crime_city < totalcrimemin:
        totalcrimemin = crime_city
        minname = c
    # totalcrime: 일어난 총 범죄 횟수
    totalcrime += crime_city

hardcrime = 0

for crimenames in hardcrimenames:
    # 범죄 유형 중 강력범죄가 일어난 횟수만 합산한다(hardcrimes).
    hardcrime += crimenums_type[crimenames]

try:
    # 최대/최소 값과 도시 이름 출력
    print('범죄가 가장 많은 지역은 {} 이고, 횟수는 {}회 입니다.'.format(maxname, totalcrimemax))
    print('범죄가 가장 적은 지역은 {} 이고, 횟수는 {}회 입니다.'.format(minname, totalcrimemin))
    # 도시 별 평균 범죄 횟수는 전체 범죄 횟수를 도시 수로 나눈 것이다.
    print('지역 당 평균 범죄 횟수는 %.02f회 입니다.' % (float(totalcrime) / len(citynames)))
    # 강력 범죄의 비율은 강력 범죄 횟수를 전체 범죄 횟수로 나눈 것이다.
    print('전체 범죄 중 강력범죄의 비율은 %.02f%% 입니다.' %
          (float(hardcrime) / totalcrime * 100))
# 만약 0으로 나누는 에러가 발생하는 경우
except ZeroDivisionError as err:
    # 에러메세지를 출력하고 종료한다.
    print('0으로 나눌 수 없습니다!')
    exit(0)
