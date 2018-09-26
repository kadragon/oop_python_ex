def outer_func(tag):
    tag = tag

    def inner_func(txt):
        print('<{0}>{1}<{0}>'.format(tag, txt))

    return inner_func


h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func('h1태그의 안입니다.')
# 결과: <h1>h1태그의 안입니다.<h1>
h1_func('h1태그 재활용!')
# 결과: <h1>h1태그 재활용!<h1>
p_func('p태그의 안입니다.')
# 결과: <p>p태그의 안입니다.<p>
