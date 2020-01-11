import time

import page
from base.web_base import WebBase
from page.page_mp_login import PageMpLogin
from tools.get_driver import GetDriver
from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()

class PageMpArticle(WebBase):

    # 点击内容管理
    def page_click_content(self):
        time.sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_post_article(self):
        time.sleep(2)
        self.base_click(page.mp_publish_article)

    # 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_article_title, title)

    # 输入文字内容
    def page_input_article_content(self, content):
        # 切换到iframe标签
        self.driver.switch_to.frame(self.base_find(page.mp_article_iframe_id))
        # 输入文章内容
        self.base_input(page.mp_article_content, content)
        # 切换回主页面
        self.driver.switch_to.default_content()

    # 选择封面
    def page_check_cover(self):
        # 滚动条操作
        self.driver.execute_script("window.scrollTo(0,1000)")
        # 点击自动
        self.base_click(page.mp_article_cover)

    # 选择频道
    def page_check_channel(self,channel):
        # 点击选择频道
        # self.base_click(page.mp_channel)
        # time.sleep(2)
        # 选择具体方法
        # self.base_click((page.mp_check_channel[0], page.mp_check_channel[1].format(channel)))
        self.web_base_click_ul_li("请选择",channel)

    # 点击发布
    def page_click_commit(self):
        self.base_click(page.mp_commit_btn)

    # 获取发布 结果提示信息
    def page_get_commit_result(self):
        return self.base_get_text(page.mp_msg_alert)

    # 业务组合方法 发布文章
    def page_publish_article(self, title, content, channel):
        log.info("正在调用自媒体文章发布业务组合方法,文章名:{},文章内容:{},频道:{}".format(title,content,channel))
        # 点击内容管理
        self.page_click_content()
        # 点击发布文章
        self.page_click_post_article()
        # 输入文章名称
        self.page_input_title(title)
        # 输入文章内容
        self.page_input_article_content(content)
        # 选择封面
        self.page_check_cover()
        # 选择频道
        self.page_check_channel(channel)
        # 点击发布
        self.page_click_commit()


if __name__ == '__main__':
    # 此处代码不可用,路径问题(log)
    driver = GetDriver().get_driver("http://ttmp.research.itcast.cn/#/login")
    page1 = PageMpLogin(driver)
    page1.page_mp_login("13812345678", "246810")
    print(page1.page_get_nickname())
    time.sleep(2)
    page3 = PageMpArticle(driver)
    page3.page_publish_article("test111", "啦啦啦阿拉", "数据库")
    time.sleep(3)
    page3.page_get_commit_result()
    time.sleep(3)
    driver.quit()
