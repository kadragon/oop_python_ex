import bs4
from selenium import webdriver

driver = webdriver.PhantomJS('/Users/kadragon/Dev/oop_python_ex/project_ex/14_phantomjs')
driver.implicitly_wait(1)

driver.get('http://living.sivillage.com/jaju/display/displayCategory?dspCatNo=010000000081&upDspCatNo=010000000007&chnSct=P')

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

img = soup.select('div.subject p')

for i in img:
    print(i.getText())