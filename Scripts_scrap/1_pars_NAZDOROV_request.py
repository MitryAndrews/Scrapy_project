import time
from typing import Dict
import datetime
import requests
from bs4 import BeautifulSoup
import json
import csv
import random
from random import choice
from random import uniform
from fake_useragent import UserAgent
# from look_ip import get_location
user_agent = UserAgent()
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2023-01-16'
path_ = fr'C:\Users\user\Scrapy_project\CSV_file'
# path_ = fr'C:\Users\mitry\Scraping\csv_file'
file_name = path_+'\csv_NAZDOROV_page_parsing_'+parsing_day+'.csv'
list_href = []
list_name = []
list_group = []
with open(fr'{file_name}', 'r', encoding='utf-8') as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        list_href.append(row['href_name'])
        list_name.append(row['name_item'])
        list_group.append(row['group'])
        # print(row['href_name'])
list_value = [[i, j] for i, j in zip(list_href, list_group)]
dict_item = {x: y for x, y in zip(list_name, list_value)}
proxy_list = ['45.130.70.64:8000', '45.130.69.212:8000', '45.130.71.208:8000']
proxy_list2 = []
for i in proxy_list:
    prox = i.replace('п»ї', '')
    print(prox)
    proxy_list2.append(prox)
count = 1
for item_key, item_value in dict_item.items():
    proxy = {'http': 'http://' + choice(proxy_list2)}
    agent = {'User-Agent': f'{user_agent.random}'}
    print(proxy, agent)
    #ip_current = get_location(url='https://2ip.ru')
    print(f'Парсинг - {count}, страницы {item_value[1]}; user-agent - {agent}')#, ip_current - {ip_current}; proxy - {proxy}')
    if count % 5 == 0:
        print('CANGE IP 5 (in 10 sec?)')#, ip_current
        time.sleep(uniform(7, 10))
    elif count % 10 == 0:
        print('CANGE IP 10 (in 10 sec?)') #, ip_current
        time.sleep(uniform(10, 13))
    else:
        time.sleep(uniform(5, 8))
    # print('# = ', count, ' keys - ', item_key, ' value -', item_value)
    req = requests.get(item_value[0], headers=agent, proxies=proxy)
    if req.status_code == 200:
        src = req.text
        with open(fr'C:\Users\user\Scrapy_project\Archive_NAZDOROV\href_NAZDOROV_requests\{count}_{item_value[1]}_{parsing_day}.html', 'w', encoding='utf-8') as file:
            file.write(src)
        print('thats OK')
    else:
        print('Error', req.status_code)
    count += 1


