from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
main_url = 'https://www.tripadvisor.co.kr/'
input_path = '../Data/Region_Data/region_data.json'

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
    
def save_to_json(country, data, type):
    if type.equals('train'):
        filename = f"{country}_attr_review_train.json"
    else:
        filename = f"{country}_attr_review_recent.json"
        
    filepath = f'../Data/Review_Data/Attr_Review/{filename}'
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    

def country_crawler(country, regions):
    train_data = []
    recent_data = []
    # 메인 페이지 들어가기
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
        driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[4]/a').click()
        driver.implicitly_wait(5)
        sleep(5)
        
        # 뷰숲
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # 현재 지역의 관광지 링크 따기 &rf=n&ssrc=A&o=(n-1)*30 패턴인데 관광지의 개수 생각해서 코드 변경해야 함
        attr_hrefs = []
        a_tags = soup.select('div.rating-review-count > div > a')
        
        for tag in a_tags:
            attr_hrefs.append(tag['href'])
            
        sleep(3)
        
        attr_hrefs = list(set(attr_hrefs))
        print(attr_hrefs)
        print(len(attr_hrefs))
        
        for i in range(3):
            driver.get(f"{main_url}{attr_hrefs[i]}")
            driver.implicitly_wait(5)
            sleep(3)
            
            # 관광지 이름        
            attr_name = driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div/div[1]/div[1]').text
            print(attr_name)
            sleep(5)
            
            ################### 긍정적 리뷰 (4~5점)
            # 4,5점만 선택
            driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[1]/div/div/div[2]/div/div/div[1]/div/button/div/span').click() # 필터
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[4]').click() # 4점
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[5]').click() # 5점
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div/div[1]/button').click() # 적용
            driver.implicitly_wait(3)
            sleep(3)
            
            # 뷰숲
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            # 리뷰 텍스트 (페이지 당 10개 존재)
            attr_review_content_list = []
            attr_review_score_list = []
            
            reviews = soup.find_all('span', class_='yCeTE')
            for review in reviews:
                attr_review_content_list.append(review.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            sleep(3)
            
            ################ 부정적 리뷰 (1~2점) 
            # 4,5점 지우고 1,2점 체크
            driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[1]/div/div/div[2]/div/div/div[1]/div/button/div/span').click() # 필터
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[4]').click() # 4점 눌러서 해제
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[5]').click() # 5점 눌러서 해제
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[2]').click() # 2점 체크
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[1]').click() # 1점 체크
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div/div[1]/button').click() # 적용
            driver.implicitly_wait(3)
            sleep(3)
            
            # 뷰숲
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            reviews = soup.find_all('span', class_='yCeTE')
            for review in reviews:
                attr_review_content_list.append(review.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            sleep(3)
            
            for i in range(len(attr_review_score_list)+1):
                title = attr_review_content_list[i*2]
                content = attr_review_content_list[i*2-1]
                score = attr_review_score_list[i]
                train_data.append({'country':country, 'region': region, 'attr_name':attr_name, 'score':score, 'title':title, 'content':content})
            
            ################ 최신순 리뷰
            driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[1]/div/div/div[2]/div/div/div[1]/div/button/div/span').click() # 필터
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[2]').click() # 2점 눌러서 해제
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/button[1]').click() # 1점 눌러서 해제
            driver.implicitly_wait(3)
            driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div/div[1]/button').click() # 적용
            driver.implicitly_wait(3)
            sleep(3)
            
            # 뷰숲
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            # 리뷰 텍스트 (페이지 당 10개 존재)
            attr_review_content_list = []
            attr_review_score_list = []
            
            reviews = soup.find_all('span', class_='yCeTE')
            print(len(reviews))
            for review in reviews:
                attr_review_content_list.append(review.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            
            for i in range(len(attr_review_score_list)+1):
                title = attr_review_content_list[i*2]
                content = attr_review_content_list[i*2-1]
                score = attr_review_score_list[i]
                recent_data.append({'country':country, 'region': region, 'attr_name':attr_name, 'score':score, 'title':title, 'content':content})
                
            sleep(3)
            
    save_to_json(country, train_data, 'train')
    save_to_json(country, recent_data, 'recent')
    
    driver.quit()
    
if __name__=='__main__':
    controller()
        