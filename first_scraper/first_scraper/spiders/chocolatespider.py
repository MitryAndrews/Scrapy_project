import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = 'chocolatespider' # атрибут класса, дающий имя пауку. Мы будем использовать это при запуске нашего паука позже scrapy crawl <spider_name>.
    # allowed_domains = ['apiss.ru']
    allowed_domains = ['chocolate.co.uk'] #
    # start_urls = ['https://apiss.ru/product-tag/best/']
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response):
        pass

#name - атрибут класса, дающий имя пауку. Мы будем использовать это при запуске нашего паука 
#позже scrapy crawl <spider_name>.
#allowed_domains - атрибут класса, который сообщает Scrapy, что он должен когда-либо очищать только 
#страницы chocolate.co.ukдомена. Это не дает пауку стать румяным и очищать множество веб-сайтов. 
#Это необязательно.
#start_urls - атрибут класса, который сообщает Scrapy первый URL-адрес, который он должен очистить. 
# Мы немного изменим это.
#parse - parseфункция вызывается после получения ответа от целевого сайта.
"""Чтобы начать использовать этого Паука, нам нужно будет сделать две вещи:
Измените на start_urlsURL-адрес, который мы хотим очистить https://www.chocolate.co.uk/collections/all .
Вставляем наш код разбора в parse функцию."""



