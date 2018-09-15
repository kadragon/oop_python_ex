"""
Title   file
Author  kadragon
Date    2018.09.15
"""

import pickle

f = open('pickle', 'wb')
my_list = ['test', 'pickle', 1, 2, 3, 4]
pickle.dump(my_list, f)
f.close()

f = open('pickle', 'rb')
print(pickle.load(f))
