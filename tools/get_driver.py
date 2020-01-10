from selenium import webdriver


class GetDriver:
    __driver = None
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