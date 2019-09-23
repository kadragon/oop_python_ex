import csv  # csv 파일 처리
import continent as cont  # 대륙 정보 관련(자작)
from sys import exit  # 프로그램 종료


def dict_initialize(d=dict()):
    """
    딕셔너리를 받아 초기화해줍니다. 만일 인자가 없으면 새로운 딕셔너리를 만들어 반환합니다. 
    :parameter d: 초기화하고자 하는 딕셔너리입니다. 없으면 빈 딕셔너리가 default로 설정됩니다. 
    :return: 딕셔너리 d가 초기화된 채로 반환됩니다. 
    """
    d = {"asia": 0, "africa": 0, "america": 0, "europe": 0, "oceania": 0}  # 초기화
    return d  # 딕셔너리 반환


def rank(d):
    """
    딕셔너리를 받아 value의 순위별로 키를 나열합니다.
    :parameter d: 순위를 알고자 하는 딕셔너리입니다.
    :return: 리스트를 반환합니다. d에서 value가 클수록 key가 앞에 옵니다. 
    """
    rank_list = []  # 순위 리스트
    values = list(d.values())  # d에서 value만 추출한 뒤 list로
    values.sort(reverse=True)  # value를 정렬(내림차순)
    keys = d.keys()

    for i in range(len(d)):
        for j in keys:
            if d[j] == values[i]:
                rank_list.append(j)  # 순위 리스트에 가장 큰 대륙부터 삽입
                break

    return rank_list


def average(d):
    """
    대륙이 key이고 변량의 합이 value인 딕셔너리를 받아 value를 key에 속한 국가로 나누어 반환합니다.
    :parameter d: key별 평균 value를 구하고자 하는 딕셔너리입니다. 
    :return: d에 속한 key는 그대로 두고, value는 평균을 내어 업데이트한 딕셔너리를 반환합니다. 
    """
    average_dict = dict()  # 평균값 딕셔너리
    keys = list(d.keys())
    values = list(d.values())

    for i in keys:
        for j in values:
            if j == d[i]:
                break
        average_dict[i] = round(j / cont.num_of_country(i))  # 평균값과 키를 매칭시켜 삽입

    return average_dict


# 분석 데이터: 국가별 수산물 수입/수출 정보
# 국가별로 나뉘어져 있는 데이터를 대륙별로 합산하고 평균을 내어 비교
# 파일을 열어본다. 존재하지 않으면 예외를 통해 프로그램 종료. 
try:
    f = open("./01.csv", encoding="cp949")
except FileNotFoundError:  # 파일이 존재하지 않음
    print("파일이 존재하지 않습니다.")
    exit(1)  # 프로그램 종료
else:  # 파일이 존재하여 성공적으로 열어봄
    data = csv.reader(f)

row_cnt = 0
export_weight = dict_initialize()  # 대륙별 수출 중량
export_money = dict_initialize()  # 대륙별 수출 액수
import_weight = dict_initialize()  # 대륙별 수입 중량
import_money = dict_initialize()  # 대륙별 수입 액수

for row in data:
    row_cnt += 1
    """
    첫 줄과 둘째 줄만 출력하여 데이터가 어떻게 들어있는지 파악하는 부분
    지금은 굳이 필요 없는 부분
    if row_cnt<=2:
        print(row)
        # 첫번재 줄은 분석에 활용하지 않음
        if row_cnt==1:
            continue
    """
    continent_belonged = cont.get_where_continent(row[1].upper().strip().replace("'", ""))  # 그 나라가 속한 대륙
    # print("{} {}".format(row[1], continent_belonged)) - 확인용

    try:
        if (row[2] == "'E'"):  # 수출 통계
            export_weight[continent_belonged] += int(row[6].replace("'", ""))
            export_money[continent_belonged] += int(row[7].replace("'", ""))
        else:  # 수입 통계
            import_weight[continent_belonged] += int(row[6].replace("'", ""))
            import_money[continent_belonged] += int(row[7].replace("'", ""))
    except KeyError:  # 범례와 기타국만 걸러냄
        print(row_cnt, row)

# 이 아래는 도출해낸 데이터를 출력하는 부분입니다. 

print("2018년 05월 기준의 대륙별 수산물 수출입 통계입니다. ")
print("=" * 100)
print("대륙별 수출 중량:", export_weight)  # 데이터 도출 1-1: 대륙별 수출 중량
print("순위:", rank(export_weight))  # 데이터 도출 1-2: 순위
print("평균:", average(export_weight))  # 데이터 도출 1-3: 대륙별 수출 중량 평균(국가 수로 나눔)
print("순위:", rank(average(export_weight)))  # 데이터 도출 1-4: 평균의 순위
print("=" * 100)
print("대륙별 수출 액수:", export_money)  # 데이터 도출 2-1: 대륙별 수출 액수
print("순위:", rank(export_money))  # 데이터 도출 2-2: 순위
print("평균:", average(export_money))  # 데이터 도출 2-3: 대륙별 수출 액수 평균(국가 수로 나눔)
print("순위:", rank(average(export_money)))  # 데이터 도출 2-4: 평균의 순위
print("=" * 100)
print("대륙별 수입 중량:", import_weight)  # 데이터 도출 3-1: 대륙별 수입 중량
print("순위:", rank(import_weight))  # 데이터 도출 3-2: 순위
print("평균:", average(import_weight))  # 데이터 도출 3-3: 대륙별 수입 중량 평균(국가 수로 나눔)
print("순위:", rank(average(import_weight)))  # 데이터 도출 3-4: 평균의 순위
print("=" * 100)
print("대륙별 수입 액수:", import_money)  # 데이터 도출 4-1: 대륙별 수입 액수
print("순위:", rank(import_money))  # 데이터 도출 4-2: 순위
print("평균:", average(import_money))  # 데이터 도출 4-3: 대륙별 수입 액수 평균(국가 수로 나눔)
print("순위:", rank(average(import_money)))  # 데이터 도출 4-4: 평균의 순위
print("=" * 100)
print("끝!")

# print(rank(export_money))
