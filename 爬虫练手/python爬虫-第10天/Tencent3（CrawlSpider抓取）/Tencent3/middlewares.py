#coding:utf-8

import random
from settings import USER_AGENT_LIST


class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        # 获取一个新的User-Agent
        user_agent = random.choice(USER_AGENT_LIST)

        # 更改当前请求的User-Agent
        request.headers["User-Agent"] = user_agent
        # print("---" * 30)
        # print(request.headers)
        #return request


class RandomProxyMiddleware(object):
    def process_request(self, request, spider):
        # 验证代理，需要提供账户名密码和ip:port
        proxy = "http://maozhaojun:ntkn0npx@39.96.8.207:16818"
        # 免费代理
        #proxy = "http://39.106.10.232:16818"

        # 给当前请求添加代理信息
        request.meta['proxy'] = proxy

