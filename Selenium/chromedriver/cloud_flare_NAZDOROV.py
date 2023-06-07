import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from datetime import date
from time import sleep
from random import choice, uniform
from selenium import webdriver
from fake_useragent import UserAgent
import random
useragent = UserAgent()
user_agent = useragent.random
options = uc.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
now = date.today()
url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
url = 'https://vitaexpress.ru/'
url = 'https://xn--80aafkze2bij.online'
# url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'

# url = 'https://apteka-april.ru/catalog/396070-lekarstvennye_preparaty_i_bady/3872-sredstva_dlya_lecheniya_prostudy_i_grippa'
# url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
# url = 'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=3872&subtypeSlugs=%22sredstva_dlya_lecheniya_prostudy_i_grippa%22&cityID=57974[100:25]'
str_add = '?page='
dict_url = {
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/preparaty-pri-prostudnykh-zabolevaniyakh-i-grippe/': 5, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/obezbolivayushchie-preparaty/': 12,
    'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/pishchevaritelnaya-sistema/': 17, 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/serdechno-sosudistye-preparaty/': 35
    }
# dict_url = {
    # 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/': 3, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/': 3,
    # 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/': 3, 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/': 3
    # }
list_url = ['https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/preparaty-pri-prostudnykh-zabolevaniyakh-i-grippe/', 'https://xn--80aafkze2bij.online/category/lekarstvennye-preparaty/obezbolivayushchie-preparaty/'
               'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/']
path = fr'C:\Users\user\Scrapy_project\Archive_NAZDOROV'
count = 1

try:
    driver = uc.Chrome()
    driver.get(url=url)
    sleep(uniform(3, 5))
    count = 1
    for k, v in dict_url.items():
        count = 1
        for i in range(v):
            url_2 = k+str_add+str(count)
            group = url_2.replace('//', '').split('/')[3]
            print(group)
            name_file = f'0{count}_{group}_NAZDOROV_{now}.html' if len(str(count))==1 else f'{count}_{group}_NAZDOROV_{now}.html'
            path_file = path+'\\'+name_file
            print(path_file)
            driver.get(url=url_2)
            with open(path_file, 'w', encoding="utf-8") as f: #html txt
                f.write(driver.page_source)
            print('path_file ENTER')
            sleep(uniform(2, 5))
            count +=1
    
    # with open(f'{name_file}.html', 'w', encoding="utf-8") as file: #html txt
    #     file.write(driver.page_source)
    # driver.get(url=url)
    # sleep(uniform(8, 16))
    # for i in range(4):
    #     sleep(uniform(3, 5))
    #     driver.get(url=f'{url}{str_add}{count}')
    #     button_check = driver.find_element(by=By.CSS_SELECTOR, value='div.col-xs-12:nth-child(2) > div:nth-child(1)')
    #     if button_check:
    #         print('wow_done')
    #     else:
    #         print('Nope')
    #     count += 1
    
    # button_show = driver.find_element(by=By.XPATH, value='//button[@class="btn-pager js-vue-catalog"]')
    # button_show.click()
    # count += 1
    # name_file = f'0{count}_vita_{now}' if len(str(count))==1 else f'{count}_vita_{now}'
    # with open(f'{name_file}.html', 'w', encoding="utf-8") as file:
    #     file.write(driver.page_source)
    # input_password = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    # input_password.clear()
    # input_password.send_keys('apm425307mpa')
    # time.sleep(3)
    # chief_input = driver.find_element(by=By.CSS_SELECTOR, value='.css-p171hx')
    # chief_input.click()
    # time.sleep(120)
    # time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()