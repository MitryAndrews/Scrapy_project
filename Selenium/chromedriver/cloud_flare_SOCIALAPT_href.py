import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import csv
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
now = '2023-06-01'
now = '2023-07-04'
url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
# url = 'https://vitaexpress.ru/'
# url = 'https://xn--80aafkze2bij.online'
url = 'https://astrahan.social-apteka.ru'

str_add = '?p='
path_ = fr'C:\Users\user\Scrapy_project\CSV_file'
file_name = path_+'\csv_SOCIALAPT_page_parsing_'+now+'.csv'
list_href = []
list_name = []
list_group = []

with open(fr'{file_name}', 'r', encoding='utf-8') as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        list_href.append(row['href_name'])
        list_name.append(row['name_item'])
        list_group.append(row['group'])
list_value = [[i, j] for i, j in zip(list_href, list_group)]
dict_item = {x: y for x, y in zip(list_name, list_value)}
for k, v in dict_item.items():
    print(f'{v[1]} : ---> {v[0]}')
    
#print(list_href)
dict_url = {
    'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIBZ': 4, 
    }
number = 1
list_href = list_href[number:3]# last to 100
list_url = []
group2 = 'second'
group2 = 'first'
path = fr'C:\Users\user\Scrapy_project\CSV_file'
count = number
#'======================================================================================'
try:
    driver = uc.Chrome()
    driver.get(url=url)
    sleep(uniform(2, 4))
    count = number
    for k, v in dict_item.items():
        #print(k)
        #count = 1
        url_2 = v[0]
        # group = url_2.replace('//', '').split('/')[4]
        group = v[1]
        #print(group)
        path_file = fr'C:\Users\user\Scrapy_project\Archive_SOCIALAPT\href_SOCIALAPT_requests\{count}_{v[1]}_{now}.html'
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
    
    
#'=================================================================================='