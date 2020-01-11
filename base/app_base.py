from time import sleep

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):

    # 从右向左滑方法
    def app_base_right_to_left(self, area_loc, find_text):
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
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(find_text)
        # 获取当前页面元素结构
        page_source = self.driver.page_source
        while True:
            # 首先 查找一次当前页面是否存在要找的元素
            try:
                el2 = self.base_find(loc, timeout=3)
                log.info("找到指定的频道了")
                el2.click()
                # 跳出循环
                break
            except:
                log.info("当前页面没有找到指定频道!")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
            if page_source == self.driver.page_source:
                log.info("滑不动了,已经是最后一页了")
                raise NoSuchElementException("已经最后一页了,找不到指定频道{}!".format(find_text))
            else:
                page_source = self.driver.page_source

    # 从下向上滑方法
    def app_base_down_to_up(self, area_loc, find_text):
        # size = self.driver.get_window_size
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
        start_x = width * 0.5
        start_y = y + height * 0.8
        end_x = width * 0.5
        end_y = y + height * 0.2
        # 组合find_text包含的元素定位信息
        loc = By.XPATH, "//*[@bounds='[0,260][900,1464]']//*[contains(@text,'{}')]".format(find_text)
        # 获取当前页面元素结构
        page_source = self.driver.page_source
        while True:
            # 首先 查找一次当前页面是否存在要找的元素
            try:
                el2 = self.base_find(loc, timeout=3)
                log.info("找到包含{}的文章了,文章标题为{}".format(find_text,el2.text))
                el2.click()
                # 跳出循环
                break
            except:
                log.info("当前页面没有找到指定文章!")
                # 滑动屏幕
                # self.driver.swipe(width * 0.5, height * 0.7, width * 0.5, height * 0.3, 2000)
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
            if page_source == self.driver.page_source:
                log.info("滑不动了,已经是最后一页了")
                raise NoSuchElementException("已经最后一页了,找不到指定文章{}!".format(find_text))
            else:
                page_source = self.driver.page_source