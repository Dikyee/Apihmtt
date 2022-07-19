"""
   相关工具封装
"""
import api
from tools.get_log import GetLog

# 日志器
log = GetLog.get_log()

class Tools(object):

    # 获取token
    @classmethod
    def get_token(cls,response):
        log.info("正在获取Authorization")
        token = response.json().get('data').get('token')
        api.headers['Authorization'] = "Bearer " + token
        log.info(f"获取后的headers为：{api.headers}")

    # 进行断言
    @classmethod
    def implement_accsert(cls,response,message='OK',code=201):
        log.info("正在进行断言")
        try:
            assert message == response.json().get('message')
            assert code == response.status_code
        except Exception as e :
            log.error("错误信息为：",e)
        #抛出异常
            raise
