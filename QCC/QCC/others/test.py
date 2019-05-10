#!/usr/bin/env python
# __*__ coding: utf-8 __*__
"""
__author__: lazy
@file: 
@time: 2019/4/19 13:37
@func:
"""
import requests,re
url = 'https://www.qichacha.com/firm_a72de93b5c0f1b12015f992419fd6700.html#base'
# headers = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding":"gzip, deflate, br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Cache-Control":"max-age=0",
#     "Connection":"keep-alive",
#     # "Cookie":"hasShow=1; UM_distinctid=16a34279a373f-0a06c5e17865f7-1e173073-afc80-16a34279a38acb; QCCSESSID=91vsd5bv85icp7ugl4dr4okp34; CNZZDATA1254842228=1035763552-1555647990-%7C1555647990; _uab_collina=155565317643684968478086; zg_did=%7B%22did%22%3A%20%2216a34279deb6c-013635daabac6-1e173073-afc80-16a34279dec13e%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201555653172725%2C%22updated%22%3A%201555653172740%2C%22info%22%3A%201555653172737%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1555653173; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1555653173; acw_tc=6f48649b15556531730436061e472f96b6b49087b0d732e3c8069652f7; ",
#     "Host":"www.qichacha.com",
#     "Referer":"https://www.qichacha.com/",
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
# }
# #
# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Host': 'www.qichacha.com', 'Referer': 'https://www.qichacha.com/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'Cookie': 'hasShow=1; UM_distinctid=16a342dd86e77e-0f60f818f14fc7-1e173073-afc80-16a342dd86f61b; QCCSESSID=mem2m8af4sk27njioskapsmu40; CNZZDATA1254842228=1244317403-1555653390-%7C1555653390; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1555653583; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1555653583; _uab_collina=155565358425954008313169; zg_did=%7B%22did%22%3A%20%2216a342de104447-0228234923e5de-1e173073-afc80-16a342de10558c%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201555653583113%2C%22updated%22%3A%201555653583118%2C%22info%22%3A%201555653583117%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; acw_tc=6f48649b15556535808692086e39006d64f58c810482741f706cfd6ec2; '}
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Host': 'www.qichacha.com', 'Referer': 'https://www.qichacha.com/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'Cookie': 'hasShow=1; UM_distinctid=16a3431d427482-0bd5f4d8f9361c-1e173073-afc80-16a3431d428917; QCCSESSID=7vor4aa9bampr1f89b56ci8q90; CNZZDATA1254842228=1897490421-1555653390-%7C1555653390; _uab_collina=155565384657654214452944; zg_did=%7B%22did%22%3A%20%2216a3431d888520-0dad1e2f826b5d-1e173073-afc80-16a3431d889557%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201555653843086%2C%22updated%22%3A%201555653843092%2C%22info%22%3A%201555653843090%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1555653844; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1555653844; acw_tc=da5bdd9915556538431937353ed1b65ac922704ba12732deca2a9a8c3f; '}

response = requests.get(url=url)
print(response.text)







