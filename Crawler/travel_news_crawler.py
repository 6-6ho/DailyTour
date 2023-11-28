import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json

# 브라우저 꺼짐 방지 옵션 설정 및 driver 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def get_travel_news_url() :
    url_list = []

    for page in range(1, 6) : 
        URL = 'https://www.traveltimes.co.kr/news/articleList.html?page=' + str(page)  + '&total=84&box_idxno=&sc_sub_section_code=S2N43&view_type=sm'
        driver.get(URL) #페이지 접속

        time.sleep(1)

        html = driver.page_source 
        soup = BeautifulSoup(html, 'html.parser')

        li_tags = soup.select('#section-list > ul > li')
        
        for li in li_tags:
            a = li.find('a', class_='thumb')
            url_list.append('https://www.traveltimes.co.kr/' + a['href'])
        
    return url_list 

def travel_news_crawling(url_list):
    news_list = [] 
    for url in url_list :
        driver.get(url) #페이지 접속

        time.sleep(2)

        html = driver.page_source 
        soup = BeautifulSoup(html, 'html.parser')

        news_title = soup.find('h3', class_='heading').text

        article_body = soup.find('article', id='article-view-content-div')
        p_list = article_body.find_all('p')

        news_content = ''
        for p in p_list :
            news_content += p.text

        print(news_content)

        parse_to_json(news_title, news_content, news_list)
    
    
    save_to_json(news_list)


def parse_to_json(news_title, news_content, news_list):
    news_list.append({
        'news_title' : news_title,
        'news_content' : news_content
    })



# 크롤링 데이터 json으로 저장
def save_to_json(news_list):
    with open('travel_news.json', 'w', encoding='utf-8') as file :
        json.dump({'travel_news' : news_list}, file, ensure_ascii=False, indent=4)


def main():
    url_list = get_travel_news_url()
    travel_news_crawling(url_list)



if __name__ == '__main__' :
    main()