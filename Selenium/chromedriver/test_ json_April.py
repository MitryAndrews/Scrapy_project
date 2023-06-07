import time
from datetime import date
import requests
import json
import xmltodict
import os

now = date.today()
start =100
step = 100 
num_page = 100
count = 1*step
list_file = []

path = fr'C:\Users\user\Scrapy_project\April_out_json'

for i in range(1, 1000, step):
    name_file = fr'{count}_{step}_april_{now}_out.txt'
    file_in = fr'{path}\{name_file}'
    
    list_file.append(file_in)

    # print(file_in)
print(list_file)
cnt = 0
for file_json in list_file:
    with open(fr'{file_json}', encoding='utf-8') as f:
        file_contect = f.read()
        templates = json.loads(file_contect)
        # cnt += 1
        # print(len(templates))
        # print()
        # print('========================================')
        # print()
for i in templates:
    print('========================================')
    for k, v in i.items():
      print('key -', k, 'value -', v)  
    # print(i)
    # print()
    # print('========================================')
    print()





