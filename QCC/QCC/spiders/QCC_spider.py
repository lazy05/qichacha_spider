#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: 
@time: 2019/4/2 14:20
@func:
"""
import datetime
import re,scrapy
import time

import requests
from bs4 import BeautifulSoup
from redis.sentinel import Sentinel
from QCC.Cookie.cookie import Cookie
from QCC.items.ELinkItem import ELinkItem
from QCC.items.MLinkItem import MLinkItem
from QCC.settings import REDIS_ENAME_DB as redis_ename_db
from bwjf_scrapy_redis.utils import bytes_to_str
from bwjf_scrapy.spider.BwjfRedisSpider import BwjfRedisSpider
sentinel = Sentinel([],
                    socket_timeout=5)
r = sentinel.master_for('mymaster', socket_timeout=5, db=0)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.qichacha.com",
    "Referer": "https://www.qichacha.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}

cookie = Cookie()


class QCCSpider(BwjfRedisSpider):
    name = 'QCC'
    redis_key = 'unit_word'
    redis_db = redis_ename_db

    #从redis中获得关键词
    def make_request_from_data(self, data):
        ename = bytes_to_str(data, self.redis_encoding)
        # print('关键词',ename)
        c= cookie.output_cookie()
        url = 'https://www.qichacha.com/search?key=' + ename
        headers['Cookie'] = eval(c)['cookie']
        #  提交查询请求
        return scrapy.Request(url='https://www.baidu.com/', meta={'headers': headers,'cookie':eval(c), 'url':url}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        if '##' in response.url or '**' in response.url:
            print('请求响应异常')
        else:
            meta = response.meta
            ip = cookie.get_ip()
            proxys = {}
            proxys['http'] = 'http://' + ip['host'] + ":" + ip['port']
            proxys['https'] = 'https://' + ip['host'] + ":" + ip['port']
            html = requests.get(url=meta['url'],headers=meta['headers'],proxies=proxys).text
            cookies = response.meta['cookie']
            rep = BeautifulSoup(html, 'lxml')
            labels = rep.select('label[class="text-dark-lter"] input')[:-2]
            if labels:
                mlinkitem = MLinkItem()
                elinkitem = ELinkItem()
                for i in labels:
                    name = i.get('data-name').replace('<em>', '').replace('</em>', '')
                    link = i.get('value')
                    # print(name, link)
                    mlinkitem['e_name'] = name
                    mlinkitem['url'] = 'https://www.qichacha.com/firm_{}.html#base'.format(link)
                    mlinkitem['source'] = '企查查'
                    mlinkitem['status'] = '0'
                    mlinkitem['createDate'] = str(round(time.time(),3))
                    yield mlinkitem
                    elinkitem['href'] = mlinkitem['url']
                    yield elinkitem
            else:
                r.srem('QCC_Cookie',cookies)
                print('cookie失效,删除cookie')













