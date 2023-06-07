import undetected_chromedriver
import time

url = 'https://habr.com/ru/all/'

try:
    driver = undetected_chromedriver.Chrome()
    driver.get(url=url)
    with open(f'index.html', 'w', encoding="utf-8") as file:
        file.write(driver.page_source)
    # time.sleep(2)
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # driver.get("https://www.vindecoderz.com/EN/")
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()