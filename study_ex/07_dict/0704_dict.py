"""
Title   사전 타입 | dictionary
Author  kadragon
Date    2018.09.08
"""

popul_dict = {'China': 1367485388, 'India': 1251695584, 'Indonesia': 321368864, 'America': 513949445,
              'Brazil': 255993674}
print(popul_dict['China'])
# 결과: 1367485388

popul_dict['China'] = 1367000000
print(popul_dict['China'])
# 결과: 1367000000
