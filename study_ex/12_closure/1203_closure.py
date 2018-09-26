def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()

print(my_func)
# 결과: <function outer_func.<locals>.inner_func at 0x10a294158>

my_func()
# 결과: Hi
