from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

test_list = ["japan", "china", "singapore"]
driver = webdriver.Chrome()

def crawler():
    driver.get('https://kr.trip.com/?locale=ko-kr')
    driver.implicitly_wait(10)
    
    for country in test_list:
        input_text = driver.find_element(By.ID, "hotels-destination")
        input_text.send_keys(Keys.CONTROL, 'a')
        input_text.send_keys(Keys.DELETE)
        driver.implicitly_wait(5)
        input_text.send_keys(country)
        driver.implicitly_wait(5)
        sleep(1)
        
        target_list = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/ul/li[1]/div/div[2]/div[2]/div[2]")
        driver.implicitly_wait(5)
        
        for target in target_list:
            print(target.text)
        driver.implicitly_wait(5)
        
        sleep(2)
    driver.quit()
    
if __name__=='__main__':
    crawler()