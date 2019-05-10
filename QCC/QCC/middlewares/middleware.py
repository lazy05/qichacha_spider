from redis.sentinel import Sentinel
from scrapy.http import HtmlResponse, Response
from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError

sentinel = Sentinel([],socket_timeout=5)
r = sentinel.master_for('mymaster', socket_timeout=5, db=8)

class ProxyMiddleware(object):
    def __init__(self):
        self.ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def process_request(self, request, spider):
        PROXIES = r.srandmember("proxies", 1)
        proxy = PROXIES[0].decode('utf-8')
        proxy = eval(proxy)
        proxys = "http://" + str(proxy['ip']) + ':' + str(proxy['port'])
        print('set proxy is :', proxys)
        request.meta['proxy'] = proxys


    def process_response(self,request,response,spider):
        #捕获状态码为40x/50x的response
        if str(response.status).startswith('4') or str(response.status).startswith('5'):
            #随意封装，直接返回response，spider代码中根据url==''来处理response
            print('Response code error--->{}'.format(response.status))
            response = HtmlResponse(url='##')
            return response
        #其他状态码不处理
        return response


    def process_exception(self,request,exception,spider):
        #捕获几乎所有的异常
        if isinstance(exception, self.ALL_EXCEPTIONS):
            #在日志中打印异常类型
            print('Got Exception:{}'.format(exception))
            #随意封装一个response，返回给spider
            response = HtmlResponse(url='**')
            return response
        print('Not contained exception: %s' % exception)

