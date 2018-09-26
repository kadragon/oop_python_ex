def decorator_function(original_function):
    def wrapper_function():
        print('%s 함수가 호출되기전 입니다.' % original_function.__name__)
        return original_function()

    return wrapper_function


@decorator_function
def display():
    print('display 함수가 실행됐습니다.')


@decorator_function
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


display()
print()
display_info('John', 25)
# TypeError: wrapper_function() takes 0 positional arguments but 2 were given
