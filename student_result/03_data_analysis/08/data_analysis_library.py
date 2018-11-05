import csv
from sys import exit

file = "library_csv_data.csv"

# 과제용

print("Siri: Module CSV로 실행합니다!! \n")
try:  # 파일이 있는지를 확인해 주는지에 대한 여부
    f = open(file, encoding='cp949')
except FileNotFoundError:
    print("Siri: csv module로 읽을 파일이 없는데요!?!?")
    exit(0)
else:
    raw_data_csv = csv.reader(f)

for row in raw_data_csv:  # 속성 알아보기
    print("raw_data_csv: index(" + str(row), end="")
    print(")\n")
    break

borrow = 0
amount_of_book = 0
Max_book = 0
Book_location = {}

count = 0
cnt = 0
for row in raw_data_csv:
    if count == 0:
        count = 1
        continue

    cnt = cnt + 1  # 도서관 총 수

    borrow = int(row[16]) + borrow  # 빌릴수 있는 대출의 총합

    amount_of_book = int(row[12]) + amount_of_book  # 도서의 총합

    if int(row[12]) > Max_book:  # 최대 책 수량
        Max_book = int(row[12])

    try:
        Book_location[row[2]]
    except KeyError:
        Book_location.update({row[2]: 1})
    else:
        Book_location[row[2]] = Book_location[row[2]] + 1
"""
    if row[2] in Book_location.keys():  #도서관 존재 구 위치 
        Book_location[row[2]]=Book_location[row[2]]+1
        
    else:
        Book_location.update({row[2] : 1})
"""

print("평균 대출 수량: %d" % (borrow / cnt))
print("도서의 평균: %d" % (amount_of_book / cnt))
print("최대 도서 수량: %d\n" % (Max_book))
print("지역에 따른 도서관의 수")
print(Book_location)
