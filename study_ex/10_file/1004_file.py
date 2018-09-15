"""
Title   file
Author  kadragon
Date    2018.09.15
"""

f = open('string.txt', 'r')
for line in f:
    print(line, end='')
f.close()

print()

f = open('string.txt', 'r')
for line in f:
    print(line.strip())
f.close()

print()

with open('string.txt') as f:
    print(f.readlines())
