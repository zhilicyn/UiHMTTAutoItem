from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog
log = GetLog.get_logger()

class WebBase(Base):
    # 选择状态
    def web_base_click_ul_li(self,placeholder_text,click_text):
        log.info("正在调用选择状态方法,placeholder={},点击文本为:{}".format(placeholder_text,click_text))
        # 组合placeholder 文本元素定位信息
        loc = By.CSS_SELECTOR,"[placeholder='{}']".format(placeholder_text)
        # 查找元素并点击
        self.base_click(loc)
        sleep(1)
        # 定位ul>li -> 列表
        loc = By.CSS_SELECTOR,"ul>li"
        # 遍历 text 内容等于 click_text 条件成立:click()
        for el in self.base_finds(loc):
            if el.text == click_text:
                el.click()
                break

    # 判断元素是否存在
    def web_base_element_exists(self,text):
        loc = By.XPATH,"//*[contains(text(),'{}')]".format(text)
        try:
            self.base_find(loc,timeout=3)#页面存在要查找的元素
            log.info("页面存在要查找的元素")
            return True
        except:
            log.info("页面不存在要查找的元素")
            return False#页面不存在要查找的元素



