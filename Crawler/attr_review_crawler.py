from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

test_list = ["마리나 베이", "상하이"]
driver = webdriver.Chrome()
main_url = 'https://www.tripadvisor.co.kr/'


def crawler():
    # 메인 페이지 들어가기
    for country in test_list:
        driver.get(main_url)
        driver.implicitly_wait(5)
        sleep(2)
        
        # 지역 검색창에 입력 후 엔터
        input_text = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[4]/div/div/div[2]/div/form/div/div/input')
        input_text.send_keys(country)
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
        
        # 모든 관광지에 대해서 크롤링 하는걸로 변경해야하기 때문에
        for i in range(3): # for attr in attr_hrefs로 돌려야 함
            driver.get(f"{main_url}{attr_hrefs[i]}")
            driver.implicitly_wait(5)
            sleep(3)
            
            # 관광지 이름        
            attr_name = driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/div[1]/div/div[1]/div[1]').text
            # 관광지 평점
            attr_score = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[2]/div[1]/header/div[3]/div[1]/div/h1').text
            print(attr_name)
            print(attr_score)
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
            
            contents = soup.find_all('span', class_='yCeTE')
            print(len(contents))
            for content in contents:
                attr_review_content_list.append(content.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            sleep(3)
                
            
            # 다음 페이지로 넘어 갈 경우 페이지의 url이 변경되는 것 확인
            # https://www.tripadvisor.co.kr/Attraction_Review-g308272-d1022087-Reviews-Madame_Tussauds_Shanghai-Shanghai.html#REVIEWS'
            # 이런 링크라면 다음 페이지를 눌렀을때 Reviews-or10 ~
            #                                   Reviews-or20 ~ 패턴                                    
            
            # 긍정 키워드 달아서 json으로 저장해야 함
            
            
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
            
            # 리뷰 텍스트 (페이지 당 10개 존재)
            attr_review_content_list = []
            attr_review_score_list = []
            
            contents = soup.find_all('span', class_='yCeTE')
            print(len(contents))
            for content in contents:
                attr_review_content_list.append(content.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            sleep(3)
            
            # 부정 키워드 달아서 json으로 저장
            
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
            
            contents = soup.find_all('span', class_='yCeTE')
            print(len(contents))
            for content in contents:
                attr_review_content_list.append(content.text)
            
            # 리뷰 평점 / 파싱해야함 aria-label="풍선 5개 중 5.0"
            scores = soup.find_all('svg', class_='UctUV d H0')
            for score in scores:
                attr_review_score_list.append(score['aria-label'].split()[-1][0])
                
            print(attr_review_content_list)
            print(attr_review_score_list)
            sleep(3)
    
    driver.quit()
    
if __name__=='__main__':
    crawler()