import requests
from bs4 import BeautifulSoup as bs

print('''다음 프로그램은 아두이노의 해더파일에 해당하는 함수를 알려주는 프로그램입니다!
''')

arduino = bs(requests.Session().get('https://www.arduino.cc/en/Reference/Libraries').text, 'html.parser')

libraries = arduino.select('div#wikitext ul li a.wikilink')

#print(libraries)

library_add = []
library_name = []

for i in libraries:
    library_add.append(i.get('href').lstrip('https:'))
    library_name.append(i.getText().strip())

'''
for i in library_name:
    print(i)
'''


for i in library_add :
    if 'www' in i :
        header = bs(requests.Session().get('https:'+i).text, 'html.parser')
        functions = header.select('a.wikilink')
        function = []
        print('='*50)
        print('< https:%s >' %i)
        for j in functions:
            function.append(j.getText())
        for j in function:
            if '()' in j or '[]' in j:
                print(j)

