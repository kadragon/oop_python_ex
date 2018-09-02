"""
Title   시퀀스 타입 | sequence type | tuple 12
Author  kadragon
Date    2018.09.02
"""

from collections import namedtuple

book_info = namedtuple('struct_book_info', ['author', 'title'])

my_book = book_info('hyun', 'gop')
print(my_book)
# 결과: struct_book_info(author='hyun', title='gop')

print(my_book[0])
print(my_book.author)
# 결과: hyun

print(my_book[1])
print(my_book.title)
# 결과: gop
