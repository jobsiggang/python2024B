from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text="부산 맛집"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#power_link_body > ul > li:nth-child(1) > div > div.title_url_area > div")
print("학번이름")
print(temp_div.text)
time.sleep(10)
