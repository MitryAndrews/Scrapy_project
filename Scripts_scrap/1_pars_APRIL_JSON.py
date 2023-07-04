import time
import pandas as pd
from datetime import date
import os, fnmatch
from collections import Counter
from collections import defaultdict
import shutil
from time import sleep
from random import choice, uniform
from selenium import webdriver
import csv
import json
parsing_day = '2022-12-28'
parsing_day = '2023-05-07'
parsing_day = '2023-06-27'
dirname_from = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_json'
files = os.listdir(dirname_from)
# files = os.walk(dirname_from)
pattern = f"*{parsing_day}_RE.txt"
# print(files)
now = date.today()
now = '2022-12-28'
now = '2023-05-07'
now = '2023-06-27'
url1 = f'https://apteka-april.ru/'
path1 = fr'C:\Users\user\Scrapy_project\Archive_April'
path2 = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_json'
start =100
step = 100 
num_page = 100
count = 1*step
list_typeID = [5, 6, 8, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 222]
price_dict = {'price_withCard': 0, 'price_withPeriod':0, 'price_withoutCard': 0} 
keys_price = ['count_index', 'name_item_price', 'parsing_day', 'price_withCard', 'price_withPeriod', 'price_withoutCard']
typeID = {
    5: 'Нозология', 6: 'Действующее вещество', 8: 'Группа товара', 10: 'Бренд', 13: 'Производитель', 14: 'Other',
    15: 'Страна', 16: 'Форма выпуска', 17: 'Рецепт', 18: 'Условия хранения', 19: 'Действующее вещество, сборное название',
    20: 'Состав, вес (кратко)', 21: 'Фармакотерапевтическая группа', 222: 'Количество в упаковке'
              }
properties_dict = {'Нозология': [], 'Действующее вещество': [], 'Группа товара': [], 'Бренд': [], 'Производитель': [],
                          'Страна': [], 'Форма выпуска': [], 'Рецепт': [], 'Условия хранения': [], 'Действующее вещество, сборное название': [],
                          'Состав, вес (кратко)': [], 'Фармакотерапевтическая группа': [], 'Количество в упаковке': [], 'Other': []}
keys_prop = ['count_index', 'name_item_prop', 'parsing_day','Нозология', 'Действующее вещество', 'Группа товара', 'Бренд', 'Производитель',
                          'Страна', 'Форма выпуска', 'Рецепт', 'Условия хранения', 'Действующее вещество, сборное название',
                          'Состав, вес (кратко)', 'Фармакотерапевтическая группа', 'Количество в упаковке', 'Other']
list_item_group = []
list_file = []

for i in files:
    if fnmatch.fnmatch(i, pattern):
        i.replace('.txt', '') + '_RE' + '.txt'
        name_file = path1+'\\'+i
        name_file2 = path2+'\\'+i
        name_file3 = fr'{path2}\{i}'
        print(name_file3)
        list_file.append(name_file3)
