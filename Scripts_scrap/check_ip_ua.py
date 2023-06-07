import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice, uniform

from lxml import etree
from fake_useragent import UserAgent
user_agent= UserAgent()

def get_html(url, useragent= None, proxy=None):
    req = requests.get(url, headers=useragent, proxies=proxy)
    print(req.status_code)
    return req.text

def get_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    dom = etree.HTML(str(soup))
    # ip = dom.xpath('//div/span[@class="ip"]')[0].text
    ip = soup.find('div', class_='text-main dark:text-maindark text-4xl font-medium').text
    # ua = dom.xpath('//div/span[@style="font-size: 20px;"]')[0]
    # ua = soup.find('td', class_='break-all').text
    # print(f'ip - {ip}, type ip - {type(ip)}')
    # print(f'useragent'- {ua})
    us = soup.find('td', class_='break-all').text
    print(us)
    # print(soup.find('span', class_='ip').find_next_sibling('span').text)
    print('--------------------------------------------------')

def main():
    url = 'https://www.sitespy.ru/my-ip'
    url = 'https://awebanalysis.com/ru/what-is-my-ip-address/'
    proxies = open(fr'C:\Users\user\Scrapy_project\Scripts_scrap\proxies2.txt').read().split('\n')
        
    for i in range(len(proxies)):
        sleep(uniform(2, 6))
        proxy = {'http': 'http://'+choice(proxies)}
        proxy_value = proxy['http'].split('//')[1]
        useragent = {'User-Agent': f'{user_agent.random}'}
        print(f'{proxy_value}' if proxy_value=='176.100.76.237' else '' )#, useragent) proxy - {proxy} 
        try:
            html = get_html(url, useragent, proxy)
        except:
            continue
        
        get_ip(html)

if __name__ == '__main__':
    main()
