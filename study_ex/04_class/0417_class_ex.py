"""
Title   클래스 | Class | 16
Author  kadragon
Date    2018.08.28
"""

var = 77


class what():
    var = 100

    def print_var(self):
        print(var)

    def print_var_other(self):
        print(self.var)


what_A = what()
what_A.print_var()
what_A.print_var_other()
