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
parsing_day = '2023-05-30'
parsing_day = '2023-07-03'

# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
dict_chief = []
dict_href = []

nazdorov_name = 'https://xn--80aafkze2bij.online'
dict_url = {
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/preparaty-pri-prostudnykh-zabolevaniyakh-i-grippe/': 4, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/obezbolivayushchie-preparaty/': 12,
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/pishchevaritelnaya-sistema/': 17, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/serdechno-sosudistye-preparaty/': 35
    }
dict_chief = []
keys = ['group', 'name_item', 'href_name', 'price', 'stock', 'recipe', 'substance', 'producer']
for k, v in dict_url.items():
    group = k.replace('//', '').split('/')[3]
    num_range = v
    count11 = 1
    for i in range(num_range):
        n_page = count11
        name_file = f'0{count11}_{group}_NAZDOROV_{parsing_day}.html' if len(str(count11))==1 else f'{count11}_{group}_NAZDOROV_{parsing_day}.html'
        # print('===================================================')
        print(name_file)
        with open(fr'C:\Users\user\Scrapy_project\Archive_NAZDOROV\{name_file}', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        block_item = soup.find_all('div', class_= 'product-item col-xl-4 col-lg-4 col-md-4 col-sm-6')
        # print(len(block_item))
        for item in block_item:
            dict1 = {'group': group, 'name_item': '', 'href_name': '', 'price': '', 'stock': '', 'recipe': '', 'substance': '', 'producer': ''}
            href_name = item.find('a', class_='product-item__title').get('href')
            href_name = nazdorov_name+href_name
            dict1['href_name'] = href_name
            # print(href_name)
            name_item = item.find('a', class_='product-item__title').text.strip()
            dict1['name_item'] = name_item
            # print(name_item)
            item_offers = item.find('div', class_="product-item__offers offers")
            price = item_offers.find('div', class_='product-prices').get_text().replace('₽', '').replace(' ', '')#.text product-prices
            price = float(price) if price != '' else float(0)
            dict1['price'] = price
            prod_stock = item_offers.find('div', class_=('btn btn-alternative btn-gray btn-block'))
            stock = prod_stock.text if prod_stock != None else 'есть в наличии'
            dict1['stock'] = stock
            # print(stock)
            item_features = item.find_all('div', class_='product-item__features-item')# if item.find('div', class_='product-item__features') != None else 'Нет данных'
            print('stock ====>', stock, '------>', len(item_features))
            for i in item_features:
                item_feature_name = i.find('div', class_='product-item__features-name').get_text()
                item_feature_value = i.find('div', class_='product-item__features-value').get_text()
                if item_feature_name == 'По рецепту:':
                    dict1['recipe'] = item_feature_value
                elif item_feature_name == 'Действующее вещество:':
                    dict1['substance'] = item_feature_value
                elif item_feature_name == 'Производитель:':
                    dict1['producer'] = item_feature_value
            # print(dict1)
            
            # # print('name_item ===> ', name_item)
            # # print('href ====> ', vita_name+href_name)
            # values = [name_item, href_name, price]
            # dict1 = {x: y for x, y in zip(keys, values)}
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
        

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_NAZDOROV_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




