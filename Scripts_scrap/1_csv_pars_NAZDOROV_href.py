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
import os, fnmatch
count11 = 1

dirname_from = fr'C:\Users\user\Scrapy_project\Archive_NAZDOROV\href_NAZDOROV_requests'
files = os.listdir(dirname_from)
pattern = "*.html"
list_file = []
print(type(files))
print(len(files))
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2023-01-16'
parsing_day = '2023-05-30'

# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')


dict_chief = []
dict_href = []

# nazdorov_name = 'https://xn--80aafkze2bij.online'
dict_url = {
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/preparaty-pri-prostudnykh-zabolevaniyakh-i-grippe/': 5, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/obezbolivayushchie-preparaty/': 12,
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/pishchevaritelnaya-sistema/': 17, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/serdechno-sosudistye-preparaty/': 35
    }
list_key = []
list_point = []
count_point = 0
for i in files:#[400:450]:
    count_point +=1
    print('===================================')
    print(count_point, i)
    dict_item = {}
    # print(i)
    with open(fr'C:\Users\user\Scrapy_project\Archive_NAZDOROV\href_NAZDOROV_requests\{i}', encoding='utf-8') as file_item: #{parsing_day} , encoding='utf-8'
            src = file_item.read()
    soup = BeautifulSoup(src, 'lxml')
    product_page = soup.find('article', class_= 'product-page')
    item_name = product_page.find('h1', class_= 'product-page__header title').get_text().strip()
    list_key.append('count_index')
    dict_item['count_index'] = f'{count_point}_{parsing_day}'
    list_key.append('item_name')
    dict_item['item_name'] = item_name
    # print(item_name)
    features_list = product_page.find('div', class_= 'features-list')
    dict_feature = {}
    if features_list:
        ffff = features_list.find_all('div', class_= 'features-list__item')
        # print('======================================================')
        for i in ffff:
            # item_feature = i.get_text()
            item_feature_name = i.find('div', class_='features-list__name').get_text()
            item_feature_value = i.find('div', class_='features-list__value').get_text()
            list_key.append(item_feature_name)
            dict_item[item_feature_name] = item_feature_value
            # print(dict_feature)#, ' ======> ', item_feature_value)#ffff)# if features_list else 'nope'
    else:
        item_feature_name = 'nope'
        item_feature_value = 'nope'
        list_key.append(item_feature_name)
        dict_item[item_feature_name] = item_feature_value
    item_price = float(product_page.find('span', class_= 'product-price').get_text().strip().split(' ')[0])
    list_key.append('item_price')
    dict_item['item_price'] = item_price
    availability_pharmacy = product_page.find('table', class_= 'table table-striped table-sm small').find_all('tr')#.get_text().strip().split(' ')[0]
    num_ava = len(availability_pharmacy)
    list_key.append('availability_pharmacy')
    dict_item['availability_pharmacy'] = num_ava
    product_overview = product_page.find('div', class_= 'product-overview')#.get_text().strip()
    reserve_instruction_use = ['Nope', 'Nope nothing']
    instruction_use = product_overview.find_all('div', id = re.compile('ph')) if product_overview is not None else reserve_instruction_use
    print(item_name, '====', type(instruction_use))
    if product_overview is not None:
        for tag in instruction_use:
            name_part_ins = tag.find('h3', id = re.compile('pb')).get_text().strip()
            description_part_ins = tag.find('p')#.text#().strip()
            description_part_ins = description_part_ins.get_text() if description_part_ins is not None else tag.find('h3', id = re.compile('pb')).find_next_siblings(text=True)
            # print(name_part_ins)
            list_key.append(name_part_ins)
            dict_item[name_part_ins] = description_part_ins
            # print(item_name, '====>', name_part_ins,'++++>', description_part_ins)
    else:
        for tag in instruction_use:
            name_part_ins = reserve_instruction_use[0]
            description_part_ins = reserve_instruction_use[1]
            # print(name_part_ins)
            list_key.append(name_part_ins)
            dict_item[name_part_ins] = description_part_ins
                    
    #print('!===>', len(product_overview), type(product_overview))
    # print('===> ',num_ava-1)#, ' ==== ', availability_pharmacy)
    # print(' ====> ',dict_item)
    dict_chief.append(dict_item)
# print(dict_chief)
list_key = list(set(list_key))
print(list_key)
#================================================================

        

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_NAZDOROV_href_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = list_key
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)


