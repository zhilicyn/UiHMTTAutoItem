from selenium.webdriver.common.by import By

from tools.read_yaml import read_yaml

"""以下为自媒体头条项目url"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

"""以下为文章配置数据"""
article_title = read_yaml("mp_article.yaml")[0][0]
article_channel = "android"

"""以下为APP配置数据"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"


"""以下为自媒体配置数据"""
"""登录页面"""
# 手机号
mp_phone = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 验证码
mp_verify_code = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"

"""首页"""
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
# mp_nickname = By.XPATH, "//dl[@class='user-info']/dt"
# 内容管理
mp_content_manage = By.XPATH, "//span[text()='内容管理']"
# 发布文章
mp_publish_article = By.XPATH, "//li[contains(text(),'发布文章')]"
# 提示
mp_msg_alert = By.CSS_SELECTOR, "div[class='el-message el-message--success']>p"

"""发布文章页面"""
# 文章名称
mp_article_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 文章内容 iframe标签
mp_article_iframe = By.TAG_NAME, "iframe"
mp_article_iframe_id = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容
mp_article_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面 -- 自动
mp_article_cover = By.XPATH, "//span[text()='自动']"
# 频道
mp_channel = By.CSS_SELECTOR, "[placeholder='请选择']"
# 选择频道
mp_check_channel = By.XPATH, "//span[text()='{}']"
# 发布按钮
mp_commit_btn = By.CSS_SELECTOR, "button[class='el-button filter-item el-button--primary']"



""""以下为后台管理页面配置数据"""
# 用户名
mis_username = By.NAME, "username"
# 密码
mis_password = By.NAME, "password"
# 点击获取验证码
mis_code_btn = By.CSS_SELECTOR, ".yzm_btn"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR,"#inp1"
# 昵称
mis_nickname = By.CSS_SELECTOR,".user_info>span"

# 信息管理
mis_info_manage = By.XPATH, "//*[@class='menu']//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[@class='menu']//*[text()='内容审核']"
# 文章名称搜索框
mis_search_article_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 输入频道搜索框
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 选择具体状态 -- 传入状态
mis_status = By.XPATH, "//*[text()='{}']"

# 查询按钮
mis_demand_btn = By.CSS_SELECTOR, ".find"
# 通过按钮
mis_pass_btn = By.XPATH,"//*[text()='通过']/.."
# 确认通过按钮
mis_confirm_pass = By.CSS_SELECTOR,".el-button--primary"
# 文章id
mis_article_id = By.CSS_SELECTOR,".cell>span"

