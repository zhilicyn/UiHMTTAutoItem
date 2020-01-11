from time import sleep

import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageAppLogin(AppBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.app_username,username)

    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.app_code,code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断我的是否存在
    def page_if_element_exists(self):
        sleep(3)
        try:
            el = self.base_find(page.app_me,timeout=5)
            log.info("找到我的菜单了!它的位置位于:{}".format(el.location))
            return True
        except:
            log.info("没有找到我的菜单!")
            return False

    # 组合登录业务方法
    def page_app_login(self,username,code):
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
