from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()


class PageMisAudit(WebBase):
    # 点击信息管理
    def page_click_info_manage(self):
        sleep(2)
        self.base_click(page.mis_info_manage)

    # 点击内容审核
    def page_click_content_audit(self):
        sleep(2)
        self.base_click(page.mis_content_audit)

    # 输入搜索的文章名称
    def page_search_article(self,title):
        sleep(2)
        self.base_input(page.mis_search_article_title,title)

    # 输入频道
    def page_input_channel(self,channel):
        sleep(2)
        self.base_input(page.mis_channel,channel)

    # 选择文章状态
    def page_click_status(self):
        sleep(2)
        self.web_base_click_ul_li("请选择状态","待审核")

    # 点击查询按钮
    def page_click_demand_btn(self):
        sleep(1)
        self.base_click(page.mis_demand_btn)



    # 点击通过按钮
    def page_click_pass_btn(self):
        sleep(2)
        self.base_click(page.mis_pass_btn)

    # 点击确认通过按钮
    def page_pass_confirm_pass(self):
        sleep(2)
        self.base_click(page.mis_confirm_pass)

    # 获取文章id
    def page_get_article_id(self):
        sleep(1)
        return self.base_get_text(page.mis_article_id)


    # 组合业务方法
    def page_mis_audit(self,title,channel):
        log.info("正在调用后台文章审核组合业务方法,文章标题:{},频道:{}".format(title,channel))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_search_article(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_demand_btn()
        sleep(3)
        self.article_id = self.page_get_article_id()
        self.page_click_pass_btn()
        self.page_pass_confirm_pass()


    # 断言
    def page_assert_success(self,title,channel):
        # 刷新
        sleep(3)
        self.driver.refresh()
        sleep(1)
        # 输入标题
        self.page_search_article(title)
        # 输入频道
        self.page_input_channel(channel)
        # 点击状态
        self.web_base_click_ul_li("请选择状态","审核通过")
        # 点击查询
        self.page_click_demand_btn()
        return self.article_id




