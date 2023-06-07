import time
from datetime import date
import requests
import json
import xmltodict

now = date.today()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
# start =100
# step = 100 
# num_page = 100
# count = 1*step
# for i in range(1, 1000, step):
#     a = f'0{count}_{count+step}_april_{now}' if len(str(count))==1 else f'{count}_{count+step}_april_{now}'
#     url = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=2552&subtypeSlugs=%22obezbolivayushchie_protivovospalitelnye_sredstva%22&cityID=57974%5B{count}:{step}%5D'
#     response = requests.get(url=url, headers=headers)
#     print(a)
#     count += step

dict_url = {
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/': 35, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/': 30,
    'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/': 36, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/': 71
    }
str_add = '?&page_count='
list_url = ['https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/'
               'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/']

# print(len(xx1))
# print(xx1[-2])
path = fr'C:\Users\user\Scrapy_project\Archive_Vita'
# count = 1
# for k, v in dict_url.items():
#     count = 1
#     for i in range(v):
#         url_2 = k+str_add+str(count)
#         group = url_2.replace('//', '').split('/')[3]
#         name_file = f'0{count}_VITA_{group}_{now}.html' if len(str(count))==1 else f'{count}_VITA_{group}_{now}.html'
#         path_file = path+'\\'+name_file
#         print(path_file)
#         count +=1
start =100
step = 100 
num_page = 100
count = 1*step
x1 = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=3872&subtypeSlugs=%22sredstva_dlya_lecheniya_prostudy_i_grippa%22&cityID=57974%5B'
x2 = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=2552&subtypeSlugs=%22obezbolivayushchie_protivovospalitelnye_sredstva%22&cityID=57974%5B'
x3 = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=2555&subtypeSlugs=%22zheludochnokishechnye_sredstva%22&cityID=57974%5B'
x4 = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=2559&subtypeSlugs=%22serdechnososudistaya_sistema%22&cityID=57974%5B'
y1 = 600
y2 = 800
y3 = 600
y4 = 1200
list_url = [x1, x2, x3, x4]
list_num = [y1, y2, y3, y4]
dict_url = {k: v for k, v in zip(list_url, list_num)}
print(dict_url)
for k, v in dict_url.items():
    count = 1*step
    for j in range(1, v, step):
        tail = f'{count}:{step}%5D'
        group = k.split('%22')[-2]
        name_file = f'0{count}_{group}_{step}_APRIL_{now}' if len(str(count))==1 else f'{count}_{group}_{step}_APRIL_{now}'
        url2 = k+tail
        # print(url2)
        print(name_file)
        # print('j - ', j, group)
        count += step
        

# url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
# # url = 'https://apteka-april.ru/catalog/396070-lekarstvennye_preparaty_i_bady/3872-sredstva_dlya_lecheniya_prostudy_i_grippa'
# # url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
# str_add = '?&page_count='

# xxx = f'{url}{str_add}{count}'
# print(xxx)
# url = 'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=3872&subtypeSlugs=%22sredstva_dlya_lecheniya_prostudy_i_grippa%22&cityID=57974[100:25]'
# # ===================================
# response = requests.get(url=url, headers=headers )
# src = response.status_code
# d = response.text()
# print('Status code - ', src, d)
# with open(fr'C:\Users\example_content.xml', 'wb') as f:
#     f.write(d)

# with open(fr'C:\Users\example_content.xml', "r", encoding='utf-8') as file:
#     data = xmltodict.parse(file.read())
#     file.close()
 
#     json_data = json.dumps(data)
#     with open(fr"t.json", "w", encoding='utf-8') as json_file:
#         json_file.write(json_data)
#         json_file.close()
# print("Data retrieved")
# print(data)

# with open(f'C:\Users\example.json', 'w', encoding='utf-8') as file:
#             contents = json.loads(file.write())
# print(data)
# word = input('Enter a word:')
# data = requests.get(url + word)
# data = data.text
# try:
#     data_json = json.loads(data)
#     print(data_json)
# except json.JSONDecodeError:
#         print("Empty response")
# data = response.json()
# print(data)
# ===================================
# h = requests.head(url=url, headers=headers)
# header = h.headers
# contentType = header.get('content-type')
# print(contentType)

# s = requests.request('POST', url=url)
# ss = s.head(url=url, headers=headers)
# print(s.text)

# response.encoding = 'utr-8'
# src = response.text
# src = req.text

# with open(fr'C:\Users\example.json', 'w', encoding='utf-8') as file:
#             contents = json.loads(file.write())

# with open(fr'C:\Users\example.json', 'w', encoding='utf-8') as fp:
#     json.dump(data_json, fp)

