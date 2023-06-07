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
count11 = 123
# num_room = int(input('Input number room = '))
num_range = int(input('Input number page parsing - '))
# num_range = 255
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2022-05-14'
input_page_numer_apart = str(input('Choise number page 1-2 camera 30 days: input 1 OR 3-4+ camera 30 days: input 2 = '))
dict_camere_days = {'1': '1_2 camera 30 days', '2': '3_4 camera 30 days'}
list_name_anunt = []
list_link_anunt = []
list_anunt_href = []
adress_district = ''
print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
# dict_caracter = {}
keys_list = []
dict_chief = []
dict_href = []
keys_caracter = {'camr': 'number_camer','4 RM': 'number_camer', '3 RM': 'number_camer','2 RM': 'number_camer', 'RMLN': 'number_camer', '48 R': 'squere_flat', 'util': 'squere_flat', 'Deco': 'separat_flat', 'Semi': 'separat_flat',
                 'Nede': 'separat_flat', 'Circ': 'separat_flat', 'Vago': 'separat_flat', 'Ulti': 'num_flour', 'Demi': 'num_flour',
                 'Mans': 'num_flour', 'Part': 'num_flour', 'Etaj': 'num_flour', 'Bloc': 'age_flat', 'Imob': 'age_flat'}
keys_anunt_href = ['No', 'anunt', 'orasul', 'href', 'site', 'parsing_day']
for i in range(num_range):
    n_page = count11
    with open(fr'D:\Archive IMOBILIARE romania anunt\archive\bucuresti\2022-05-14\{count11}_{count11} страница_IMOBILIARE_RO_{dict_camere_days[input_page_numer_apart]}_{parsing_day}.html', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    block_item = soup.find_all('div', class_='container-box-anunturi')
    # print(block_item)
    count1 = 1
    # keys = ['id_flat', 'name_flat', 'href_flat', 'adress_flat', 'price_all', 'price_per_metr', 'Saller', 'Saller href', 'subscribe_flat']
    keys = ['count_page', 'count_number_anunt', 'name_anunt', 'parsing_day', 'numer_camere', 'dezvoltator', 'href_flat', 'orasul', 'location_txt',
                'distance_to_metro', 'time_to_metro', 'price_all', 'metri_patrati', 'apart_etaj', 'casa_etaj',
                'compart', 'bloc', 'logo']
    
    for item in block_item:
        # dict_caracter = {}
        block_name = soup.find_all('div', class_='box-anunt')
        count_flat = 0
        
        for item_block_name in block_name:   # это блок для ВСЕХ объявлений!!!!!!!
            dict_caracter = {}
            count_num_var = 1
            dict_caracter['06_parsing_day'] = parsing_day
            keys_list.append('06_parsing_day')
            type_imobiliare = item_block_name.get('data-name')
            block_type_logo = item_block_name.get('data-ssellertype')
            block_logo = item_block_name.get('data-ssellername')
            # print(type_imobiliare,' ==>', block_type_logo, ' ==>', block_logo)
            dict_caracter['07_type_logo'] = block_type_logo
            keys_list.append('07_type_logo')
            dict_caracter['08_logo_agent_dez'] = block_logo
            keys_list.append('08_logo_agent_dez')
            
            dict_caracter['01_count_page'] = count11
            keys_list.append('01_count_page')
            
            if item_block_name.find('h2', class_='titlu-anunt hidden-xs'):
                block_anunt = item_block_name.find('h2', class_='titlu-anunt hidden-xs')
                href_flat = item_block_name.find('h2', class_='titlu-anunt hidden-xs').find('a', itemprop = 'name').get('href') #'https://www.avito.ru' + item_block_name.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
                orasul = href_flat.split('/')[4].strip().upper()
                dict_caracter['04_href'] = href_flat
                keys_list.append('04_href')
                dict_caracter['05_orasul'] = orasul
                keys_list.append('05_orasul')
                # print(count_flat, ' == ', keys_list, ' == ', dict_caracter)
                name_anunt = item_block_name.find('h2', class_='titlu-anunt hidden-xs').find('span').text
                dict_caracter['03_name_anunt'] = name_anunt
                keys_list.append('03_name_anunt')
                count_number_anunt += 1
                dict_caracter['02_count_number_anunt'] = count_number_anunt
                keys_list.append('02_count_number_anunt')
                
                list_anunt_href = [count_number_anunt, name_anunt, orasul, href_flat, 'imobiliare_ro', parsing_day]
                count_flat += 1
            elif item_block_name.find('h2', class_='titlu-anunt'):
                nnnn = item_block_name.find('h2', class_='titlu-anunt')
                count_number_anunt += 1
                if nnnn.find('a', class_='click_din_lista'):
                    href_flat = nnnn.find('a', class_='click_din_lista').get('href')
                    orasul = href_flat.split('/')[4].strip().upper()
                    name_anunt = nnnn.find('span').text
                    
                    dict_caracter['04_href'] = href_flat
                    keys_list.append('04_href')
                    dict_caracter['05_orasul'] = orasul
                    keys_list.append('05_orasul')
                    dict_caracter['03_name_anunt'] = name_anunt
                    keys_list.append('03_name_anunt')
                    dict_caracter['02_count_number_anunt'] = count_number_anunt
                    keys_list.append('02_count_number_anunt')
                    list_anunt_href = [count_number_anunt, name_anunt, orasul, href_flat, 'imobiliare_ro', parsing_day]
                    count_flat += 1
                    # print(name_anunt, ' == ', orasul, 'its a......', href_flat)
                # print(' =================================')
            # elif item_block_name.find('h2', clacc_= 'titlu-anunt'):
            #     href_flat = item_block_name.find('a', class_='titlu-anunt').get('href')
            #     print(item_block_name)# print('second href', href_flat)
            dez = len(name_anunt.split(':'))
            if dez == 2:
                dezvoltator = name_anunt.split(':')[0]
                dict_caracter['80_dezvoltator'] = dezvoltator
                keys_list.append('80_dezvoltator')
                # print(dict_caracter)
            else:
                dezvoltator = 'Nope'
                dict_caracter['80_dezvoltator'] = dezvoltator
                keys_list.append('80_dezvoltator')
                # print(dict_caracter)
        # print(dict_caracter)
            # print(dezvoltator)
            if item_block_name.find('p', class_= 'location_txt'):
                # f1 = find('\n')
                location_txt1 = item_block_name.find('p', class_= 'location_txt').text.strip()
                if len(location_txt1.split('\n')) == 1:
                    location_txt = item_block_name.find('p', class_= 'location_txt').text.strip()
                elif len(location_txt1.split('\n')) == 2:
                    location_txt = item_block_name.find('p', class_='location_txt').text.strip().split('\n')[0].strip()
                    portal_metro2 = item_block_name.find('p', class_='location_txt').text.strip().split('\n')[1].strip()
                dict_caracter['09_location_txt'] = location_txt
                keys_list.append('09_location_txt')
                
            if item_block_name.find('div', class_= 'metrou'):
                portal_metro = item_block_name.find('div', class_='metrou').find('span').text
                dict_caracter['10_portal_metro'] = portal_metro
                keys_list.append('10_portal_metro')
                
                distance_to_metro = int(portal_metro.split(' m ')[0])
                dict_caracter['11_distance_to_metro'] = distance_to_metro
                keys_list.append('11_distance_to_metro')
                
                time_to_metro = int(portal_metro.split(' m ')[1].replace('(', '').replace(' minute)', '').replace(' minut)', ''))
                dict_caracter['12_time_to_metro'] = time_to_metro
                keys_list.append('12_time_to_metro')
                
            elif len(location_txt1.split('\n')) == 2:
                # print(location_txt1)
                portal_metro = portal_metro2 #item_block_name.find('p', class_='location_txt').text.strip().split('\n')[1].strip()
                dict_caracter['10_portal_metro'] = portal_metro
                keys_list.append('10_portal_metro')
                
                distance_to_metro = int(portal_metro.split(' m ')[0])
                dict_caracter['11_distance_to_metro'] = distance_to_metro
                keys_list.append('11_distance_to_metro')
                
                time_to_metro = int(portal_metro.split(' m ')[1].replace('(', '').replace(' minute)', '').replace(' minut)', ''))
                dict_caracter['12_time_to_metro'] = time_to_metro
                keys_list.append('12_time_to_metro')
                
            else:
                portal_metro = 'Nope'
                dict_caracter['10_portal_metro'] = portal_metro
                keys_list.append('10_portal_metro')
                
                distance_to_metro = 'Nope'
                dict_caracter['11_distance_to_metro'] = distance_to_metro
                keys_list.append('11_distance_to_metro')
                time_to_metro = 'Nope'
                dict_caracter['12_time_to_metro'] = time_to_metro
                keys_list.append('12_time_to_metro')
                
            # print(portal_metro, ' == ', distance_to_metro, ' === ', time_to_metro)
            if item_block_name.find('div', class_= 'pret'):
                # print(item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare'))
                if item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare'):
                    price_all = float(item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare').text.replace('.', '').replace(',', '.'))
                    dict_caracter['13_price_all'] = price_all
                    keys_list.append('13_price_all')
                    
                else:
                    price_all = float(0)
                    dict_caracter['13_price_all'] = price_all
                    keys_list.append('13_price_all')
                    
                # print(price_all, type(price_all))
            if item_block_name.find('ul', class_= 'caracteristici'):
                n_c = item_block_name.find('ul', class_= 'caracteristici').text.strip().replace('\n', '|').replace(',', '.').replace('|||', ',').replace('||', ',').replace('|', ',').split(',')
                # print(n_c)
                for i in n_c:
                    if i.find('camer') != -1 or i.find('cam') != -1:
                        nnn = 'camr'+i
                    elif i.find('utili') != -1:
                        nnn = 'util' + i
                    else:
                        nnn = '' + i
                    if keys_caracter[nnn[:4]]:
                        keys_key = keys_caracter[nnn[:4]]
                        dict_caracter['90_'+keys_key] = i
                        keys_list.append('90_'+keys_key)
                        # print(keys_key, '|<= value = |', i)
            elif item_block_name.find('div', class_='swiper-wrapper'):
                n_c2 = item_block_name.find('div', class_='swiper-wrapper').text.strip().replace('\n', '|').replace(',', '.').replace('||||||', ',').replace('  ', 'Etaj ').replace('mp', 'mp utili').replace('Dec.', 'Decomandat')
                n_c1 = n_c2.replace('Semidec.', 'Semidecomandat').replace('Nedec.', 'Nedecomandat').replace('o cam.', '1 cam.').replace('cam.', 'camere')
                if n_c1 != '':
                    n_c = n_c1.split(',')
                for i in n_c:
                    i = i.strip()
                    if i.find('camer') != -1 or i.find('cam') != -1:
                        nnn = 'camr'+i
                    elif i.find('utili') != -1:
                        nnn = 'util' + i
                    else:
                        nnn = '' + i
                    if keys_caracter[nnn[:4]]:
                        keys_key = keys_caracter[nnn[:4]]
                        dict_caracter['90_' + keys_key] = i
                        keys_list.append('90_' + keys_key)
                        # print(keys_key,  '|<= value = |', i)
            
            # print('! ===', n_c)
                    # print(squere_flat)
                    # print(f'{count_flat} | bloc !!! {bloc} !!! numer_camer - {len(n_c)} | {n_c} | href {href_flat} ')
# ИСКЛЮЧИТЬ
            # if item_block_name.find('div', class_='logo-agentie hidden-xs'):
            #     lg = item_block_name.find('div', class_='logo-agentie hidden-xs') #get_text#.find('img', alt='lazyload')
            #     lg2 = str(lg.find('img', class_="lazyload").get_text).replace('img alt="', '|').replace('" class="lazyload"', '|').split('|')
            #     # print(lg2)
            #     logo = lg2[1]
            # else:
            #     logo = 'Nope'
# ИСКЛЮЧИТЬ
#             print(count_number_anunt, '==', dict_caracter) # ======================
            keys = list(set(keys_list))
            keys.sort()
            # print(keys)
            # values = [count11, count_number_anunt, name_anunt, parsing_day, numer_camere, dezvoltator, href_flat, orasul, location_txt,
            #                distance_to_metro, time_to_metro, price_all, metri_patrati, apart_etaj, casa_etaj,
            #                compart, bloc, logo]
            #         # count_flat += 1
            dict_href1 = {i: j for i, j in zip(keys_anunt_href, list_anunt_href)}
            dict_href.append(dict_href1)
            # dict1 = {x: y for x, y in zip(keys, values)}
            # count_flat_0 += 1
            dict_chief.append(dict_caracter)
            # print(dict_href)
    print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{dict_camere_days[input_page_numer_apart]}_{parsing_day}')
    count11 += 1
# print(dict_href)
# '================================================================'
with open (fr'C:\Python mini\venv\data_imobiliare\CSV imobiliare first and href\csv_file_{parsing_day}_list_HREF_anunt_IMOBILIARE_RO.csv', 'a', encoding='utf-8', newline='\n') as csv_file_href:
    fieldname = keys_anunt_href
    writer = csv.DictWriter(csv_file_href, fieldnames=fieldname)
    writer.writeheader()
    for i in dict_href:
        writer.writerow(i)
# print(keys)
# print('D I C T --------------', dict_chief)

with open(fr'C:\Python mini\venv\data_imobiliare\CSV imobiliare first and href\{parsing_day}_csv_IMOBILIARE_page_parsing.csv', 'a', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)
# '======================================================================='



