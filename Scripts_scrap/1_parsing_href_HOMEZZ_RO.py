import time
from typing import Dict
import datetime
import requests
from bs4 import BeautifulSoup
import json
import csv
from random import choice
from random import uniform
from fake_useragent import UserAgent

# parsing_day = str(input('input parsing day'))
parsing_day = '2022-06-23'
user_agent = UserAgent()
list_of_href_imobiliare = []
# C:\Python mini\venv\data_imobiliare\CSV imobiliare first and href\
with open(fr'C:\Python mini\venv\data_homezz\CSV HOMEZZ first and href\csv_file_{parsing_day}_list_HREF_anunt_HOMEZZ_RO_1.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    for i in reader:
        # print(i[0])
        list_of_href_imobiliare.append(i[1])
start_page = 10900 #int(input('Введите номер первой страницы - '))
stop_page = 3 #int(input('Введите номер последней страницы - '))
# list_of_href_imobiliare = list(set(list_of_href_imobiliare))
# parsing_day = datetime.datetime.today().strftime('%Y-%m-%d')
number_of_pages = len(list_of_href_imobiliare)
item_value = list_of_href_imobiliare[start_page : number_of_pages + 1]
# number_selection = int(input('Введите с какой страницы начинаем - '))
item_key = [f'{i}_страница_HOMEZZ_RO_{parsing_day}' for i in range(start_page, number_of_pages + 1)]
# item_value = [f'https://www.avito.ru/astrahan/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQAkDmBxSMUsoIpIpZmqwBmKwBlqwBlKwBiFmGWYRZglmAWQ&p={i}' for i in range(number_selection, number_of_pages + 1)]
item_dict = {x: y for x, y in zip(item_key, item_value)}
# print(item_dict)
with open(f'href_{parsing_day}_HOMEZZ_RO.json', 'w') as fp:
    json.dump(item_dict, fp)
proxy_agent_keys = []
proxy_agent_values = []
dict_proxy_agent_chief = []
with open(f'href_{parsing_day}_HOMEZZ_RO.json', 'r') as fp:
    item_dict_json = json.load(fp)
print(item_dict_json)
#
agent_list = open(r'C:\Python mini\venv\User_Agent_list_2.txt').read().split('\n')
proxy_list = open(r'C:\Python mini\venv\proxies.txt').read().split('\n')
proxy_list2 = []
for i in proxy_list:
    prox = i.replace('п»ї', '')
    print(prox)
    proxy_list2.append(prox)
count = start_page
count_time = 1
for item_key, item_value in item_dict_json.items():
    proxy = {'http': 'http://' + choice(proxy_list2)}
    agent = {'User-Agent': choice(agent_list)}
    # print(proxy, agent)
    print('Парсинг - ', count, 'страницы', item_value, 'proxy - ', proxy, 'user-agent - ', agent)
    if count_time % 100 == 0:
        aa = 7
        bb = 10
    else:
        aa = 4
        bb = 6
    time.sleep(uniform(aa, bb))
    ## print('# = ', count, ' keys - ', item_key, ' value -', item_value)
    req = requests.get(item_value, headers=agent, proxies=proxy)
    if req.status_code == 200:
        src = req.text
        with open(fr'D:\Archive HOMEZZ romania anunt\data_homezz_href_anunt\2022-06-23\{count}_страница_href_IMOBILIARE_{parsing_day}.html', 'w', encoding='utf-8') as file:
            file.write(src)
        print('thats OK')
    else:
        print('Error', req.status_code)
    count += 1
    count_time += 1
#     dict_proxy_agent = {x:y for x, y in zip(proxy_agent_keys, proxy_agent_values)}
#     dict_proxy_agent_chief.append(dict_proxy_agent)
# with open('proxy_agent_list.csv', 'a', encoding='utf-8', newline='\n') as file_csv_proxy:
#     fieldnames = ['proxy', 'agent']
#     writer = csv.DictWriter(file_csv_proxy, fieldnames= fieldnames)
#     for i in dict_proxy_agent_chief:
#         writer.writerow(i)
