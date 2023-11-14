from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import json

csv_path = 'OutBound_Data/Outbound_10Y_data.csv'

# 올바른 함수 이름은 read_csv 입니다. read_scv는 오타입니다.
df = pd.read_csv(csv_path)

country_list = [country for country in df.columns[1:] if country not in ['사이판', '괌']]

print(country_list)

driver = webdriver.Chrome()

def crawler():
    driver.get('https://kr.trip.com/?locale=ko-kr')
    driver.implicitly_wait(10)
    # 각 나라별로 데이터를 저장할 딕셔너리 생성
    country_data = {}
    
    for country in country_list:
        input_text = driver.find_element(By.ID, "hotels-destination")
        input_text.send_keys(Keys.CONTROL, 'a')
        input_text.send_keys(Keys.DELETE)
        driver.implicitly_wait(5)
        input_text.send_keys(country)
        driver.implicitly_wait(5)
        sleep(1)
        
        target_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/ul/li[1]/div/div[2]/div[2]/div[2]")
        driver.implicitly_wait(5)
        
        # 현재 나라에 대한 데이터를 저장할 리스트 초기화
        regions = []
        
        for target in target_list:
            regions.extend(target.text.split('\n'))
            print(target.text)
        
        # 딕셔너리에 현재 나라와 크롤링한 데이터 저장
        country_data[country] = regions
        driver.implicitly_wait(5)
        sleep(2)
    
    driver.quit()
    
    # JSON 파일로 데이터 저장
    with open('country_data.json', 'w', encoding='utf-8') as f:
        json.dump(country_data, f, ensure_ascii=False, indent=4)
    
if __name__=='__main__':
    crawler()