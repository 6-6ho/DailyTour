from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import pandas as pd

driver = webdriver.Chrome()
main_url = 'https://www.tripadvisor.co.kr/'
input_path = '../Data/Region_Data/region_data_copy.json'
ATTR_MAX = 15
not_img = []

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
        
    driver.quit()
    

def country_crawler(country, regions):
    # 메인 페이지 들어가기
    country_img_path = pd.DataFrame(columns=["ATTR_NAME", "IMG_PATH"]) 
    
    for region in regions:
        driver.get(main_url)
        driver.implicitly_wait(5)
        sleep(2)
        
        # 지역 검색창에 입력 후 엔터
        input_text = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[4]/div/div/div[2]/div/form/div/div/input')
        input_text.send_keys(region)
        input_text.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)
        sleep(5)
        
        # 즐길거리 클릭
        try:
            driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[4]/a').click()
            driver.implicitly_wait(5)
            sleep(5)
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
            adjusted_index = i + (i - 1) // 5
            xpath = f'/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[{adjusted_index}]/div/div/div/div[2]/div[1]/div[3]/div[1]'
            region_data = driver.find_element(By.XPATH, xpath).text
            if region not in region_data:
                to_remove.append(i)

        # 제거할 인덱스 리스트를 역순으로 정렬
        to_remove.sort(reverse=True)
        
        for index in to_remove:
            attr_hrefs.pop(index - 1)                
            
        print(len(attr_hrefs))
                
        for i in range(min(ATTR_MAX, len(attr_hrefs))):
            driver.get(f"{main_url}{attr_hrefs[i]}")
            driver.implicitly_wait(5)
            sleep(5)
            
            # 관광지 이름        
            attr_name = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]').text.lstrip()
            driver.implicitly_wait(5)
            sleep(5)
            
            # 관광지 사진 링크
            xpath = '/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/ul/li[1]/div/picture/img'
            try:
                attr_picture_path = driver.find_element(By.XPATH, xpath).get_attribute("src")
            except NoSuchElementException:
                not_img.append(attr_name)
                attr_picture_path = None
                
            print(f'attr name : {attr_name}, picture_path = {attr_picture_path}')
            new_row = pd.DataFrame([[attr_name, attr_picture_path]], columns = ["ATTR_NAME", "IMG_PATH"])
            
            country_img_path = pd.concat([country_img_path, new_row], ignore_index=True)
                
            sleep(3)
    
    csv_output_path = f'../Data/picture-data/attr/{country}_img_path.csv'
    country_img_path.to_csv(csv_output_path, index=False, encoding='utf-8')
    
if __name__=='__main__':
    controller()
        