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
now = '2023-05-27'
url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
# url = 'https://vitaexpress.ru/'
# url = 'https://xn--80aafkze2bij.online'
# url = 'https://astrahan.social-apteka.ru'
list_href = []
str_add = '?p='
choice_group2 = int(input('choice:  1 = First, 2 = Second  '))
with open(fr"C:\Users\user\Scrapy_project\CSV_file\csv_market_{choice_group2}_AVITO_page_parsing_{now}.csv", 'r', encoding='utf-8') as csv_file:
    for i in csv_file:
        #print(i, type(i))
        #print(i.strip().split(';')[2].replace("'", ""))
        # k = i.strip().split(';')[0].replace("0", " ")
        v = i.strip().split(';')[2].replace("'", "")#.replace(" 0", "").replace("0", " ")#.strip()#.replace("''", "").replace("' '", " ").replace("'", "")
        list_href.append(v)
        group = v.replace('//', '').split('/')[-1].split('_')[0]+v.replace('//', '').split('/')[-1].split('_')[1]
        # print(group)
        # dict_[k] = v
dict_url = {
    'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIBZ': 4, 
    }
number = 2132
list_href = list_href[number:]# last to 100
list_url = []
group2 = 'second'
group2 = 'first'
path = fr'C:\Users\user\Scrapy_project\Archive_AVITO\HREF_AVITO'
count = number
#'======================================================================================'
try:
    driver = uc.Chrome()
    driver.get(url=url)
    sleep(uniform(2, 4))
    count = number
    for k in list_href:
        #print(k)
        #count = 1
        url_2 = k
        # group = url_2.replace('//', '').split('/')[4]
        group = k.replace('//', '').split('/')[-1].replace('-', '_').split('_')[0]+k.replace('//', '').split('/')[-1].replace('-', '_').split('_')[1]
        #print(group)
        name_file = f'0{count}_{group}_market_{choice_group2}_AVITO_{now}.html' if len(str(count))==1 else f'{count}_{group}_market_{choice_group2}_AVITO_{now}.html'
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
    
    
#'=================================================================================='