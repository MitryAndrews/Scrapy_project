import zipfile
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import os
import random
from selenium.webdriver.common.by import By

PROXY_HOST = 'PROXY_IP'
PROXY_PORT = 8000 # Your proxy port
PROXY_USER = 'PROXY_USER'
PROXY_PASS = 'PROXY_PASS'

user_agent = UserAgent()
url = 'https://habr.com/ru/all/'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"76.0.0"
}
"""

background_js = """
let config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}
chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)
        
        chrome_options.add_extension(plugin_file)
    
    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent.random}')

    s = Service(
        executable_path=fr'C:\Users\user\Scrapy_project\Selenium\chromedriver\chromedriver.exe'
    )
    driver = webdriver.Chrome(
        service=s,
        options=chrome_options
    )

    return driver


def main():
    driver = get_chromedriver(use_proxy=False, user_agent=user_agent)
    # driver.get('https://2ip.ru')
    # sleep(2)
    driver.get(url=url)
    time.sleep(2)
    # html = driver.page_source
    with open(f'index.html', 'w') as file:
        file.write(driver.page_source)
    time.sleep(3)
    
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()