from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

useragent = UserAgent()
#options
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', useragent.random)

url = 'https://www.avito.ru/'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
url = 'https://chocolate.co.uk'
url2='https://www.youla.ru/'


driver =  webdriver.Firefox(
    executable_path=fr'C:\Users\user\Scrapy_project\Selenium\firefoxdriver\geckodriver.exe',
    options=options)
try:
    driver.get(url=url)
    time.sleep(3)
    # driver.get_screenshot_as_file('avitoF1.png')
    # driver.save_screenshot('avitoF2.png')
    # driver.refresh()
    # time.sleep(2)
    # driver.get('https://2ip.ru')
    # time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
