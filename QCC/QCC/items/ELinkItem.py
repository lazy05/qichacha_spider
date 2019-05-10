# -*- coding: utf-8 -*-
'''
Created on 2017年8月3日
企业链接
@author: dzm
'''
import scrapy

class ELinkItem(scrapy.Item):

    # 链接
    href = scrapy.Field()
