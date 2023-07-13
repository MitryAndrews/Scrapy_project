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

dirname_from = fr'C:\Users\user\Scrapy_project\Archive_SOCIALAPT\href_SOCIALAPT_requests'
files_prep = os.listdir(dirname_from)
pattern = "*2023-07-04.html"
list_file = []
print(type(files_prep))
print(len(files_prep))
# parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
# parsing_day = '2023-01-18'
# parsing_day = '2023-06-01'
parsing_day = '2023-07-04'
patt = parsing_day+'.html'
files = []
for i in files_prep:#[300:310]:
    a = i.split('_')[-1]
    if a == patt:
        files.append(i)
        # print('prep', i)
# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')


dict_chief = []
dict_href = []

# nazdorov_name = 'https://xn--80aafkze2bij.online'
dict_url = {
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/preparaty-pri-prostudnykh-zabolevaniyakh-i-grippe/': 5, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/obezbolivayushchie-preparaty/': 13,
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/pishchevaritelnaya-sistema/': 19, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/serdechno-sosudistye-preparaty/': 38
    }
list_key = []
list_point = []
count_point = 0
for i in files:#[300:310]:
    count_point +=1
    print('===================================')
    print(count_point, i)
    dict_item = {}
    # print(i)
    with open(fr'C:\Users\user\Scrapy_project\Archive_SOCIALAPT\href_SOCIALAPT_requests\{i}', encoding='utf-8') as file_item: #{parsing_day} , encoding='utf-8'
            src = file_item.read()
    soup = BeautifulSoup(src, 'lxml')
    product_page = soup.find('div', class_= 'col-12')
    item_name = product_page.find('h1', id= 'brand').get_text().strip()
    list_key.append('count_index')
    dict_item['count_index'] = f'{count_point}_{parsing_day}'
    list_key.append('item_name')
    dict_item['item_name'] = item_name
    # print('item_name', '====>', item_name)
    features_list = product_page.find('div', class_= 'main-info-wrap full-height')
    # print(features_list)
    dict_feature = {}
    if features_list:
        ffff = features_list.find_all('li', class_= 'main-info-item')
        # print('====>>', ffff)
        for i in ffff:
            # item_feature = i.get_text()
            item_feature_name = i.find('span', class_='main-info-item__title').get_text().replace(':', '').strip()
            item_feature_value = i.find(class_=re.compile('main-info-item__desc')).get_text().strip()# if not None else i.find('a', class_=re.compile('main-info-item'))#.get_text()
            list_key.append(item_feature_name)
            dict_item[item_feature_name] = item_feature_value
            # print(' ======> ',item_feature_name, '===', item_feature_value)#ffff)# if features_list else 'nope'
    else:
        item_feature_name = 'nope'
        item_feature_value = 'nope'
        list_key.append(item_feature_name)
        dict_item[item_feature_name] = item_feature_value
    item_price2 = product_page.find('span', class_= 'product-order__price') if not None else 'Wow'
    # print('item_price2', item_price2)                    
    item_price = float(product_page.find('span', class_= 'product-order__price').get_text().strip().replace('от', '').replace('₽', '').replace(' ', '').strip()) if item_price2 is not None else 'Nope'
    # print(item_price)
    list_key.append('item_price')
    dict_item['item_price'] = item_price
    # availability_pharmacy = product_page.find('div', class_= 'search__table-wrap').find('div', class_='d2').find_all('div', class_='col11 name-short') if not None else 'Nope'#.get_text().strip().split(' ')[0]
    if product_page.find('div', class_= 'search__table-wrap'):
        availability_pharmacy2 = product_page.find('div', class_= 'search__table-wrap').find('div', class_='d2').find_all('div', class_='search__tbl-row result_item') if not None  else 'Nope'
        list_drugstore = []
        dict_drugstore = {}
    # if availability_pharmacy2 != 'Nope':
        for cart_adress in availability_pharmacy2:
            dict_drugstore = {}
            name_drugstore = cart_adress.find('div', class_= 'col11 name-short').get_text()
            dict_drugstore['name_drugstore'] = name_drugstore
            adress_drugstore = cart_adress.find('div', class_= 'col22 address').get_text()
            dict_drugstore['adress_drugstore'] = adress_drugstore
            workhours_drugstore = cart_adress.find('div', class_= 'col33 work-time').get_text()
            dict_drugstore['workhours_drugstore'] = workhours_drugstore
            list_drugstore.append(dict_drugstore)
            # print(cart_adress)
            # print(dict_drugstore)        
    # print(list_drugstore)
    list_key.append('list_drugstore')
    dict_item['list_drugstore'] = list_drugstore
    num_ava = len(list_drugstore)
    # num_ava = len(availability_pharmacy)
    # print(num_ava)#, availability_pharmacy2)
    list_key.append('availability_pharmacy')
    dict_item['availability_pharmacy'] = num_ava
    product_overview = product_page.find('ul', class_= 'list-full-info')#.get_text().strip()
    reserve_instruction_use = ['Nope', 'Nope nothing']
    instruction_use = product_overview.find_all('li', class_= 'list-full-info__item') if product_overview is not None else reserve_instruction_use
    # print(item_name, '====', type(instruction_use))
    if product_overview is not None:
        for tag in instruction_use:
            name_part_ins = tag.find('span', class_= 'list-full-info__title').get_text().strip()
            description_part_ins = tag.find('div', class_= 'list-full-info__desc')#.text#().strip()
            description_part_ins = description_part_ins.get_text().replace('/n', '')# if description_part_ins is not None else tag.find('h3', id = re.compile('pb')).find_next_siblings(text=True)
            # print(name_part_ins)
            list_key.append(name_part_ins)
            dict_item[name_part_ins] = description_part_ins
            # print(item_name, '====>', name_part_ins,'++++>', type(description_part_ins))
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

        

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_SOCIALAPT_href_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = list_key
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)


