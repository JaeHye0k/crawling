from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import threading

driver = webdriver.Chrome() # 크롬 드라이버가 다른곳에 위치하면 괄호안에 크롬 드라이버의 위치를 적어줌
driver.implicitly_wait(3)
driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

def crawling(second = 1.0):
    f = open('네이버검색어순위.txt', 'a')
    f.write(datetime.today().strftime('\n'+"______________"+'\n'+"%Y/%m/%d %H:%M:%S")+'\n')
    i = 1
    for anchor in soup.select("span.item_title"):
        data = str(i) + "위: "+ anchor.get_text() + '\n'
        f.write(data)
        i += 1
    f.close()
    # threading.Timer(second, crawling, [second]).start() second초마다 crawling 함수 실행

crawling()