"""
Title   모듈과 패키지 | module and package
Author  kadragon
Date    2018.09.05
"""

import sys

i = 0
for lt in sys.path:
    print("%2d 순위 > %s" % (i, lt))
    i += 1
