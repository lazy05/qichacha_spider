#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: 
@time: 2019/4/19 13:57
@func:
"""
import datetime
import re,scrapy
import time
import zlib

import requests
from en_plugin.scrapy.items import InvoiceTitleItem
from redis.sentinel import Sentinel
from QCC.Cookie.cookie import Cookie
from QCC.items.MDetailItem import MDetailtItem
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


## 粗解析
def remove_js_css(content):
    """
    #删除web中的head,jss,注释、Css和空行等标签
    """
    r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
    sc = r.sub('', content)
    r = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''<!--.*?-->''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''<meta.*?>''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''<ins.*?</ins>''', re.I | re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''^\s+$''', re.M | re.S)
    sc = r.sub('', sc)
    r = re.compile(r'''\n+''', re.M | re.S)
    sc = r.sub('\n', sc)
    ##转化为byte形式存储
    sc = str.encode(sc)
    sc = zlib.compress(sc)
    return sc.strip()


class QCCSpider(BwjfRedisSpider):
    name = 'QCC_detail'
    redis_key = 'qcc_detail_link'
    redis_db = redis_ename_db

    #从redis中获得关键词
    def make_request_from_data(self, data):
        url = bytes_to_str(data, self.redis_encoding)
        print('链接',url)
        c= cookie.output_cookie()
        headers['Cookie'] = eval(c)['cookie']
        #  提交查询请求
        return scrapy.Request(url='https://www.baidu.com/', meta={'headers': headers,'cookie':eval(c), 'url':url}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        meta = response.meta
        ip = cookie.get_ip()
        proxys = {}
        proxys['http'] = 'http://' + ip['host'] + ":" + ip['port']
        proxys['https'] = 'https://' + ip['host'] + ":" + ip['port']
        html = requests.get(url=meta['url'],headers=meta['headers'],proxies=proxys).text
        cookies = response.meta['cookie']
        try:
            name = re.findall(r"{'企业名称':'(.*?)'}", html, re.S | re.I | re.M)[0].strip()
            print(name)
            try:
                creditcode = re.findall(r'<td class="tb">统一社会信用代码</td> <td class="">(.*?)</td>', html, re.S | re.I | re.M)[
                    0].strip()
            except:
                creditcode = re.findall(r'<td class="tb"> 工商登记 </td> <td>(.*?)</td>', html, re.S | re.I | re.M)[0].strip()
            print(creditcode)
            try:
                adder = re.findall(r'<td class="tb">企业地址</td> <td class="" colspan="3">(.*?)<a', html, re.S | re.I | re.M)[
                    0].strip()
            except:
                adder = ''
            invoicetitleitem = InvoiceTitleItem()
            mdetailitem = MDetailtItem()
            invoicetitleitem['es_index'] = 'organ'
            invoicetitleitem['name'] = name
            invoicetitleitem['creditcode'] = creditcode
            invoicetitleitem['addresstel'] = adder
            invoicetitleitem['bandkaccount'] = ''
            invoicetitleitem['source'] = '企查查'
            invoicetitleitem['status'] = ''
            invoicetitleitem['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(invoicetitleitem)
            yield invoicetitleitem
            mdetailitem['e_name'] = name
            mdetailitem['url'] = meta['url']
            mdetailitem['source'] = '企查查'
            mdetailitem['status'] = '0'
            mdetailitem['detail_page'] = remove_js_css(html)
            mdetailitem['creditcode'] = creditcode
            mdetailitem['createDate'] = str(round(time.time(),3))
            yield mdetailitem
        except:
            print(html)









