# -*- coding: utf-8 -*-
'''
Created on 2019年1月21日
企业详情html
@author: dzm
'''
import scrapy


class MDetailtItem(scrapy.Item):
    # 名称
    e_name = scrapy.Field()
    # 链接
    url = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # html
    detail_page = scrapy.Field()
    # 时间
    createDate = scrapy.Field()
    # 统一社会信用代码
    creditcode = scrapy.Field()