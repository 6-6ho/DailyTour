import re
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import pandas as pd
import random

random_sleep_time = random.uniform(4, 6)
main_url = 'https://www.tripadvisor.co.kr/'
input_path = '../Data/Region_Data/region_data_for_attr_picture.json'
ATTR_MAX = 15
not_img = []
not_reviews = []

def load_json_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def controller():
    countries_info = load_json_data(input_path)
    
    for country_info in countries_info:
        country = country_info['country']
        regions = country_info['regions']
        country_crawler(country, regions)
    

def country_crawler(country, regions):
    # 메인 페이지 들어가기
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    ]
    
    country_img_path = pd.DataFrame(columns=["ATTR_NAME", "IMG_PATH", "TOTAL_REVIEWS"]) 
    user_agent = random.choice(user_agents)
    
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    sleep(2)
    
    for region in regions:
        driver.get(main_url)
        driver.implicitly_wait(5)
        sleep(random_sleep_time*2)
        
        # 지역 검색창에 입력 후 엔터
        input_text = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[4]/div/div/div[2]/div/form/div/div/input')
        input_text.send_keys(region)
        sleep(random_sleep_time)
        input_text.send_keys(Keys.ENTER)
        sleep(random_sleep_time)
        
        # 즐길거리 클릭
        try:
            driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[4]/a').click()
            driver.implicitly_wait(5)
            sleep(random_sleep_time)
        except:
            print('not exist search-filter')
            continue

        
        # 뷰숲
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        attr_hrefs = []
        a_tags = soup.select('div.rating-review-count > div > a')
        
        for tag in a_tags:
            attr_hrefs.append(tag['href'])
            
        sleep(3)
        
        # 중복 제거 처리
        seen = set()
        attr_hrefs_no_duplicates = []
        for href in attr_hrefs:
            if href not in seen:
                seen.add(href)
                attr_hrefs_no_duplicates.append(href)

        attr_hrefs = attr_hrefs_no_duplicates[:ATTR_MAX]
        
        print(len(attr_hrefs))
        
        # 관광지 5개 마다 광고 1개씩 12345, 7891011, 1314151617 이런 형태
        to_remove = []

        for i in range(1, len(attr_hrefs) + 1):
            if i not in (7, 13):
                xpath = f'/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[3]/div[1]'
                region_data = driver.find_element(By.XPATH, xpath).text
                if region not in region_data:
                    if i > 7:
                        to_remove.append(i-1)
                    elif i > 13:
                        to_remove.append(i-2)

        # 제거할 인덱스 리스트를 역순으로 정렬
        to_remove.sort(reverse=True)
        
        for index in to_remove:
            attr_hrefs.pop(index - 1)                
            
        print(len(attr_hrefs))
                
        for i in range(min(ATTR_MAX, len(attr_hrefs))):
            driver.get(f"{main_url}{attr_hrefs[i]}")
            driver.implicitly_wait(5)
            sleep(random_sleep_time)
            
            # 관광지 이름        
            attr_name = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]').text.lstrip()
            driver.implicitly_wait(5)
            sleep(random_sleep_time)
            
            # 관광지 사진 링크
            xpath = '/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/ul/li[1]/div/picture/img'
            try:
                attr_picture_path = driver.find_element(By.XPATH, xpath).get_attribute("src")
            except NoSuchElementException:
                not_img.append(attr_name)
                attr_picture_path = None

            # 총 리뷰 수
            review_xpath ='/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[7]/div/div/div/section/section/div[1]/div/div[3]/div[1]/div/div[1]/div[2]/span'
            try:
                reviews = driver.find_element(By.XPATH, review_xpath).text
                reviews = re.findall(r'\d+', reviews)
                reviews = int(''.join(reviews))
            except NoSuchElementException:
                not_reviews.append(attr_name)
                reviews = 0
                
            print(f'attr name : {attr_name}, picture_path = {attr_picture_path}, reviews = {reviews}')
            new_row = pd.DataFrame([[attr_name, attr_picture_path, reviews]], columns = ["ATTR_NAME", "IMG_PATH", "TOTAL_REVIEWS"])
            
            country_img_path = pd.concat([country_img_path, new_row], ignore_index=True)
                
            sleep(random_sleep_time)
    
    csv_output_path = f'../Data/picture-data/attr/{country}_img_path_reviews.csv'
    country_img_path.to_csv(csv_output_path, index=False, encoding='utf-8')

    sleep(5)
    
if __name__=='__main__':
    controller()
    print("not reviews")
    print(not_reviews)
    print("not imgs")
    print(not_img)
        