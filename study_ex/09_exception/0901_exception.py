"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

# f = open('h.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'h.txt'

try:
    f = open('HelloPython.txt', 'r')
except FileNotFoundError:
    print('No file')

print('Next Code...')

"""
출력결과:
No file
Next Code...
"""
