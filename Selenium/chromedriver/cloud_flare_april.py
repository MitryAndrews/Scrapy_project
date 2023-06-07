import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
from datetime import date
from time import sleep
from random import choice, uniform
from selenium import webdriver

now = date.today()
url1 = f'https://apteka-april.ru/'
path = fr'C:\Users\user\Scrapy_project\Archive_April'
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
try:
    driver = undetected_chromedriver.Chrome()
    driver.get(url=url1)
    sleep(uniform(2, 3))
    for k, v in dict_url.items():
        count = 1*step
        for j in range(1, v, step):
            tail = f'{count}:{step}%5D'
            group = k.split('%22')[-2]
            name_file = f'0{count}_{group}_{step}_APRIL_{now}' if len(str(count))==1 else f'{count}_{group}_{step}_APRIL_{now}'
            url2 = k+tail
            driver.get(url=url2)
            name_file = f'0{count}_{group}_{step}_april_{now}' if len(str(count))==1 else f'{count}_{group}_{step}_april_{now}'
            # print(url2)
            path_file = path+'\\'+name_file
            with open(f'{path_file}.txt', 'w', encoding="utf-8") as file: #html
                file.write(driver.page_source)
            sleep(uniform(8, 15))
            print(path_file)
            # print('j - ', j, group)
            count += step
    # for i in range(1, 1000, step):
    #     url = f'https://web-api.apteka-april.ru/catalog/ID,slug,price,priceZakaz,sticker,name,images,typeIDs,subtypeIDs,categoryID,isInStock,allowDelivery,allowOnlinePayment,averageRating,reviewsNumber,bonuses,deliveryRuleID,limitWithCard,limitWithoutCard,isAvailable,isWaitingArrive,isRecipe,discountTemplate,deliveryAmount,mightNeedID,imagesSizeS,imagesSizeXS,properties,rating,properties,rating@products?typeIDs=396070&typeSlugs=%22lekarstvennye_preparaty_i_bady%22&subtypeIDs=2552&subtypeSlugs=%22obezbolivayushchie_protivovospalitelnye_sredstva%22&cityID=57974%5B{count}:{step}%5D'
    #     driver.get(url=url)
    #     name_file = f'0{count}_{step}_april_{now}' if len(str(count))==1 else f'{count}_{step}_april_{now}'
        
    #     with open(f'{name_file}.txt', 'w', encoding="utf-8") as file: #html
    #         file.write(driver.page_source)
    #     sleep(uniform(5, 10))
    #     print(f'0{count}_{step}_april_{now}')
    #     count += step
        # driver.close()
        # driver.quit()
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