"""
   自媒体文章发表
"""
import pytest
import api
from api.api_pm_zmt import ApiZmt
from tools.get_tools import Tools
from tools.read_yaml import read_yaml
from tools.get_log import GetLog

# 日志器
log = GetLog.get_log()

class TestApizmt(object):
    def setup_class(self):
        self.zmt = ApiZmt()

    def teardown_class(self):
        pass

    # 请求登入接口
    @pytest.mark.parametrize("mobile,code",read_yaml("data_zmt.yaml"))
    def test01_api_login(self,mobile,code):
        # 登入接口响应参数
        r_login = self.zmt.api_login(mobile,code)
        # 获取token
        Tools.get_token(r_login)
        # 断言
        Tools.implement_accsert(r_login)

    def test02_api_artical(self,title=api.title,content=api.content,channel_id=api.channal_id):
        r_artical = self.zmt.api_artical(title,content,channel_id)
        # 获取文章id
        api.artical_id = r_artical.json().get('data').get('id')
        log.info(f"获取文章id为：{api.artical_id}")
        # 断言
        Tools.implement_accsert(r_artical)









if __name__ == '__main__':
    pytest.main()