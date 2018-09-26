def decorator_function(original_function):
    def wrapper_function():
        print('%s 함수가 호출되기전 입니다.' % original_function.__name__)
        return original_function()

    return wrapper_function


def display_1():
    print('display_1 함수가 실행됐습니다.')


def display_2():
    print('display_2 함수가 실행됐습니다.')


display_1 = decorator_function(display_1)
display_2 = decorator_function(display_2)

display_1()
# 결과:
#   display_1 함수가 호출되기전 입니다.
#   display_1 함수가 실행됐습니다.
print()
display_2()
# 결과:
#   display_2 함수가 호출되기전 입니다.
#   display_2 함수가 실행됐습니다.
