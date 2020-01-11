import time

import page
from base.web_base import WebBase
from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()


class PageMisLogin(WebBase):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.mis_password, pwd)

    # 点击登录
    def page_click_login_btn(self):
        # 改变按钮为可点击状态
        # 使id为inp1的元素的disabled属性失效,这里disabled属性使登录按钮不可点击
        self.driver.execute_script("document.getElementById('inp1').disabled=false")
        # 点击登录按钮
        self.base_click(page.mis_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        time.sleep(2)
        return self.base_get_text(page.mis_nickname)

    # 组合登陆业务方法
    def page_mis_login(self, username, pwd):
        log.info("正在调用后台组合登录业务方法,用户名:{},密码:{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()

    # 组合登陆业务成功方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用后台组合登录业务成功方法,用户名:{},密码:{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
