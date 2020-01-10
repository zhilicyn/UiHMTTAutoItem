import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog

# 获取日志对象
log = GetLog().get_logger()

class Base:
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素 --> 给输入/点击/获取文本方法使用
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素:".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 定位一组元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素:".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))


    # 输入方法
    def base_input(self, loc, text):
        # 调用查找元素方法
        ele = self.base_find(loc)
        # 清空
        log.info("正在执行清空操作")
        ele.clear()
        # 输入操作
        log.info("正在给 {} 元素执行输入操作:{}".format(loc,text))
        ele.send_keys(text)

    # 点击方法
    def base_click(self, loc):
        log.info("正在对{}元素执行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取文本方法
    def base_get_text(self, loc):
        log.info("正在获取{}元素的文本内容:{}".format(loc,self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 截图
        log.info("出现异常!正在执行截图操作!")
        self.driver.get_screenshot_as_file("./images/err.png")
        # 调用将图片写入报告
        self.__base_write_image()

    # 将图片写入allure报告
    def __base_write_image(self):
        log.info("出现异常!正在将截图写入报告!")
        with open("./images/err.png","rb")as f:
            allure.attach("错误原因",f.read(),allure.attach_type.PNG)