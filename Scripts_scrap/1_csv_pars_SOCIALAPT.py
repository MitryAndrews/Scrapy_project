import re
import time
from typing import Dict
import datetime
import requests
from bs4 import BeautifulSoup
import json
import csv
from random import choice
from random import uniform
count11 = 1
# num_room = int(input('Input number room = '))
# num_range = int(input('Input number page parsing - '))

parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2023-06-01'
parsing_day = '2023-07-04'
# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
dict_chief = []
dict_href = []

social_name = 'https://astrahan.social-apteka.ru'
dict_url = {
    'https://astrahan.social-apteka.ru/catalog/gripp-i-prostuda/': 7, 'https://astrahan.social-apteka.ru/catalog/bol-temperatura/': 8,
    'https://astrahan.social-apteka.ru/catalog/zheludok-kishechnik-pechen/': 12, 'https://astrahan.social-apteka.ru/catalog/serdechno-sosudistaya-sistema/': 18
    }
dict_chief = []
keys = ['group', 'name_item', 'href_name', 'price', 'producer']
for k, v in dict_url.items():
    group = k.replace('//', '').split('/')[2]
    # print(group)
    num_range = v
    count11 = 1
    for i in range(num_range):
        n_page = count11
        name_file = f'0{count11}_{group}_SOCIALAPT_{parsing_day}.html' if len(str(count11))==1 else f'{count11}_{group}_SOCIALAPT_{parsing_day}.html'
        # print('===================================================')
        print(name_file)
        with open(fr'C:\Users\user\Scrapy_project\Archive_SOCIALAPT\{name_file}', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        block_item = soup.find_all('div', class_= 'block-search-list-result__item2')
        # print(block_item)
        for item in block_item:
            dict1 = {'group': group, 'name_item': '', 'href_name': '', 'price': '', 'producer': ''}
            href_name = item.find('div', class_='block-search-list-result__name').find('a').get('href')
            href_name = social_name+href_name
            dict1['href_name'] = href_name
            # print(href_name)
            name_item = item.find('div', class_='block-search-list-result__name').text.strip()
            dict1['name_item'] = name_item
            # print(name_item)
            price = item.find('div', class_='search-list-result-price__current').get_text().replace('₽', '').replace(' ', '').replace('от', '').strip()#.text product-prices
            price = float(price) if price != '' else float(0)
            # print(price)
            dict1['price'] = price
            producer = item.find('div', class_='vendors').text.strip()
            dict1['producer'] = producer
            # print(producer)
            # print('name_item ===> ', name_item)
            # print('href ====> ', vita_name+href_name)
            # values = [name_item, href_name, price]
            # dict1 = {x: y for x, y in zip(keys, values)}
            dict_chief.append(dict1)
            # print('dict1 ===> ', dict1)
        count11 += 1
print(dict_chief)

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_SOCIALAPT_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




