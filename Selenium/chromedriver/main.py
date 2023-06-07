from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

url = 'https://www.avito.ru/'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://chocolate.co.uk'
url2='https://www.youla.ru/'
useragent = UserAgent()
 #options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')
#set proxy
# options.add_argument('--proxy-server=138.128.91.65:8000')
driver =  webdriver.Chrome(
    executable_path=fr'C:\Users\user\Scrapy_project\Selenium\chromedriver\chromedriver.exe',
    options=options
    ) 

try:
    driver.get(url=url)
    time.sleep(2)
    # driver.get(url=url2)
    # time.sleep(3)
    # driver.get_screenshot_as_file('avito1.png')
    # driver.save_screenshot('avito2.png')
    # driver.refresh()
    # time.sleep(2)
    driver.get('https://2ip.ru')
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
