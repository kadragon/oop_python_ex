"""
Title   file
Author  kadragon
Date    2018.09.15
"""

f = open('test.txt', 'w')
f.write('Python')
f.close()

f = open('test.txt', 'r')
string = f.read()
print(string)  # 출력 값: Python
f.close()

f = open('test.txt', 'a')
return_value = f.write(' is simple')
print(return_value)  # 출력 값: 10
f.close()

try:
    f = open('test.txt', 'x')
except FileExistsError:
    print('FileExistsError')
else:
    f.write('+_____+')
finally:
    f.close()

# 출력: FileExistsError
