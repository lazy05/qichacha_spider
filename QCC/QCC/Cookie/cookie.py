#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: cookie.py
@time: 2019/4/2 14:26
@func:通过selenium获取cookie
"""
from bwjf_scrapy.util.webdriver_util import WebdriverUtil
from redis.sentinel import Sentinel
from QCC.settings import REDIS_SENTINELS, REDIS_ENAME_DB

sentinel = Sentinel([], socket_timeout=5)
rip = sentinel.master_for('mymaster', socket_timeout=5, db=8)
r = sentinel.master_for('mymaster', socket_timeout=5, db=0)

class Cookie(object):
    def get_ip(self):
        PROXIES = rip.srandmember("proxies", 1)
        proxy = PROXIES[0].decode('utf-8')
        proxy = eval(proxy)
        proxys = {'host':str(proxy['ip']),'port':proxy['port']}
        # print('set proxy is :', proxys)
        return proxys


    def get_cookie(self):
        proxys = self.get_ip()
        browser = WebdriverUtil().getWebDriverHeadLess(proxyip=proxys, types=None)
        browser.get("https://www.qichacha.com/")
        cookie_list = browser.get_cookies()
        strs = ''
        cookie_dict = {}
        for cookie in cookie_list:
            infos = cookie['name'] + '=' + cookie['value'] + '; '
            strs += infos
        cookie_dict['cookie'] = strs
        browser.quit()
        return cookie_dict


    def remove_cookie(self):
        c = r.spop('QCC_Cookie')
        print('失效cookie已删除')


    def input_cookie(self):
        cookie_list = self.get_cookie()
        # print(cookie_list)
        r.sadd('QCC_Cookie',cookie_list)
        print('cookie已存入redis')


    def output_cookie(self):
        result = r.srandmember('QCC_Cookie')
        cookie = str(result, "utf-8")
        print('取出cookie')
        return cookie


