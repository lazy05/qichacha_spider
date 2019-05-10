# -*- coding: utf-8 -*-
'''
Created on 2017年8月3日
企业链接
@author: dzm
'''
import scrapy


class MLinkItem(scrapy.Item):
    # 名称
    e_name = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # 时间
    createDate = scrapy.Field()

