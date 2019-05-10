# -*- coding: utf-8 -*-
'''
Created on 2018年5月28日
redis管道主要存放的是过程数据
@author: dzm
'''
from redis.sentinel import Sentinel
from QCC.items.ELinkItem import ELinkItem


class RedisPipeline(object):

    def __init__(self, server):
        self.server = server


    def process_item(self, item, spider):
        print('step RedisPipeline item type is {}'.format(type(item)))
        if type(item) == ELinkItem:
            # 企业详情链接存储
            self.server.sadd('qcc_detail_link',item['href'])
        else:
            return item

    @classmethod
    def from_settings(cls, settings):
        params = {'db': settings.get('REDIS_ENAME_DB')}
        sentinel = Sentinel(settings.get('REDIS_SENTINELS'), **params)
        server = sentinel.master_for(settings.get('REDIS_PARAMS')['service_name'], **params)
        return cls(server)

