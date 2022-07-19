import api
import requests
from tools.get_log import GetLog

# 日志器
log = GetLog.get_log()

class ApiZmt(object):
    def __init__(self):
        log.info("正在初始化接口")
        # 登入接口
        self.url_login = api.host + "/mp/v1_0/authorizations"
        # 发表文章接口
        self.url_artical = api.host + "/mp/v1_0/articles?draft=false"

    def api_login(self,mobile,code):
        log.info(f"正在请求接口：mobile：{mobile},code{code}")
        # 登入参数
        data = {"mobile":mobile,"code":code}
        # 登入请求
        log.info("正在返回接口")
        return requests.post(url=self.url_login,json=data,headers=api.headers)


    def api_artical(self,title,content,channel_id):
        data = {"title":title,"content":content,"imgType":"none","channel_id":channel_id,"cover":{"type":0,"images":[]}}
        return  requests.post(url=self.url_artical,json=data,headers=api.headers )


if __name__ == '__main__':
    ApiZmt().api_artical()

