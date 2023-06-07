import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from datetime import date
from time import sleep
from random import choice, uniform
from selenium import webdriver
from fake_useragent import UserAgent
import random
useragent = UserAgent()
user_agent = useragent.random
options = uc.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
now = date.today()
url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
# url = 'https://vitaexpress.ru/'
# url = 'https://xn--80aafkze2bij.online'
# url = 'https://astrahan.social-apteka.ru'

str_add = '?p='
dict_url = {
    'https://www.avito.ru/astrahan/kvartiry/prodam/studii/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFP5Y': 9,
    'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIBZ': 26, 
    'https://www.avito.ru/astrahan/kvartiry/prodam/2-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIJZ': 9,
    'https://www.avito.ru/astrahan/kvartiry/prodam/3-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIRZ': 8,
    'https://www.avito.ru/astrahan/kvartiry/prodam/4-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIZZ': 1
    }
# dict_url = {
#     'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIBZ?cd=1': 16,
#     'https://www.avito.ru/astrahan/kvartiry/prodam/2-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIJZ?cd=1': 20, 
#     'https://www.avito.ru/astrahan/kvartiry/prodam/3-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIRZ?cd=1': 17,
#     ' https://www.avito.ru/astrahan/kvartiry/prodam/4-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIZZ?cd=1': 3
#     }

dict_url = { 
              'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIBZ?cd=1': 16,
              'https://www.avito.ru/astrahan/kvartiry/prodam/2-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIJZ?cd=1': 20, 
              'https://www.avito.ru/astrahan/kvartiry/prodam/3-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIRZ?cd=1': 17,
              'https://www.avito.ru/astrahan/kvartiry/prodam/4-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIZZ?cd=1': 3
    }

list_url = []
path = fr'C:\Users\user\Scrapy_project\Archive_AVITO\CHIEF_PAGES'
count = 1

try:
    driver = uc.Chrome()
    driver.get(url=url)
    sleep(uniform(3, 5))
    count = 1
    for k, v in dict_url.items():
        count = 1
        for i in range(v):
            url_2 = k+str_add+str(count)
            group = url_2.replace('//', '').split('/')[4]
            group2 = url_2.replace('//', '').split('/')[4:6][1].split('-')[0]
            print(group)
            name_file = f'0{count}_{group}_{group2}_AVITO_{now}.html' if len(str(count))==1 else f'{count}_{group}_{group2}_AVITO_{now}.html'
            path_file = path+'\\'+name_file
            print(path_file)
            driver.get(url=url_2)
            with open(path_file, 'w', encoding="utf-8") as f: #html txt
                f.write(driver.page_source)
            print('path_file ENTER')
            sleep(uniform(5, 7))
            count +=1
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()