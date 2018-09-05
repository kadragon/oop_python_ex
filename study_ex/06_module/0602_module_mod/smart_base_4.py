"""
Title   모듈과 패키지 | module and package
Author  kadragon
Date    2018.09.05
"""

import phone_base
import camera_base

print("smart.py's module name is", __name__)
print("=" * 50)

while True:
    choice = input('What do you want? (0~2) :')
    if choice == '0':
        break
    elif choice == '1':
        camera_base.photo()
    elif choice == '2':
        phone_base.make_call()
    elif choice == '3':
        print("차후 구현")
