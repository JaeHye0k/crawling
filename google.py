from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def web_crawling(keyword_list,break_count = 0):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    for keyword in keyword_list:
        elem = driver.find_element_by_name("q")  # 검색창 Focus
        elem.clear()
        elem.send_keys(keyword) # 검색 키워드 입력
        elem.send_keys(Keys.RETURN) # 엔터키
        SCROLL_PAUSE_TIME = 1
        path = "C:/Users/이재혁/PycharmProjects/crawling/downloads/"+keyword+"/"

        # Get scroll height (scroll down with infinite loading)
        last_height = driver.execute_script("return document.body.scrollHeight") # 브라우저의 높이

        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 브라우저 끝까지 스크롤을 내림
        #
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME) # 로딩을 기다림
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height: # 스크롤을 내렸을때 나오는게 없으니까 높이가 같음
        #         try:
        #             driver.find_element_by_class_name("mye4qd").click() # 결과 더보기 클릭
        #         except:
        #             break
        #     last_height = new_height

        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # 이미지 리스트
        count = 1
        for image in images:
            if count == break_count: break
            try:
                image.click()
                time.sleep(1) # 이미지로딩을 기다림
                imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src") # 이미지 src를 불러옴
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent',
                                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)
                if not os.path.exists(path):
                    os.makedirs(path)
                urllib.request.urlretrieve(imgUrl, path + str(count)+".jpg")
                count += 1
            except:
                pass # 오류가 났을때 그냥 다음으로 넘어감

    driver.close() # 웹 브라우저를 닫아줌


if __name__ == '__main__':
    keyword_list = [""] # 이곳에 크롤링 할 키워드를 적음
    break_count = int(input('사진을 몇장 다운로드 받으시겠습니까?: '))
    web_crawling(keyword_list,break_count)