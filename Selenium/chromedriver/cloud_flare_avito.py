import undetected_chromedriver
from selenium.webdriver.common.by import By
import time

url = 'https://habr.com/ru/all/'
url = 'https://www.avito.ru/'
url = 'https://vitaexpress.ru/'
url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/?&page_count=4'
# url = 'https://apteka-april.ru/catalog/396070-lekarstvennye_preparaty_i_bady/3872-sredstva_dlya_lecheniya_prostudy_i_grippa'
# url = 'https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/'
str_add = '?&page_count='
list_url = ['https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/obezbolivayushchie/'
               'https://vitaexpress.ru/catalog/lekarstva-i-bady/zheludochno-kishechnye-preparaty/', 'https://vitaexpress.ru/catalog/lekarstva-i-bady/zdorovoe-serdtse-i-sosudy/']
try:
    driver = undetected_chromedriver.Chrome()
    driver.get(url=url)
    with open(f'wow_index.html', 'w', encoding="utf-8") as file:
        file.write(driver.page_source)
    # driver.get(url=url)
    time.sleep(35)
    # with open(f'index.html', 'w') as file:
    #     file.write(driver.page_source)
    # time.sleep(3)
    # reg_form = driver.find_element(by=By.CSS_SELECTOR, value='.index-services-menu-link-not-authenticated-Pzomx')
    # reg_form.click()
    # time.sleep(2)
    # phone_form = driver.find_element(by=By.CSS_SELECTOR, value='label.css-vnayv5:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    # phone_form.clear()
    # phone_form.send_keys('9053603453')
    # time.sleep(2)
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