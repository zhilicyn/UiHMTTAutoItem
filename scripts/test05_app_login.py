from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_app_driver()
        # 通过统一入口类获取PageAppLogin对象
        self.app_login = PageIn(self.driver).page_get_PageAppLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 测试方法
    def test_app_login(self, username="13812345678", code="246810"):
        # 登录
        self.app_login.page_app_login(username, code)
        # 断言
        try:
            assert self.app_login.page_if_element_exists()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.app_login.base_get_img()
            # 抛异常
            raise
