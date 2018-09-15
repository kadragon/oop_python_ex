"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

import sys

try:
    f = open('HelloPython.txt', 'r')
except FileNotFoundError:
    print('No file')
    sys.exit(0)
    # raise SystemExit

print('Next Code...')

"""
출력 결과: No file
"""
