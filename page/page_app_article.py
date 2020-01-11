from time import sleep

import page
from base.app_base import AppBase


class PageAppArticle(AppBase):
    # 查找并点击频道
    def page_find_channel(self,find_text):
        # 调用滑动点击频道方法
        self.app_base_right_to_left(page.app_area,find_text)

    # 查找文章
    def page_find_article(self):
        sleep(1)
        # 搜索框输入文章名
        # self.base_input(page.app_search,page.article_title)
        # 调用从下向上滑动方法
        self.app_base_down_to_up(page.app_article_area,page.article_title)

    # 组合业务方法
    def page_app_article(self,find_text):
        self.page_find_channel(find_text)
        self.page_find_article()