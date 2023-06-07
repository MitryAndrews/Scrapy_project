# Scrapy settings for apteka project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'apteka'

SPIDER_MODULES = ['apteka.spiders']
NEWSPIDER_MODULE = 'apteka.spiders'

#Getting Started Guide
#API Key (required):
#You need to include your API key on every request.
# Here is = https://scrapeops.io/docs/fake-user-agent-headers-api/integrations/python-scrapy/

SCRAPEOPS_API_KEY = '0b7ee11e-6427-4178-a3cc-d0b0cb2df7a5'
SCRAPEOPS_FAKE_HEADERS_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'apteka.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'apteka (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ROTATING_PROXY_LIST = ['185.191.76.84:80', '198.49.68.80:80', '104.148.36.10:80', '110.164.3.7:8888', 
'50.220.187.9:80', '68.185.57.66:80', '50.231.110.26:80', '50.230.222.202:80']#, 
# '178.22.49.151:42478', '50.206.111.89:80', '50.207.253.118:80', '50.217.44.154:80', 
# '65.37.106.2:80', '24.158.29.166:80', '50.217.110.216:80', '50.174.26.56:80', 
# '50.218.57.69:80', '50.218.57.70:80', '50.204.233.30:80', '50.239.72.18:80', 
# '50.239.72.17:80', '50.217.22.111:80', '50.237.89.160:80', '50.217.44.153:80', 
# '50.239.72.19:80', '106.107.205.112:80', '50.217.22.106:80', '50.217.22.109:80', 
# '50.217.110.218:80', '50.227.121.33:80', '50.217.226.47:80', '50.217.226.44:80', 
# '50.227.121.32:80', '150.181.4.41:80', '195.23.57.78:80', '50.219.142.159:80', 
# '50.206.25.108:80', '50.206.25.111:80', '77.73.241.154:80', '50.220.21.202:80', 
# '24.95.253.39:80', '50.228.141.98:80', '50.223.130.88:80', '50.228.141.102:80', 
# '50.217.22.104:80', '50.217.44.152:80', '50.218.57.71:80', '50.223.130.90:80', 
# '106.107.203.151:80', '50.218.57.67:80', '50.217.110.222:80', '50.237.89.166:80', 
# '50.217.226.42:80', '50.217.226.41:80', '107.1.93.212:80', '50.207.187.131:80', 
# '50.207.187.129:80', '212.230.172.6:80', '20.121.184.238:80', '87.247.186.105:80', 
# '80.179.140.189:80', '37.235.48.177:80', '37.235.48.19:80', '165.22.226.8:80']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'apteka.middlewares.AptekaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'apteka.middlewares.AptekaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'apteka.pipelines.AptekaPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
