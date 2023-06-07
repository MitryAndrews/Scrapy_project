import scrapy


class VitaexpressspiderSpider(scrapy.Spider):
    name = 'vitaexpressspider'
    allowed_domains = ['vitaexpress.ru']
    start_urls = ['http://vitaexpress.ru/']

    def parse(self, response):
        pass
