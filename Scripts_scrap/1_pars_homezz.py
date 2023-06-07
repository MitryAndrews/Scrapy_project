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
from look_ip import get_location
user_agent = UserAgent()
parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
parsing_day = '2022-06-23'
number_selection = int(input('Введите с какой страницы начинаем - '))
number_of_pages = int(input('Введите кол-во страниц парсинга - '))
# input_page_numer_apart = str(input('Choise number page 1-2 camera 30 days: input 1 OR 3-4+ camera 30 days: input 2 = '))
# dict_camere_days = {'1': '1_2 camera 30 days', '2': '3_4 camera 30 days'}
# dict_list_orasul = {'bucuresti-ilfov 1-2 cam': 'https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=283747521&pagina=',
#                     'bucuresti-ilfov 3-4 cam': 'https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=283747967&pagina=',
#                     'cluj tot jud 1-2 cam': 'https://www.imobiliare.ro/vanzare-apartamente/cluj?id=55730410&pagina=',
#                     'cluj tot jud 3-4 cam': 'https://www.imobiliare.ro/vanzare-apartamente/cluj?id=78665944&pagina='}
# dict_page_numer_apart = {'1': f'https://www.imobiliare.ro/vanzare-apartamente/iasi?id=76295772&pagina=',
#                          '2': f'https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=283747967&pagina='}
item_key = [f'{i} страница' for i in range(number_selection, number_of_pages + 1)]
item_value = [f'https://homezz.ro/anunturi_apartamente_de-vanzare_fara-poze_{str(i)}.html' for i in range(number_selection, number_of_pages + 1)]
# print('key - ', item_key, ' == value - ', item_value)
item_dict = {x: y for x, y in zip(item_key, item_value)}

with open('href_homezz_ro.json', 'w') as fp:
    json.dump(item_dict, fp)

with open('href_homezz_ro.json', 'r') as fp:
    item_dict_json = json.load(fp)
# print(item_dict_json)

agent_list = open(r'C:\Python mini\venv\User_Agent_list_2.txt').read().split('\n')
proxy_list = open(r'C:\Python mini\venv\proxies.txt').read().split('\n')
proxy_list2 = []
for i in proxy_list:
    prox = i.replace('п»ї', '')
    print(prox)
    proxy_list2.append(prox)
count = number_selection
for item_key, item_value in item_dict_json.items():
    proxy = {'http': 'http://' + choice(proxy_list2)}
    agent = {'User-Agent': f'{user_agent.random}'}
    print(proxy, agent)
    #ip_current = get_location(url='https://2ip.ru')
    print(f'Парсинг - {count}, страницы {item_value}; user-agent - {agent}')#, ip_current - {ip_current}; proxy - {proxy}')
    if count % 5 == 0:
        print('CANGE IP 5 (in 10 sec?)')#, ip_current
        time.sleep(uniform(7, 10))
    elif count % 10 == 0:
        print('CANGE IP 10 (in 10 sec?)') #, ip_current
        time.sleep(uniform(10, 13))
    else:
        time.sleep(uniform(5, 8))
    # print('# = ', count, ' keys - ', item_key, ' value -', item_value)
    req = requests.get(item_value, headers=agent, proxies=proxy)
    if req.status_code == 200:
        src = req.text
        with open(fr'C:\Python mini\venv\data_homezz\data_homezz_anunt\{count}_{item_key}_HOMEZZ_RO_ALL_{parsing_day}.html', 'w', encoding='utf-8') as file:
            file.write(src)
        print('thats OK')
    else:
        print('Error', req.status_code)
    count += 1


