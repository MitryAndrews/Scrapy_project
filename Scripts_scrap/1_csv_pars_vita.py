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
parsing_day = '2022-12-27'

# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
dict_chief = []
dict_href = []

vita_name = 'https://vitaexpress.ru'
dict_url = {
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/': 35, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/': 30,
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/': 36, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/': 71
    }
dict_chief = []
keys = ['name_item', 'href_name', 'price']
for k, v in dict_url.items():
    group = k.replace('//', '').split('/')[3]
    num_range = v
    count11 = 1
    for i in range(num_range):
        n_page = count11
        name_file = f'0{count11}_{group}_VITA_{parsing_day}.html' if len(str(count11))==1 else f'{count11}_{group}_VITA_{parsing_day}.html'
        # print('===================================================')
        print(name_file)
        with open(fr'C:\Users\user\Scrapy_project\Archive_Vita\{name_file}', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        block_item = soup.find_all('div', class_= 'product__mobRight d-flex flex-col h-100 w-sm-100 h-sm-auto')
        for item in block_item:
            href_name = item.find('a', itemprop='url').get('href')
            href_name = vita_name+href_name
            name_item = item.find('span', itemprop="name").text.strip()
            price = item.find('span', class_="priceSVG").find('span').text.strip().replace(' ', '').replace('от', '')
            price = float(price) if price != '' else float(0)
            # print('name_item ===> ', name_item)
            # print('href ====> ', vita_name+href_name)
            values = [name_item, href_name, price]
            dict1 = {x: y for x, y in zip(keys, values)}
            dict_chief.append(dict1)
            # print('dict1 ===> ', dict1)
        count11 += 1
# print(dict_chief)
# with open (f'csv_file_{parsing_day}_list_HREF_anunt_IMOBILIARE_RO.csv', 'w', encoding='utf-8', newline='\n') as csv_file_href:
#     fieldname = keys_anunt_href
#     writer = csv.DictWriter(csv_file_href, fieldnames=fieldname)
#     writer.writeheader()
#     for i in dict_href:
#         writer.writerow(i)
        

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_VITA_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




