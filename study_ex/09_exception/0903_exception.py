"""
Title   try, exception
Author  kadragon
Date    2018.09.15
"""

import time

total = 0

try:
    while total < 5:
        print("doing something")
        total += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("exception...")
else:
    print("no exception...")

print("Next...")
