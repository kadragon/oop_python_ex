"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

while True:
    try:
        data = input('>')
        print(10 / int(data))
    except (ZeroDivisionError, ValueError, KeyboardInterrupt) as e:
        print(e)
        if isinstance(e, KeyboardInterrupt):
            print('KeyboardInterrupt')
            break

print('Bye~')
