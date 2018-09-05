"""
Title   모듈과 패키지 | module and package
Author  kadragon
Date    2018.09.05
"""

import phone_mod
import camera_mod


def smart_on():
    while True:
        choice = input('What do you want? (0~2) :')
        if choice == '0':
            break
        elif choice == '1':
            camera_mod.photo()
        elif choice == '2':
            phone_mod.make_call()
        elif choice == '3':
            print("차후 구현")


# if __name__ == '__main__':
if __name__ == 'builtins':
    smart_on()
