import scrapy


class AptekaSpiderSpider(scrapy.Spider):
    name = 'apteka_spider'
    allowed_domains = ['vitaexpress.ru']
    start_urls = ['https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/']
    # allowed_domains = ['apteka.ru']
    # start_urls = ['https://apteka.ru/category/orvi/antiviral_action/']
#https://vitaexpress.ru/catalog/lekarstva-i-bady/lekarstva-ot-prostudy/
    def parse(self, response):
        pass
