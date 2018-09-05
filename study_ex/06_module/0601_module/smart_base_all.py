"""
Title   모듈과 패키지 | module and package
Author  kadragon
Date    2018.09.05
"""


def photo():
    print("Take a photo")


def make_call():
    print("Make a Call")


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
