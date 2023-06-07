import undetected_chromedriver as uc
# import seleniumwire.undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
from time import sleep
from random import choice, uniform
from selenium import webdriver
from fake_useragent import UserAgent
import random
proxy_list2 = ['45.130.70.64:8000', '45.130.69.212:8000', '45.130.71.208:8000']
# proxy = {'http': 'http://' + choice(proxy_list2)}#это старый код
proxy = choice(proxy_list2)

useragent = UserAgent()
user_agent = useragent.random
# user_agent = user_agent["google chrome"]
print(f"{user_agent=}")
print(f'{proxy}')
options = uc.ChromeOptions()
options = uc.options.ChromeOptions()
options.add_argument(f'--proxy-server={proxy}')
options.add_argument(f'--user-agent={user_agent}')
options.add_argument(f"--disable-popup-blocking")
options.add_argument(f"--disable-notifications")
now = date.today()
path_ = fr'C:\Users\mitry\Scraping\Archive_test'
url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
url = 'https://vitaexpress.ru/'
url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
url = 'https://awebanalysis.com/ru/what-is-my-ip-address/'
# url = 'https://2ip.ru/'
# url = 'https://apteka-april.ru/catalog/396070-lekarstvennye_preparaty_i_bady/3872-sredstva_dlya_lecheniya_prostudy_i_grippa'
# url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
# url = 'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=3872&subtypeSlugs=%22sredstva_dlya_lecheniya_prostudy_i_grippa%22&cityID=57974[100:25]'
str_add = '?&page_count='
list_url = ['https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/'
               'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/']
count = 1
try:
    driver = uc.Chrome(options=options)
    driver.get(url=url)
    sleep(uniform(3, 5))
    name_file = f'0{count}_ip_useragent_{now}' if len(str(count))==1 else f'{count}_vita_{now}'
    with open(f'{name_file}.html', 'w', encoding="utf-8") as file: #html txt
        file.write(driver.page_source)
    # driver.get(url=url)
    sleep(uniform(8, 16))
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()