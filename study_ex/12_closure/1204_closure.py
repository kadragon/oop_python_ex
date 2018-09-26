def outer_func(tag):
    text = 'Some text'
    tag = tag

    def inner_func():
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_func


h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func()
# 결과: <h1>Some text<h1>
p_func()
# 결과: <p>Some text<p>

func = {'h1': outer_func('h1')}
func['h1']()
# 결과: <h1>Some text<h1>
