import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# 브라우저 꺼짐 방지 옵션 설정 및 driver 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def accom_review_crawling() :
    # 크롤링할 국가 지역
    URL = 'https://www.agoda.com/ko-kr/?ds=rQL3Oqsd%2FK%2FPTWIy'
    driver.get(URL) #페이지 접속

    time.sleep(10)

    close_btn = driver.find_element(By.CLASS_NAME, 'ab-close-button')
    close_btn.click()

    # 숙소를 검색할 국가의 지역 
    accom = '도쿄'  # 검색할 국가의 지역

    keyword_element = driver.find_element(By.ID, 'textInput') # 검색창 element
    keyword_element.clear() 
    keyword_element.send_keys(accom)    # 검색창에 입력하고 입력 타이핑
    
    time.sleep(1)

    li_btn = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "Suggestion__categoryName")))
    li_btn.click()

    driver.execute_script("window.scrollTo(0, 700)") 
    time.sleep(1)

    # 검색하기 버튼 클릭. 
    search_btn = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[2]/div/button')
    driver.execute_script("arguments[0].click();", search_btn)
    # search_btn.click() 

    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[-1]) # 새로 열린 탭으로 이동

    driver.implicitly_wait(5)
    time.sleep(3)

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')


    hotel_list_element = soup.find('ol', class_='hotel-list-container') # 호텔 리스트를 담고 있는 태그 
    a_tag = hotel_list_element.find_all('a')  # 호텔 상세 페이지 링크 태그 찾기

    hotel_url_list = []  # url을 담을 list
    for a in a_tag:
        if "href" in a.attrs:
            hotel_url = ''
            hotel_url += 'https://www.agoda.com/' + a["href"]
            hotel_url_list.append(hotel_url)
         
    print(len(hotel_list_element))

    return hotel_url_list


# 호텔 상세 페이지에서 리뷰 및 평점 크롤링
def hotel_review_crawling(hotel_url_list):
    hotel_list = []

    for hotel in hotel_url_list: 
       driver.get(hotel) #페이지 접속
       
       time.sleep(5)

       html = driver.page_source 
       soup = BeautifulSoup(html, 'html.parser')
       hotel_name = soup.find('p', class_='HeaderCerebrum__Name').text
       print(hotel_name)

       element = soup.find('li', {'data-href' : '#customer-reviews-panel'})
       data_href = element['data-href']
       print(data_href)
       nav_bar = driver.find_element(By.CSS_SELECTOR, f'[data-href="{data_href}"] > button')
       driver.execute_script("arguments[0].click();", nav_bar)


       time.sleep(3)

       # 리뷰 작성 언어 선택 (크롤러 시작할 때마다 페이지 html 양식이 바뀌어서 예외 처리.. )
       try:
           language_select = Select(driver.find_element(By.CSS_SELECTOR, '#reviewFilterSection > div.sc-bdfBwQ.sc-gsTCUz.gdcQLK > div.sc-bdfBwQ.sc-gsTCUz.djZOQg > div > div > label > div.sc-bdfBwQ.sc-gsTCUz.bqqCNI > span > select') )
           time.sleep(3)
           language_select.select_by_visible_text('한국어')
           time.sleep(3)
           language_select = driver.find_element(By.XPATH, '//*[@id="reviews-language-filter_list"]')
           driver.execute_script("arguments[0].click();", language_select)
           language = driver.find_element(By.XPATH, '//*[@id="reviews-language-filter_list"]/ul/li[3]/span/span[2]')
           driver.execute_script("arguments[0].click();", language)
       except:
           driver.find_element(By.CSS_SELECTOR, '#reviewFilterSection > div.Review__FilterContainer')
           language_select = driver.find_element(By.XPATH, '//*[@id="reviews-language-filter_list"]')
           driver.execute_script("arguments[0].click();", language_select)
           korean_xpath = """//*[@id="reviews-language-filter_list"]/ul/li/span//span[text()='한국어']"""
           korean_language = driver.find_element(By.XPATH, korean_xpath)
           korean_language.click()

           

       # 리뷰 정렬 
       sort_select = Select(driver.find_element(By.XPATH, '//*[@id="review-sort-id"]'))
       time.sleep(2)
       sort_select.select_by_value("1") # 1 - 최신순, 2 - 높은 평점 우선 보기, 3 - 낮은평점우선보기

       time.sleep(1)


       for i in range(0, 3) :  # 리뷰 3 페이지까지 이동하면서 데이터 추가.
            html = driver.page_source   # 리뷰 페이지 이동할 때 파싱 새로 해주기 
            soup = BeautifulSoup(html, 'html.parser')

            review_div = soup.find_all('div', class_='Review-comment')  # 리뷰 div 모두 찾기
            # print(review_div)

            for review in review_div : 
                review_score = review.find('div', class_='Review-comment-leftScore').text  # 리뷰 평점
                review_title = review.find('h3', class_='Review-comment-bodyTitle').text   # 리뷰 제목
                review_content = review.find('p', class_='Review-comment-bodyText').text   # 리뷰 상세 정보 

                parse_to_json(hotel_name, float(review_score)//2, review_title, review_content, hotel_list)  # json으로 저장

                print(review_title)
            print()
            page_btn = driver.find_element(By.XPATH, '//*[@id="reviewSection"]/div[4]/div/span[3]/i')
            driver.execute_script("arguments[0].click();", page_btn)
            time.sleep(3)

    save_to_json(hotel_list) # json 파일로 저장 

def parse_to_json(hotel_name, review_score, review_title, review_content, hotel_list):
    hotel_list.append({
        "national" : "일본", 
        "local" : "도쿄",
        "hotel_name" : hotel_name,
        "score" : review_score,
        "title" : review_title,
        "content" : review_content
    })
    print(hotel_list)

# 크롤링 데이터 json으로 저장
def save_to_json(hotel_list):
    with open('japan_accom_review.json', 'w', encoding='utf-8') as file :
        json.dump({'accom_review' : hotel_list}, file, ensure_ascii=False, indent=4)


def main():
    hotel_url_list = accom_review_crawling()
    hotel_review_crawling(hotel_url_list)


if __name__ == '__main__' :
    main()