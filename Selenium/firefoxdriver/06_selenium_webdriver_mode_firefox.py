from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = fr"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

driver =  webdriver.Firefox(
    executable_path=fr'C:\Users\user\Scrapy_project\Selenium\firefoxdriver\geckodriver.exe',
    options=options)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()