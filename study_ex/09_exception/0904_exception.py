"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

dic = {'apple': 2, 'banana': 10, 'fine': 5}

# if 를 활용한 데이터 확인 방법
dic_list = dict(dic)

data = input('>')
if data in dic_list:
    print("{}: {}개".format(data, dic[data]))
else:
    print('There is no data.')

# try except else 를 이용한 방법
while True:
    data = input('>')
    try:
        dic[data]
    except KeyError:
        print('There is no data.')
    else:
        print("{}: {}개".format(data, dic[data]))
    print("continue...")
