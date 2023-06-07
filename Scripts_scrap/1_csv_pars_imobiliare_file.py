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
num_range = 118
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2022-05-10'

# adress_region = 'Астраханская область' #str(input('Введите область поиска - '))
# adress_city = 'Астрахань' #str(input('Введите город поиска - '))
list_name_anunt = []
list_link_anunt = []
list_anunt_href = []
adress_district = ''
print(f'{parsing_day} - begining ')
# print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
count_flat_0 = 1
count_number_anunt =0
dict_chief = []
dict_href = []
keys_anunt_href = ['No', 'anunt', 'orasul', 'href', 'site', 'parsing_day']
for i in range(num_range):
    n_page = count11
    with open(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}.html', encoding='utf-8') as file: #{parsing_day} , encoding='utf-8'
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
        block_name = soup.find_all('div', class_='box-anunt')
        count_flat = 0
        for item_block_name in block_name:   # это блок для ВСЕХ объявлений!!!!!!!
            if item_block_name.find('h2', class_='titlu-anunt hidden-xs'):
                block_anunt = item_block_name.find('h2', class_='titlu-anunt hidden-xs')
                href_flat = item_block_name.find('h2', class_='titlu-anunt hidden-xs').find('a', itemprop = 'name').get('href') #'https://www.avito.ru' + item_block_name.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
                orasul = href_flat.split('/')[4].strip().upper()
                # print(len(orasul), orasul)
                name_anunt = item_block_name.find('h2', class_='titlu-anunt hidden-xs').find('span').text
                # print(name_anunt)
                count_number_anunt += 1
                list_anunt_href = [count_number_anunt, name_anunt, orasul, href_flat, 'imobiliare_ro', parsing_day]
                count_flat += 1
            dez = len(name_anunt.split(':'))
            if dez == 2:
                dezvoltator = name_anunt.split(':')[0]
            else:
                dezvoltator = 'Nope'
            # print(dezvoltator)
            if item_block_name.find('p', class_= 'location_txt'):
                location_txt = item_block_name.find('p', class_= 'location_txt').text.strip()
            if item_block_name.find('div', class_= 'metrou'):
                portal_metro = item_block_name.find('div', class_='metrou').find('span').text
                distance_to_metro = int(portal_metro.split(' m ')[0])
                time_to_metro = int(portal_metro.split(' m ')[1].replace('(', '').replace(' minute)', '').replace(' minut)', ''))
            else:
                distance_to_metro = 'Nope'
                time_to_metro = 'Nope'
                portal_metro = 'Nope'
                # print(distance_to_metro, time_to_metro)
            if item_block_name.find('div', class_= 'pret'):
                # print(item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare'))
                if item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare'):
                    price_all = float(item_block_name.find('div', class_='pret').find('span', class_= 'pret-mare').text.replace('.', '').replace(',', '.'))
                else:
                    price_all = float(0)
                # print(price_all, type(price_all))
            if item_block_name.find('ul', class_= 'caracteristici'):
                n_c = item_block_name.find('ul', class_= 'caracteristici').text.strip().replace('\n', '|').replace('|||', ',').replace('||', ',').replace('|', ',').split(',')
                print(n_c)
                if n_c[1][-4:-1] == ' ca':
                    nnn = n_c.pop(1)
                if n_c[0][-6:-1] == 'camer':
                    numer_camere = n_c[0].replace('o', '1')
                    # print(numer_camere)
                     #No -  {count_flat} | numer_camer - {len(numer_camer)} =
                if n_c[1][-5:-1] == 'util':
                    try:
                        metri_patrati = float(n_c[1].replace(' mp utili', ''))
                    except:
                        metri_patrati = float(0)
                    # print(metri_patrati, ' - ', type(metri_patrati))
                print(n_c[1], '2- ', n_c[2])
                if n_c[2][0:4] == 'Etaj':
                    etaj = n_c[2].replace('Etaj ', '')
                    print(etaj)
                    if len(etaj.split('/')) == 1:
                        casa_etaj = float(etaj) + 1
                        apart_etaj = float(etaj) +1
                    else:
                        casa_etaj = float(etaj.split('/')[1]) + 1
                        apart_etaj = float(etaj.split('/')[0]) + 1
                elif  n_c[2][0:4] == 'Part':
                    etaj = n_c[2].replace('Parter', '0')
                    if len(etaj.split('/')) == 1:
                        casa_etaj = float(etaj) + 1
                        apart_etaj = float(etaj) +1
                    else:
                        casa_etaj = float(etaj.split('/')[1]) + 1
                        apart_etaj = float(etaj.split('/')[0]) + 1
                elif n_c[1][0:4] == 'Etaj':
                    etaj = n_c[1].replace('Etaj ', '')
                if len(n_c) > 3:
                    if n_c[3][0:4] == 'Deco':
                        compart = 'Decomandat'
                    elif n_c[3][0:4] == 'Semi':
                        compart = 'Semidecomandat'
                    else:
                        compart = 'Nope'
                else:
                    compart = 'Nope'
                if len(n_c) == 6:
                    nn = n_c.pop(4)
                if len(n_c) == 5:
                    if n_c[4] == 'Bloc nou':
                        bloc = 'Bloc nou'
                elif len(n_c) == 4:
                    bloc = 'Bloc veche'
                else:
                    bloc = 'Nope'
                # print(f'{count_flat} | bloc !!! {bloc} !!! numer_camer - {len(n_c)} | {n_c} | href {href_flat} ')
            if item_block_name.find('div', class_='logo-agentie hidden-xs'):
                lg = item_block_name.find('div', class_='logo-agentie hidden-xs') #get_text#.find('img', alt='lazyload')
                lg2 = str(lg.find('img', class_="lazyload").get_text).replace('img alt="', '|').replace('" class="lazyload"', '|').split('|')
                # print(lg2)
                logo = lg2[1]
            else:
                logo = 'Nope'
            # print(f'N {count_flat}: parsing_day {parsing_day} \n name_anunt {name_anunt}, numer_camere {numer_camere}, dezvoltator {dezvoltator}, '
            #          f'href_flat {href_flat}, location_txt {location_txt}, distance_to_metro {distance_to_metro}, time_to_metro {time_to_metro}, '
            #          f'price_all {price_all}, metri_patrati {metri_patrati}, apart_etaj {apart_etaj}, '
            #          f'casa_etaj {casa_etaj}, compart {compart}, bloc {bloc}, logo {logo}.  ')
            # print(numer_camere ,' - ', name_anunt)
                # print(f'{count_flat} | numer_camer - {len(n_c)} | {n_c}')

            # count_flat += 1
    # print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
    # count11 += 1
    
            values = [count11, count_number_anunt, name_anunt, parsing_day, numer_camere, dezvoltator, href_flat, orasul, location_txt,
                           distance_to_metro, time_to_metro, price_all, metri_patrati, apart_etaj, casa_etaj,
                           compart, bloc, logo]
                    # count_flat += 1
            dict_href1 = {i: j for i, j in zip(keys_anunt_href, list_anunt_href)}
            dict_href.append(dict_href1)
            dict1 = {x: y for x, y in zip(keys, values)}
            count_flat_0 += 1
            dict_chief.append(dict1)
            # print(dict_href)
    print(fr'C:\Python mini\venv\data_imobiliare\{count11}_{count11} страница_IMOBILIARE_RO_{parsing_day}')
    count11 += 1
# print(list_name_anunt, ' ----', list_link_anunt)
with open (f'csv_file_{parsing_day}_list_HREF_anunt_IMOBILIARE_RO.csv', 'w', encoding='utf-8', newline='\n') as csv_file_href:
    fieldname = keys_anunt_href
    writer = csv.DictWriter(csv_file_href, fieldnames=fieldname)
    writer.writeheader()
    for i in dict_href:
        writer.writerow(i)
        
#
#     print('Ends of - page # :', count11)
#     count11 += 1
#     print(' --------------------------------------------')

# print('D I C T --------------', dict_chief)
#     #
with open(fr'csv_IMOBILIARE_page_parsing_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)




