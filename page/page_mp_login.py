import time

import page
from base.base import Base

from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()


class PageMpLogin(Base):

    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.mp_phone, phone)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(page.mp_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法(测试脚本业务层调用)
    def page_mp_login(self, phone, code):
        log.info("正在调用自媒体登录组合方法,账号:{},验证码:{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

        # 组合业务方法(测试脚本业务层调用)
    def page_mp_login_success(self, phone="13812345678", code="246810"):
        log.info("正在调用自媒体登录组合方法,账号:{},验证码:{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        time.sleep(1)
        self.page_click_login_btn()
