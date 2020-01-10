import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMisLogin:
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mis)
        # 获取PageMisLogin 对象
        self.mis_login = PageIn(self.driver).page_get_PageMisLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username,password,expect",read_yaml("mis_login.yaml"))
    def test_login(self,username,password,expect):
        # 登录
        self.mis_login.page_mis_login(username,password)
        # 获取昵称
        nickname = self.mis_login.page_get_nickname()
        print("获取到的昵称为:",nickname)
        # 断言
        try:
            assert expect in nickname
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛出异常
            raise e


