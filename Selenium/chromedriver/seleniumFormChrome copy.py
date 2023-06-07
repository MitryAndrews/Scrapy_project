import zipfile
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
PROXY_LIST = []


# url = 'https://www.avito.ru/'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://chocolate.co.uk'
url='https://www.youla.ru/'
useragent = UserAgent()

 #options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')
#set proxy
# options.add_argument('--proxy-server=138.128.91.65:8000')
options.add_argument("--disable-blink-features=AutomationControlled")
s = Service(executable_path=fr'C:\Users\user\Scrapy_project\Selenium\chromedriver\chromedriver.exe')
driver =  webdriver.Chrome(service=s, options=options) 

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
    # driver.get(url=url)
    # time.sleep(2)
    # with open(f'index.html', 'w') as file:
    #     file.write(driver.page_source)
    # time.sleep(3)
    # reg_form = driver.find_element(by=By.CSS_SELECTOR, value='.index-services-menu-link-not-authenticated-Pzomx')
    # reg_form.click()
    # time.sleep(2)
    # phone_form = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    # phone_form.clear()
    # phone_form.send_keys('9053603453')
    # time.sleep(2)
    # input_password = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    # input_password.clear()
    # input_password.send_keys('apm425307mpa')
    # time.sleep(3)
    # chief_input = driver.find_element(by=By.CSS_SELECTOR, value='.css-p171hx')
    # chief_input.click()
    # time.sleep(120)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
