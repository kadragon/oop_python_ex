"""
Title   사전 타입 | dictionary
Author  kadragon
Date    2018.09.08
"""

popul_dict = {'China': 1367485388, 'India': 1251695584, 'Indonesia': 321368864, 'America': 513949445,
              'Brazil': 255993674}
print(list(popul_dict))
# 결과: ['China', 'India', 'Indonesia', 'America', 'Brazil']

popul_list = [['China', 1367485388], ['India', 1251695584], ['America', 513949445], ['Indonesia', 321368864],
              ['Brazil', 255993674]]
popul_convert_dict = dict(popul_dict)
print(popul_convert_dict)
# 결과: {'China': 1367485388, 'India': 1251695584, ...

test = ['ab', 'cd']
print(dict(test))
# 결과: {'a': 'b', 'c': 'd'}
