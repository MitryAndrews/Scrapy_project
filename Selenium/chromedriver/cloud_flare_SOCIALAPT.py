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
url = 'https://vitaexpress.ru/'
url = 'https://xn--80aafkze2bij.online'
url = 'https://astrahan.social-apteka.ru'

str_add = '?PAGEN_2='
dict_url = {
    'https://astrahan.social-apteka.ru/catalog/gripp-i-prostuda/': 7, 'https://astrahan.social-apteka.ru/catalog/bol-temperatura/': 8,
    'https://astrahan.social-apteka.ru/catalog/zheludok-kishechnik-pechen/': 12, 'https://astrahan.social-apteka.ru/catalog/serdechno-sosudistaya-sistema/': 18
    }

list_url = []
path = fr'C:\Users\user\Scrapy_project\Archive_SOCIALAPT'
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
            group = url_2.replace('//', '').split('/')[2]
            print(group)
            name_file = f'0{count}_{group}_SOCIALAPT_{now}.html' if len(str(count))==1 else f'{count}_{group}_SOCIALAPT_{now}.html'
            path_file = path+'\\'+name_file
            print(path_file)
            driver.get(url=url_2)
            with open(path_file, 'w', encoding="utf-8") as f: #html txt
                f.write(driver.page_source)
            print('path_file ENTER')
            sleep(uniform(2, 4))
            count +=1
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()