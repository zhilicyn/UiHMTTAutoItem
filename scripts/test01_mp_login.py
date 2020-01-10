import pytest

from tools.read_yaml import read_yaml

import time

import page
from tools.get_driver import GetDriver
from page.page_in import PageIn
from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()

class TestLogin:

    @classmethod
    def setup_class(cls):
        # 获取driver
        cls.driver = GetDriver().get_driver(page.url_mp)
        # 获取PageMpLogin对象
        cls.login = PageIn(cls.driver).page_get_PageMpLogin()

    @classmethod
    def teardown_class(cls):
        # 关闭driver
        time.sleep(2)
        GetDriver().quit_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone,code,expect",read_yaml("mp_login.yaml"))
    def test_mp_login(self,phone,code,expect):
        # 登录
        self.login.page_mp_login(phone,code)
        # 获取昵称
        nickname = self.login.page_get_nickname()
        print("获取到的昵称: ",nickname)
        # 断言
        try:
            # 断言昵称
            assert "13812345678" == nickname # 没有指定异常信息
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise e


