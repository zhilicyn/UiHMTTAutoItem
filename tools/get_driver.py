from time import sleep

from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    __driver = None
    __app_driver = None
    # 获取driver
    @classmethod
    def get_driver(cls,url):
        if cls.__driver is None:
            # 获取driver对象
            cls.__driver = webdriver.Chrome()
            # 最大化窗口
            cls.__driver.maximize_window()
            # 打开url
            cls.__driver.get(url)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            # 置空
            cls.__driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            cap = {
                "platformName": "Android", # 测试的平台(Android和iOS)
                "platformVersion": "5.1", # 设备系统版本
                "deviceName": "模拟器", # 设备名称
                "appPackage": page.appPackage, # 待测应用包名
                "appActivity": page.appActivity, # 待测应用的启动名
                'resetKeyboard': True, # 解决脚本输入中文的问题
                'unicodeKeyboard': True,
                'noReset':False # 不重置应用,设置为False.表示每次启动APP都重置应用
        }
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            # 置空
            cls.__app_driver = None

if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(5)