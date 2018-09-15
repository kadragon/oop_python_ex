"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

import sys
import time

try:
    f = open('song.txt', 'r')
except FileNotFoundError:
    print('no file')
    sys.exit(0)

else:
    try:
        for line in f:
            if 'end' in line:
                raise SystemExit
            print(line, end='')
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        print("file close")
        f.close()
