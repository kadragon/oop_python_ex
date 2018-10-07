# https://code.sasa.hs.kr/problem.php?id=2185


def de_func(or_func):
    def we_func():
        print('=' * 14)
        print('function debug')
        print('=' * 14)
        return or_func()

    return we_func


def print_sasa():
    print("SASA")


@de_func
def print_python():
    print("Python")


print_sasa()
print_python()
