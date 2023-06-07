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
parsing_day = '2023-05-27'

# print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
dict_chief = []
dict_href = []

social_name = 'https://www.avito.ru'
dict_url2 = {
              'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIBZ?cd=1': 16,
              'https://www.avito.ru/astrahan/kvartiry/prodam/2-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIJZ?cd=1': 20, 
              'https://www.avito.ru/astrahan/kvartiry/prodam/3-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIRZ?cd=1': 17,
              'https://www.avito.ru/astrahan/kvartiry/prodam/4-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIZZ?cd=1': 3
     }
dict_url1 = {
              'https://www.avito.ru/astrahan/kvartiry/prodam/studii/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFP5Y': 9,
              'https://www.avito.ru/astrahan/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIBZ': 26, 
              'https://www.avito.ru/astrahan/kvartiry/prodam/2-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIJZ': 9,
              'https://www.avito.ru/astrahan/kvartiry/prodam/3-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIRZ': 8,
              'https://www.avito.ru/astrahan/kvartiry/prodam/4-komnatnye/novostroyka-ASgBAQICAUSSA8YQAkDmBxSOUsoIFIZZ': 1

    }
dict_chief = []
keys = ['group', 'name_item', 'href_name', 'price', 'street', 'region', 'seller', 'group2']
choice_group2 = int(input('choice:  1 = First, 2 = Second  '))
dict_url = dict_url1 if choice_group2 == 1 else dict_url2
for k, v in dict_url.items():
    group = k.replace('//', '').split('/')[4]
    group2 = k.replace('//', '').split('/')[4:6][1].split('-')[0]
    # print(group)
    num_range = v
    count11 = 1
    for i in range(num_range):
        n_page = count11
        name_file = f'0{count11}_{group}_{group2}_AVITO_{parsing_day}.html' if len(str(count11))==1 else f'{count11}_{group}_{group2}_AVITO_{parsing_day}.html'
        #name_file = f'0{count11}_{group}_{group2}_AVITO_{parsing_day}.html' if len(str(count11))==1 else f'{count11}_{group}_{group2}_AVITO_{parsing_day}.html'
        # print('===================================================')
        print(name_file)
        with open(fr'C:\Users\user\Scrapy_project\Archive_AVITO\CHIEF_PAGES\{name_file}', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        block_item = soup.find_all('div', class_= 'iva-item-content-rejJg')
        # print(block_item)
        for item in block_item:
            dict1 = {'group': group, 'name_item': '', 'href_name': '', 'price': '', 'street': '', 'region': '', 'seller': '', 'group2': group2}
            href_name = item.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')#.find('a').get('href')
            href_name = social_name+href_name
            print(href_name)
            dict1['href_name'] = href_name
            # print(href_name)
            name_item = item.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('title')
            print(name_item)
            dict1['name_item'] = name_item
            # print(name_item)
            price = item.find('strong', class_='styles-module-root-LIAav').get_text().replace('₽', '').replace(' ', '').replace('\xa0', '').replace('\xa0', '').replace('от', '').strip()#.text product-prices
            price = float(price) if price != '' else float(0)
            print(price)
            dict1['price'] = price
            place = item.find('div', class_='geo-root-zPwRk')
            street = place.find('p', class_= 'styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD').text.strip()
            if place.find('p', class_= 'styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA styles-module-ellipsis-LKWy3 styles-module-ellipsis_oneLine-NY089 stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-root_top-HYzCt styles-module-margin-top_0-_usAN'):
                region = place.find('p', class_= 'styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA styles-module-ellipsis-LKWy3 styles-module-ellipsis_oneLine-NY089 stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-root_top-HYzCt styles-module-margin-top_0-_usAN').text.strip()
            else:
                region = 'None'
            print(street, type(street))
            print(region, type(street))
            dict1['street'] = street
            dict1['region'] = region
            if item.find('div', class_ = 'iva-item-sellerInfo-_q_Uw'):
                sell_block = item.find('div', class_ = 'iva-item-sellerInfo-_q_Uw')
                if sell_block.find('a', class_= 'styles-module-root-QmppR styles-module-root_noVisited-aFA10 styles-module-root_preset_black-JkIdG'):
                    seller = sell_block.find('a', class_= 'styles-module-root-QmppR styles-module-root_noVisited-aFA10 styles-module-root_preset_black-JkIdG').get_text().strip()
                else:
                    seller = 'None'
            print(seller)
            dict1['seller'] = seller
            print('=============================================================')
            # print('name_item ===> ', name_item)
            # print('href ====> ', vita_name+href_name)
            # values = [name_item, href_name, price]
            # dict1 = {x: y for x, y in zip(keys, values)}
            dict_chief.append(dict1)
            # print('dict1 ===> ', dict1)
        count11 += 1
# print(dict_chief)

with open(fr'C:\Users\user\Scrapy_project\CSV_file\csv_market_{choice_group2}_AVITO_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname, delimiter=';')
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




