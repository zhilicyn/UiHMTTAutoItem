from base.base import Base


class AppBase(Base):

    # 滑动方法
    def app_base_swipe(self, tag=1):
        # 获取手机分辨率
        size = self.driver.get_window_size
        width = size['width']
        height = size['height']
        # 向左滑动
        if tag == 1:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5)
        # 向右滑动
        elif tag == 2:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5)
        # 向上滑动
        elif tag == 3:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)
        # 向下滑动
        elif tag == 4:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8)
