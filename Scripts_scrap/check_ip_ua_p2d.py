import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# from proxy_info import login, password

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
}
user_agent = UserAgent()
user_agent = {'User-Agent': f'{user_agent.random}'}
proxies = {
    'https': 'http://66.228.50.107:10000'
    }
# 'https': f'http://{login}:{password}@proxy_ip:proxy_port'

def get_location(url):
    response = requests.get(url=url)#, proxies=proxies)# , headers=user_agent
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.status_code)
    # print(soup)
    print(soup.find('div', class_='ip-icon-label'))#.text.strip())
    # ip = soup.find('div', class_='ip-icon-label').text.strip()
    # print(f'ip- {ip}')
    print(soup.find('div', class_='value value-country'))#.text.strip())
    
    # print(f'IP: {ip}\nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')
    
    
if __name__ == '__main__':
    main()