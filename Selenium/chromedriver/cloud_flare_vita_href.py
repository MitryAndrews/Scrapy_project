import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from datetime import date
from time import sleep
from random import choice, uniform
from selenium import webdriver
from fake_useragent import UserAgent
import random
import csv

proxy_list2 = ['45.130.70.64:8000', '45.130.69.212:8000', '45.130.71.208:8000']
proxy = choice(proxy_list2)


now = date.today()
parsing_day = '2022-12-27'
now = parsing_day
path_ = fr'C:\Users\user\Scrapy_project\CSV_file'
file_name = path_+'\csv_VITA_page_parsing_'+parsing_day+'.csv'
list_href = []
with open(fr'{file_name}', 'r', encoding='utf-8') as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        list_href.append(row['href_name'])
        # print(row['href_name'])
        
# path2 = 'C:\Users\user\Scrapy_project\Archive_Vita\href_VITA'
str_add = '?&page_count='
dict_url = {
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/': 35, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/': 30,
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/': 36, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/': 71
    }

list_url = ['https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/'
               'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/']
path2 = fr'C:\Users\user\Scrapy_project\Archive_Vita\href_VITA'
count = 1
num_href = len(list_href)
list_href = list_href[:1]
# ================================
try:
    driver = uc.Chrome(version_main = 108)
    # driver.get(url=url)
    # sleep(uniform(3, 5))
    count = 1
    
    for href in list_href:
        proxy = choice(proxy_list2)
        useragent = UserAgent()
        user_agent = useragent.random
        options = uc.ChromeOptions()
        options = uc.options.ChromeOptions()
        options.add_argument(f'--proxy-server={proxy}')
        options.add_argument(f'--user-agent={user_agent}')
        options.add_argument(f"--disable-popup-blocking")
        options.add_argument(f"--disable-notifications")
        url = 'https://awebanalysis.com/ru/what-is-my-ip-address/'
        url_2 = href
        name_file = f'0{count}_href_VITA_{now}.html' if len(str(count))==1 else f'{count}_href_VITA_{now}.html'
        path_file = path2+'\\'+name_file
        print(path_file)
        driver = uc.Chrome(version_main = 108)#, options=options)
        # driver.get(url=url)
        # sleep(uniform(5, 7))
        driver.get(url=url_2)
        with open(path_file, 'w', encoding="utf-8") as f: #html txt
            f.write(driver.page_source)
        print('path_file ENTER')
        sleep(uniform(30, 35))
        count +=1
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    
    
