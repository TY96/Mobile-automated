from appium.webdriver.common import mobileby


class Login_page():
    by = mobileby.MobileBy()
    # 手机输入框
    user = (by.ID, "com.ansiyida.cgjl:id/editText_phone")
    # 密码输入框
    password = (by.ID, "com.ansiyida.cgjl:id/editText_password")
    # 登录按钮
    enter_button = (by.ID, "com.ansiyida.cgjl:id/btn_login")
    # 注册按钮
    register_button = (by.ID, "com.ansiyida.cgjl:id/text_reg")
    # qq登录按钮
    qq_button = (by.ID, "com.ansiyida.cgjl:id/tv_qq")
    # 微信按钮
    wechat_button = (by.ID, "com.ansiyida.cgjl:id/tv_weiXin")
    # 微博按钮
    microblog_button = (by.ID, "com.ansiyida.cgjl:id/tv_xinLang")

    # 输入手机号码
    def input_user(self,username):
        self.send_keys(username,*self.user)
    # 输入密码

    def input_password(self,pwd):
        self.send_keys(pwd,*self.password)
    # 点击登录按钮

    def click_enter_button(self):
        self.find_element(*self.enter_button).click()
    # 点击注册按钮

    def click_register_button(self):
        self.find_element(*self.register_button).click()
    # 点击qq按钮

    def click_qq_button(self):
        self.find_element(self.qq_button).click()
    # 点击微信按钮

    def click_wechat_button(self):
        self.find_element(self.wechat_button).click()
    # 点击微博按钮

    def click_microblog_button(self):
        self.find_element(self.microblog_button).click()
