from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mis)
        # 实例化统一入口类
        self.page = PageIn(self.driver)
        # 调用登录业务成功方法
        self.page.page_get_PageMisLogin().page_mis_login_success()
        # 实例化PageMisAudit对象
        self.mis_audit = self.page.page_get_PageMisAudit()

    # 结束
    def teardown_class(self):
        # 关闭driver
        sleep(5)
        GetDriver.quit_driver()

    # 审核文章测试方法
    def test_article_audit(self,title=page.article_title,channel=page.article_channel):
        # 调用文章审核业务方法
        self.mis_audit.page_mis_audit(title,channel)
        # 获取文章id
        article_id = self.mis_audit.page_assert_success(title,channel)
        print("获取到的文章id为:",article_id)
        # 断言
        try:
            assert self.mis_audit.web_base_element_exists(article_id)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_audit.base_get_img()
            # 抛出异常
            raise e



