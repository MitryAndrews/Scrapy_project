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
path = fr'C:\Users\user\Scrapy_project'
path2 = fr'C:\Users\user\Scrapy_project\April_out_json'
words1 = '<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">'
words2 = '</pre></body></html>'
for i in range(1, 1000, step):
    name_file = f'{count}_{step}_april_{now}.txt'
    name_file2 = f'{count}_{step}_april_{now}_out.txt'
    file_in = path+'\\'+name_file
    file_out = path2+'\\'+name_file2
    list_file.append(file_in)
    
    with open(file_in, encoding='utf-8') as infile, open(file_out, "w", encoding='utf-8') as outfile:
        for line in infile:
            line = line.replace(words1, '').replace(words2, '')
            outfile.write(line)
            print('records line')
    count += step
    # print(file_in)
# print(list_file)


