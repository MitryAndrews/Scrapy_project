import time
from datetime import date
import os, fnmatch
import shutil
from time import sleep
from random import choice, uniform
from selenium import webdriver
import csv
import json
now = date.today()
# now = '2022-12-28'
now = '2023-05-07'
dirname_from = fr'C:\Users\user\Scrapy_project\Archive_April'
files = os.listdir(dirname_from)
# files = os.walk(dirname_from)
pattern = f"*{now}.txt"
# print(files)
url1 = f'https://apteka-april.ru/'
path1 = fr'C:\Users\user\Scrapy_project\Archive_April'
path2 = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_json'
start =100
step = 100 
num_page = 100
count = 1*step
total_count = 1200
text_1 = '<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">'
text_2 = '</pre></body></html>'
for i in files:
    if fnmatch.fnmatch(i, pattern):
        print(path1+'\\'+i)#i)
for i in files:
    if fnmatch.fnmatch(i, pattern):
        name_file = path1+'\\'+i
        name_file2 = path2+'\\'+i.replace('.txt', '')+'_RE'+'.txt'
        print(name_file)
        print(name_file2)
        with open(name_file, 'r', encoding='utf-8') as file:
            file_data = file.read()
        # Replace the target string
            file_data = file_data.replace(text_1, '')
            file_data = file_data.replace(text_2, '')

    # Write the file out again
        with open(name_file2, 'w', encoding='utf-8') as file:
            file.write(file_data)
