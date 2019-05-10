#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: 
@time: 2019/4/2 14:23
@func:
"""
from scrapy import cmdline
cmdline.execute('scrapy crawl QCC'.split())
# cmdline.execute('scrapy crawl QCC_detail'.split())