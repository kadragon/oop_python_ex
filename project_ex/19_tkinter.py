from tkinter import *

window = Tk()
window.title('Calculator')
# window.geometry("640x400+100+100")
window.resizable(False, False)

first, second = 0, 0
str_value = StringVar()
operator = 0


def tk_button_maker(text: str, column: int, row: int, colspan=1, rowspan=1, lambda_function=None):
    global window
    return Button(window, text=text, command=lambda_function).grid(column=column, row=row, columnspan=colspan, rowspan=rowspan, sticky="nsew")


def number_click(number=0):
    global first, second, str_value, operator
    if operator == 0:
        if str_value.get() == '0':
            str_value.set(str(number))
            first = number
        else:
            first *= 10
            first += number
            str_value.set(str(first))
    else:
        if str_value.get() == '0' or second == 0:
            str_value.set(str(number))
            second = number
        else:
            second *= 10
            second += number
            str_value.set(str(second))


def clear():
    global first, str_value
    first = 0
    str_value.set('0')


def operator_click(op):
    global operator
    op_list = '+-*/'
    operator = op_list.find(op) + 1


def calculate():
    global first, second, operator
    if operator == 1:
        first += second
    elif operator == 2:
        first -= second
    elif operator == 3:
        first *= second
    elif operator == 4:
        first /= second

    str_value.set(first)
    second = 0
    operator = 0


button_d = {
    ('7', 0, 1, 1, 1, lambda: number_click(7)),
    ('8', 1, 1, 1, 1, lambda: number_click(8)),
    ('9', 2, 1, 1, 1, lambda: number_click(9)),
    ('C', 3, 1, 2, 1, lambda: clear()),
    ('4', 0, 2, 1, 1, lambda: number_click(4)),
    ('5', 1, 2, 1, 1, lambda: number_click(5)),
    ('6', 2, 2, 1, 1, lambda: number_click(6)),
    ('*', 3, 2, 1, 1, lambda: operator_click('*')),
    ('/', 4, 2, 1, 1, lambda: operator_click('/')),
    ('1', 0, 3, 1, 1, lambda: number_click(1)),
    ('2', 1, 3, 1, 1, lambda: number_click(2)),
    ('3', 2, 3, 1, 1, lambda: number_click(3)),
    ('+', 3, 3, 1, 2, lambda: operator_click('+')),
    ('-', 4, 3, 1, 1, lambda: operator_click('-')),
    ('0', 0, 4, 2, 1, lambda: number_click(0)),
    ('.', 2, 4, 1, 1, lambda: None),
    ('=', 4, 4, 1, 1, lambda: calculate()),
}

for text, col, row, colspan, rowspan, lambda_function in button_d:
    tk_button_maker(text, col, row, colspan, rowspan, lambda_function)

for i in range(5):
    Grid.rowconfigure(window, i, weight=i)
    Grid.columnconfigure(window, i, weight=i)

str_value.set(str(first))
display = Entry(window, textvariable=str_value, justify='right').grid(columnspan=5, row=0)

window.mainloop()
