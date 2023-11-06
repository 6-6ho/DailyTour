from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

test_list = ["마리나 베이", "상하이", "교토"]
driver = webdriver.Chrome()

def crawler():
    for country in test_list:
        driver.get('https://www.tripadvisor.co.kr/')
        driver.implicitly_wait(10)
        
        input_text = driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[4]/div/div/div[2]/div/form/div/div/input')
        input_text.send_keys(country)
        input_text.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)
        
        driver.find_element(By.XPATH, '//*[@id="search-filters"]/ul/li[4]/a').click()
        driver.implicitly_wait(5)
        
        driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]')
        
        
        
        
        
    
    driver.quit()
    
if __name__=='__main__':
    crawler()