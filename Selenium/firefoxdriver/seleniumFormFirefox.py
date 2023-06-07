from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
useragent = UserAgent()
#options
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', useragent.random)
options.set_preference("dom.webdriver.enabled", False)
url = 'https://www.avito.ru/'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://chocolate.co.uk'
# url2='https://www.youla.ru/'


driver =  webdriver.Firefox(
    executable_path=fr'C:\Users\user\Scrapy_project\Selenium\firefoxdriver\geckodriver.exe',
    options=options)
try:
    driver.get(url=url)
    # time.sleep(2)
    reg_form = driver.find_element(by=By.CSS_SELECTOR, value='.index-services-menu-link-not-authenticated-Pzomx')
    reg_form.click()
    time.sleep(2)
    phone_form = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    phone_form.clear()
    phone_form.send_keys('9053603453')
    time.sleep(2)
    input_password = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    input_password.clear()
    input_password.send_keys('apm425307mpa')
    time.sleep(3)
    chief_input = driver.find_element(by=By.CSS_SELECTOR, value='.css-p171hx')
    chief_input.click()
    time.sleep(20)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
