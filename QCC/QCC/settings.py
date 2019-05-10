# -*- coding: utf-8 -*-

# Scrapy settings for QCC project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'QCC'

SPIDER_MODULES = ['QCC.spiders']
NEWSPIDER_MODULE = 'QCC.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'QCC (+http://www.yourdomain.com)'

# Obey robots.txt rules
HTTPERROR_ALLOWED_CODES = [500,405, 404, 403, 302,400, 100, 301]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
RETRY_HTTP_CODES = [502, 503, 504, 522, 524, 408]

# robots.txt规则
ROBOTSTXT_OBEY = False
# 并发请求数,保护当前机器请求的带宽不超出负载
# CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS = 2
# 对一个网站的最大并发数
CONCURRENT_REQUESTS_PER_DOMAIN = 50
# 对一个IP的最大并发数
CONCURRENT_REQUESTS_PER_IP = 50
# 同时处理的Item数量
CONCURRENT_ITEMS = 200
# 下载超时
DOWNLOAD_TIMEOUT = 360
# 下载延迟5s
DOWNLOAD_DELAY = 2

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
   # 'gs_jilin.middlewares.GsJilinDownloaderMiddleware': 543,
   #  "internet.error"
   #  'QCC.middlewares.middleware.ProxyMiddleware': 280,
    'bwjf_scrapy.middlewares.retry.RetryMiddleware': 120,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xy_hunan.middlewares.XyHunanSpiderMiddleware': 543,
#}
ITEM_PIPELINES = {
   # 'gs_jilin.pipelines.GsJilinPipeline': 300,
    'en_plugin.scrapy.pipeline.SubEnEsPipeline':50,
    'QCC.pipelines.MongoPipeline.MongodbPipeline': 75,
    "QCC.pipelines.RedisPipeline.RedisPipeline":100
}
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
#Redis数据库集群配置
REDIS_PARAMS = {
    'use_sentinel': True,
    'service_name': 'mymaster',
    'db': 3
}
REDIS_SENTINELS = []
REDIS_KEY_PRFIX = ''
REDIS_ANNUAL_KEY_PRFIX = ''
REDIS_HASH_KEY_PRFIX = ''
# # 企业名称数据库
REDIS_ENAME_KEY=''
# REDIS_LINKS_KEY = 'links_'
REDIS_ENAME_DB=0


#忽略的htto代码
RETRY_ENABLED=True
IGNORE_HTTP_CODES = [200]
RETRY_TIMES=5
RETRY_PRIORITY_ADJUST = -1
#ElasticSearch配置
ES_IP = ''
ES_USER = ''
ES_PASSWORD = ''


## MONGODB配置
MONGODB = ''
MONGODB_LINK_DBNAME = 'detail_links'
MONGODB_COLL = 'qcc_links'
MONGODB_HTML_DBNAME = 'detail_html'
MONGODB_HTML_COLL = 'qcc_detail'

#MONGODB抬头异常数据存储
MONGODB_SUB_EN_DB='en_invalid'
MONGODB_DB='xy_title_info'



# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'QCC.middlewares.QccSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'QCC.middlewares.QccDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'QCC.pipelines.QccPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
