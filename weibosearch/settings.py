# Scrapy settings for scrapy_weibo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'weibosearch'

SPIDER_MODULES = ['weibosearch.spiders']
NEWSPIDER_MODULE = 'weibosearch.spiders'

# redis config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# scheduler config
SCHEDULER_PERSIST = True
QUEUE_KEY = '%(spider)s:requests'
DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER = "weibosearch.redis.scheduler.Scheduler"

# pipelines config  see more info from http://stackoverflow.com/questions/20881431/scrapy-item-pipelines-warning
#ITEM_PIPELINES = ['weibosearch.pipelines.ScrapyWeiboPipeline']
ITEM_PIPELINES = {
    'weibosearch.pipelines.ScrapyWeiboPipeline': 500,
}
DOWNLOAD_DELAY = 10

TIME_DELTA = 30

# bootstrap from file (item.txt) or from db
BOOTSTRAP = 'file'

# how many feeds can fetch from a item
FEED_LIMIT = 300000

#set the company proxy
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
}