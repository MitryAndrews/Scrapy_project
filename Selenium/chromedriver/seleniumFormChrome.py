from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By

url = 'https://www.avito.ru/'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://chocolate.co.uk'
# url2='https://www.youla.ru/'
# useragent = UserAgent()

 #options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
#set proxy
# options.add_argument('--proxy-server=138.128.91.65:8000')
driver =  webdriver.Chrome(
    executable_path=fr'C:\Users\user\Scrapy_project\Selenium\chromedriver\chromedriver.exe',
    options=options
    ) 

try:
    driver.get(url=url)
    # time.sleep(2)
    reg_form = driver.find_element(by=By.CSS_SELECTOR, value='.index-services-menu-link-not-authenticated-Pzomx')
    reg_form.click()
    time.sleep(2)
    phone_form = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    phone_form.clear()
    phone_form.send_keys('9618143453')
    time.sleep(2)
    input_password = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    input_password.clear()
    input_password.send_keys('Apm425307_')
    time.sleep(3)
    chief_input = driver.find_element(by=By.CSS_SELECTOR, value='.css-p171hx')
    chief_input.click()
    time.sleep(60)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
