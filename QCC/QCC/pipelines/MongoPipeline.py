#!/usr/bin/env python
# __*__ coding: utf-8 __*__

""" 
__author__: Xiongkai
@file: MongoPipeline.py
@time: 2019/02/18
@func: define your functions
"""
import uuid
import pymongo
from QCC.items.MDetailItem import MDetailtItem
from QCC.items.MLinkItem import MLinkItem
from QCC.settings import MONGODB_COLL, MONGODB_LINK_DBNAME, \
    MONGODB_HTML_DBNAME, MONGODB_HTML_COLL, MONGODB


class MongodbPipeline(object):
    def __init__(self):
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(MONGODB)
        db_link = client[MONGODB_LINK_DBNAME]
        db_html = client[MONGODB_HTML_DBNAME]
        # 存放数据的数据库表名
        self.coll_link = db_link[MONGODB_COLL]
        self.coll_html = db_html[MONGODB_HTML_COLL]

    def process_item(self, item, spider):
        print('step MongoPipeline item type is {}'.format(type(item)))
        if isinstance(item,MLinkItem):
            try:
                item = dict(item)
                _id = uuid.uuid1().hex
                item['_id'] = _id
                self.coll_link.insert(item)
            except Exception as e:
                print('err:%s ;插入失败:%s' % (e, item))

        elif isinstance(item,MDetailtItem):
            try:
                item = dict(item)
                _id = uuid.uuid1().hex
                item['_id'] = _id
                self.coll_html.insert(item)
            except Exception as e:
                print('err:%s ;插入失败:%s' % (e, item))
        else:
            return item
