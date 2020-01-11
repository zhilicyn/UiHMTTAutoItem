from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):

    # 从右向左滑方法
    def app_base_right_to_left(self, area_loc,find_text):
        # 获取区域元素
        el1 = self.base_find(area_loc)
        # 获取区域位置
        location = el1.location
        y = location.get('y')
        # 获取元素宽高
        size = el1.size
        width = size['width']
        height = size['height']
        # 计算start_x,start_y.end_x,end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        # 组合find_text包含的元素定位信息
        loc = By.XPATH,"//*[contains(@text,'{}')]".format(find_text)
        # 获取当前页面元素结构
        page_source = self.driver.page_source
        while True:
            # 首先 查找一次当前页面是否存在要找的元素
            try:
                el2 = self.base_find(loc,timeout=3)
                log.info("找到指定的频道了")
                el2.click()
                # 跳出循环
                break
            except:
                log.info("当前页面没有找到指定频道!")
                # 滑动屏幕
                self.driver.swipe(start_x,start_y,end_x,end_y,2000)
            if page_source == self.driver.page_source:
                log.info("滑不动了,已经是最后一页了")
                raise Exception("找不到指定频道!")
            else:
                page_source = self.driver.page_source




    # 从下向上滑方法
    def app_base_down_to_up(self, channel="android"):
        flag = False
        # 获取元素位置
        sleep(2)
        loc1 = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
        el1 = self.base_find(loc1, timeout=5)
        log.info("定位到元素{}了".format(el1))
        x = el1.location['x']
        y = el1.location['y']
        log.info("元素的坐标为:x={},y={}".format(x, y))
        # 获取元素大小
        width = el1.size['width']
        height = el1.size['height']
        log.info("元素的宽高为:width={},height={}".format(width, height))
        loc2 = By.XPATH, "[@class='android.view.View' and contains(@text,'{}')]".format(channel)
        page1 = self.driver.page_source
        # 查找指定元素
        while flag == False:
            try:
                # 查找频道元素并点击
                self.base_find(loc2, timeout=5).click()
                log.info("找到{}频道了!".format(channel))
                flag = True
            except:
                log.info("当前页面找不到{}频道!".format(channel))
            # 向左滑动
            self.driver.swipe(width * 0.8, y + height * 0.5, width * 0.2, y + height * 0.5, 2000)
            if page1 == self.driver.page_source:
                log.error("已经滑到最后一页了")
                break
            else:
                page1 = self.driver.page_source






