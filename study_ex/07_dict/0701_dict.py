"""
Title   사전 타입 | dictionary
Author  kadragon
Date    2018.09.08
"""

"""
마치 영한사전에서 영어단어와 그 뜻이 연결되어 하나의 항목을 이루는 것처럼.
key 와 이에 연결되는 value 가 하나의 항목을 이룸.
"""

popul_list = [['China', 1367485388], ['India', 1251695584], ['America', 513949445], ['Indonesia', 321368864],
              ['Brazil', 255993674]]

for i in popul_list:
    if i[0] == 'India':
        print(i[1])

popul_dict = {'China': 1367485388, 'India': 1251695584, 'Indonesia': 321368864, 'America': 513949445,
              'Brazil': 255993674}

print(popul_dict['India'])
