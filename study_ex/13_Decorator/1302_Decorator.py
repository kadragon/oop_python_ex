def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print('display 함수가 실행됐습니다.')


decorated_display = decorator_function(display)

decorated_display()
# 결과: display 함수가 실행됐습니다.
