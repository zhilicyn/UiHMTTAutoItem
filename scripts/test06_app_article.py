import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestAppArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 实例化统一入口类
        self.page_in = PageIn(driver)
        # 调用组合登录业务成功方法
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        # 实例化PageAPPArticle对象
        self.app_article = self.page_in.page_get_PageAppArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 查找文章测试方法
    def test_app_article(self,channel=page.article_channel):
        # 查找文章组合业务方法
        self.app_article.page_app_article(channel)
        # 断言
        try:
            pass
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.app_article.base_get_img()
            # 抛出异常
            raise
