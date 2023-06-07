import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = 'chocolatespider'
    allowed_domains = ['vitaexpress.ru']
    start_urls = ['http://vitaexpress.ru/']

    def parse(self, response):
        pass