# print(len(list_file))#, '=====', list_file)
count_name = 0
count_file = 0
list_typeID = []
list_keys = []
list_value = []
dict_chief = []
dict_type_ID_1 = {5: 0, 6: 0, 8: 0, 10: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17:0, 18: 0, 19: 0, 20: 0, 21: 0, 222: 0}
dict_prop_chief = []
dict_price_chief = []
count_index = 1
price = {'price_withCard': 0, 'price_withPeriod':0, 'price_withoutCard': 0}
for f in list_file:#[:2]:
    # print(f)
    count_file += 1
    with open(f, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        # count_index = 1
        for i in data:
            # print('========================================')
            print(i)
            # print('file >>>', f, ' || ', 'file_split >>>', f.split('_')[4])
            for ii in i:
                list_keys.append(ii)
                #print(ii)
            try:
                name_item = i['name']
            except TypeError:
                name_item = 'None'
                # print('None item')
            dict1 = i
            # print( 'this is ', f.split('_')[4])#['group'])
            dict1['group'] = f.split('_')[4] 
            count_index_total = f'{count_index}_{parsing_day}'
            dict1['count_index'] = count_index_total
            dict_chief.append(dict1)
            # count_index += 1
            # print('name = >', name_item, '>>>>>>', dict1) #, '\n', '========properties========', '\n', jj['name'])
            # for k, v in i.items():
            #     print(k, '>>>>>', v)
                # for k, v in g.items():
                #     print(k, v)
            try:
                properties = i['properties']
            except TypeError:
                a = 1
                # print('None item')
            try:
                price = i['price']
                x_price = 0
                # print(price)
            except:
                x_price = 999111999
                # print('None item')
            count_name += 1
            count_typeID = 1
            list_item_ID = []
            list_rec =[]
            properties_dict = {'Нозология': [], 'Действующее вещество': [], 'Группа товара': [], 'Бренд': [], 'Производитель': [],
                          'Страна': [], 'Форма выпуска': [], 'Рецепт': [], 'Условия хранения': [], 'Действующее вещество, сборное название': [],
                          'Состав, вес (кратко)': [], 'Фармакотерапевтическая группа': [], 'Количество в упаковке': [], 'Other': []}
            for j in properties:
                list_typeID.append(j['typeID'])
                list_item_ID.append(j['typeID'])
                prop_value = j['name']
                prop_name = typeID[j['typeID']]
                properties_dict['count_index'] = count_index_total
                properties_dict['name_item_prop'] = name_item
                properties_dict['parsing_day'] = parsing_day
                properties_dict[prop_name].append(prop_value)
                if len(properties) == count_typeID:
                    dict_prop_chief.append(properties_dict)
                    # print('== new_name_item ==')
                    # print('name_item', name_item, '=== properties_dict ===', properties_dict)# prop_name, '====', prop_value)#, '====',typeID[j['typeID']], ' =|= ', yyy)
                count_typeID += 1
            price_dict = {'price_withCard': 0, 'price_withPeriod':0, 'price_withoutCard': 0}         
            count_price = 1
            for k, v in price.items():
                # print('===price===price=============')
                # print(name_item, ' === price_'+k, v, type(price))
                price_dict['count_index'] = count_index_total
                #print('count_index ----->', count_index_total)
                price_dict['name_item_price'] =  name_item
                price_dict['parsing_day'] = parsing_day
                price_dict['price_'+k] = v 
                if count_price == 3 and x_price != 999111999:
                    dict_price_chief.append(price_dict)
                # print (price_dict)
                if count_price == 3 and x_price == 999111999:
                    dict_price_chief.append({'count_index': count_index_total, 'name_item_price': name_item, 'parsing_day': parsing_day, 'price_withCard': 0, 'price_withPeriod':0, 'price_withoutCard': 0})
                count_price += 1
                # print(j['name'], ' === ', j['typeID'])
            count_index += 1
list_typeID = list(set(list_typeID))
#list_item_group = list(set(list_item_group))
list_keys = Counter(list_keys)
keys = list(set(list_keys))
keys.append('group')
keys.append('count_index')
# print('list_keys', list_keys)
# print('list_keys2', len(keys), keys)
# print('count_file = ', count_file)
# print('count_name', count_name)
# print('list typeID = ', len(list_typeID), list_typeID, 'dict_type_ID_1', dict_type_ID_1)
'разбивка на группы ==========================================='
prop_dict = {'count_index': '','name_item_prop': '', 'parsing_day': '','Нозология': [], 'Действующее вещество': [], 'Группа товара': [], 'Бренд': [], 'Производитель': [],
                          'Страна': [], 'Форма выпуска': [], 'Рецепт': [], 'Условия хранения': [], 'Действующее вещество, сборное название': [],
                          'Состав, вес (кратко)': [], 'Фармакотерапевтическая группа': [], 'Количество в упаковке': [], 'Other': []}
prop_num_dict = {'count_index': '', 'name_item_prop': '', 'parsing_day': '','Нозология': [], 'Действующее вещество': [], 'Группа товара': [], 'Бренд': [], 'Производитель': [],
                          'Страна': [], 'Форма выпуска': [], 'Рецепт': [], 'Условия хранения': [], 'Действующее вещество, сборное название': [],
                          'Состав, вес (кратко)': [], 'Фармакотерапевтическая группа': [], 'Количество в упаковке': [], 'Other': []}
list_group = []
list_num_group = []
count_total = 0
for d in dict_prop_chief:
    count_total += 1
    for k, v in d.items():
        l = len(v) if type(v) == list else 0
        ll = v if type(v) == list and k == 'Группа товара' else 0
        prop_num_dict[k].append(l) if type(v) == list else 0
        # print(k, l)
        for i in v:
            prop_dict[k].append(i) if type(v) == list else 0
            # print(prop_dict[k])
        #    list_group.append(i) if type(v) == list and k == 'Группа товара' else 0
        # print(len(v), type(v))
        #list_num_group.append(l)
        #print(l, type(v), k, v) if k == 'Группа товара' and l >0 else 'None'#, ' = ', ll)
# print(prop_dict)
# print(prop_dict['Группа товара'])
# counter_x = 
prop_dict2 = {}
#for k, v in price_dict:
    
prop_dict2['Нозология'] = dict(Counter(prop_dict['Нозология']))
print('=================================')
list_need_group = ['Нозология', 'Действующее вещество', 'Группа товара']
#for k, v in prop_num_dict.items():
 #   prop_num_dict[k] = dict(Counter(v))
prop_num_dict = {k: sorted(v) for k, v in prop_num_dict.items()}
prop_num_dict1 = {k: dict(Counter(v)) for k, v in prop_num_dict.items()}    
prop_num_dict2 = {k: {k2: round(v2/count_total, 4) for k2, v2 in v.items()} for k, v in prop_num_dict1.items()}    
print(prop_num_dict2)
print(count_total)
dict_number_group = {}
list_dict_prop_add = []
for k, v in prop_num_dict2.items():
    if k in list_need_group:
        total = 1-v[0]
        count_group = 0
        count_group2 = 0
        del v[0]
        max_num_group = max(list(v))
        print('that - ',k, max(list(v)))
        for k1, v1 in v.items():
            count_group += v1/total#, 4)
            share_num_group = round(k1/max_num_group, 4)
            ratio = count_group / share_num_group#, 4)
            if count_group <= 2: #count_group < 0.86 or v[max_num_group] > 0.35: #share_num_group >= count_group or count_group2 == k1:
                num_group = k1
                count_group2 += 1
            # num_group2 = k1 if count_group < 0.85 or share_num_group >= count_group else 0 
                print('count_group2 - ', count_group2, 'num_group - ', num_group, 'k1 - ', k1, ' - count_group - ', count_group,  '- ', share_num_group, ' - share_num_group', 'ratio = ', ratio)
        dict_number_group[k] = num_group
        
dict_number_group2 = {k.replace('Нозология', 'nosology').replace('Действующее вещество', 'active_ingredient').replace('Группа товара', 'product_group'): v for k, v in dict_number_group.items()}
list_prop_add = []
list_prop_add2 = []
for k, v in dict_number_group2.items():
    for i in range(1,v+1):
        list_prop_add.append(f'{k}_{i}')
        list_prop_add2.append({f'{k}_{i}': ''})
def gen_dict(x, n = 'Ключ'):
    y = []
    y2 = []
    if n != '':
        for k, v in x.items():
            for i in range(1,v+1):
                y.append(f'{k}_{i}')
                y2.append({f'{k}_{i}': ''})
    else:
        for k, v in x[n].items():
            for i in range(1,v+1):
                y.append(f'{k}_{i}')
                y2.append({f'{k}_{i}': ''})
    return y

print('list_prop_add ===+++===> ', list_prop_add)
print('list_prop_add2 ===+++===> ', list_prop_add2)
print()
print('=================================================================')
print('dict_number_group', dict_number_group)
print(list(dict_number_group2.keys()))
name_translate = {k: v for k, v in zip(list(dict_number_group.keys()), list(dict_number_group2.keys()))}
print('name_translate ==> ', name_translate)                  
print('=====================================================================')
print('keys_prop - >', keys_prop)
dict_prop_add = {k: [] for k in list_prop_add}
dict_prop_add2 = {k: '' for k in list_prop_add}
print()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('dict_prop_add +++ ====> ', dict_prop_add)
print('dict_prop_add2 +++ ====> ', dict_prop_add2)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('dict_number_group2', dict_number_group2)
# print('wow - ', [k+str(i) for i in range(1, v) for k, v in dict_number_group.items()])
#list_prop_dict = [{k: v for k, v in }]
keys_prop.extend(list_prop_add)
print('=======KEYS=====KEYS====KEYS====KEYS====')
print('keys_prop - >', keys_prop)
print('=======KEYS=====KEYS====KEYS====KEYS====')

example = gen_dict(dict_number_group, 'Нозология')
example2 = [k.replace('Нозология', 'nosology').replace('Действующее вещество', 'active_ingredient').replace('Группа товара', 'product_group') for k in example]
print('example = ', example2)

""" dict_prop_chief - list of the dict where every dict is a string of a data base
    in the dict (string) we have to update with new elements concicting of product 
    classification groups. 
"""
'++++++++++++++++++++++=============='
# def check_dict(name_item_prop, name_change):
#     for j in name_item_prop:
#            name_change2[f'{name_change}_{name_item_prop.index(j)+1}'] = j
#     return name_change2
def check_dict_global(dict_number_group):
   name_change2 = {}
   for group in dict_number_group:
       name_item_prop = i[group]
       name_change = name_translate[group]
       num_change = dict_number_group[group]
       len_name_item_prop = len(name_item_prop)
       dict_pattern[name_change] = len_name_item_prop
       dict_pattern_list = gen_dict(dict_pattern)
    #    name_change2 = {}
       for j in name_item_prop:
           name_change2[f'{name_change}_{name_item_prop.index(j)+1}'] = j
   return name_change2
for i in dict_prop_chief:
   #print(i)
   i.update(dict_prop_add2)
   dict_pattern = {}
   dict_pattern_list = []
   name_change2 = check_dict_global(dict_number_group)
   dict_temp = {}
   #print('name_change2 +++++========> ', name_change2)
   #for k, v in name_change2.items():
    #   for k2, v2 in dict_prop_add.items():
     #      if v in v2:
      #         dict_temp[k2] = v
       #        dict_prop_add[k2].append(v)
        #       dict_prop_add[k2] = list(set(dict_prop_add[k2]))
            #    print(name_change2.values())
            #    print('dict_temp ++++====>', dict_temp)
            #    print()
            #    print('dict_prop_add===+++===> ', len(dict_prop_add))
         #  else:
          #     dict_temp[k] = v
           #    dict_prop_add[k2].append(v)
            #   dict_prop_add[k2] = list(set(dict_prop_add[k2]))
            #    print('dict_temp ++++====>', dict_temp)
            #    print()
            #    print('dict_prop_add===+++===> ', len(dict_prop_add))
#    print('name_change2 +++++========> ', name_change2)
#    print('dict_prop_add ===########===> ' ,dict_prop_add)
#    for group in dict_number_group:
#        name_item_prop = i[group]
#        name_change = name_translate[group]
#        num_change = dict_number_group[group]
#        len_name_item_prop = len(name_item_prop)
#        dict_pattern[name_change] = len_name_item_prop
#        dict_pattern_list = gen_dict(dict_pattern)
#        print(name_change, ' = ', num_change)
#        print(f'name_change - {name_change} = {num_change} | name_item_prop - {name_item_prop, len(name_item_prop)} | dict_pattern === {dict_pattern} | len_name_item_prop={len_name_item_prop}') 
#        name_change2 = {}
#        name_change2 = check_dict(name_item_prop, name_change)
#        print('name_change2 +++++=====> ', name_change2)
    #    for j in name_item_prop:
    #        x = 99991111999 if len(name_item_prop) == 0 else 0
    #        name_change2[f'{name_change}_{name_item_prop.index(j)+1}'] = j
    #        print('x', x)
    #        print(f'key = {name_change}_{name_item_prop.index(j)+1}, value = {j}')
        # print(j, name_item_prop.index(j)+1)
# with open(fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\test.csv', 'w') as f: 
#     for key in dict_prop_add.keys(): 
#         f.write("%s,%s\n"%(key,dict_prop_add[key]))
count_temp = 0
list_dict_temp = []
list_group_goods = []
list_group_active = []
list_group_nosology = []
for i in dict_prop_chief:
    # print(i['Группа товара'])
    for k, v in i.items():
        x = k[:-2].replace('y_', 'y').replace('t_', 't').replace('p_', 'p')
        if k in dict_number_group.keys():
            count_temp += 1
            # list_dict_temp.append({'N': count_temp})
            for j in v:
                list_group_nosology.append(j) if k == list(dict_number_group.keys())[0] else ''
                list_group_active.append(j) if k == list(dict_number_group.keys())[1] else ''
                list_group_goods.append(j) if k == list(dict_number_group.keys())[2] else ''
                # print(list_group_nosology)
                # print(i['name_item_prop'], ' +++===>', k, v)
        # if x in list(name_translate.values()):
        #     print(v)
print()
print('!!!!!!!!!!!!!!!!!!!!!!!++++++++++++++++++++++==============')
x = (Counter(list_group_nosology))
y = (Counter(list_group_active))
z = (Counter(list_group_goods))
# print('COUNT ITEM TOTAL ===> ', count_temp)
# print(' ===== S E P A R A T E ====== ')
# print(x) 
# print(' ===== S E P A R A T E ====== ')
# print(y) 
# print(' ===== S E P A R A T E ====== ')
# print(z) 
# print('!!!!!!!!!!!!!!!!!!!!!!!++++++++++++++++++++++==============')
list_dict_temp = []
dict_11 = {}
for k, v in z.items():
    dict_11 = {}
    dict_11['group'] = k
    dict_11['num'] = v
    list_dict_temp.append(dict_11)
    # print(k, ' === ', v)

# print(list_dict_temp)
# print('COUNT ITEM TOTAL ===> ', count_temp)
keys_temp = ['group', 'num']
file_csv_temp = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\test_group_prop_APRIL_{parsing_day}.csv'
with open(file_csv_temp, 'w', encoding='utf-8', newline='\n') as csv_file:
    fieldname = keys_temp
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in list_dict_temp:
        writer.writerow(d)
number_group = 5
with open(fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\group_april.csv', 'r', encoding='utf-8', newline='\n') as file_group_goods:
    sreader = csv.reader(file_group_goods, delimiter=';')
    # print(sreader)
    for line in sreader:
        x = 0
        #print(line)#[1], line[2])
print(dict_prop_add2)

#print(dict_prop_chief)
'++++++++++++++++++++++=============='
#     x = 0
#    print(i)

# for i in dict_prop_chief:
#     for j in dict_number_group:
#         x = 0
#         #print(i[j])
# for i in dict_number_group:
#     for j in dict_prop_chief:
#         x = 1
        #print(j[i])
# print(prop_dict2)
#count_list_group = list_group
#list_group = list(set(list_group))

#print(Counter(count_list_group))
'==========================================='
# print('dict_prop_chief ', dict_prop_chief)
# print('dict_price_chief ', dict_price_chief)
file_csv = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\csv_properties_APRIL_index_{parsing_day}.csv'
file_csv_price = fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\csv_price_APRIL_index_{parsing_day}.csv'
#print(list_item_group)
'==========================================='

with open(file_csv, 'w', encoding='utf-8', newline='\n') as csv_file:
    fieldname = keys_prop
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_prop_chief:
        writer.writerow(d)

with open(file_csv_price, 'w', encoding='utf-8', newline='\n') as csv_file:
    fieldname = keys_price
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_price_chief:
        writer.writerow(d)

with open(fr'C:\Users\user\Scrapy_project\Archive_April\APRIL_csv\csv_APRIL_page_parsing_index_{parsing_day}.csv', 'w', encoding='utf-8', newline='\n') as csv_file:  #encoding='utf-8',
    fieldname = keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    for d in dict_chief:
        writer.writerow(d)
