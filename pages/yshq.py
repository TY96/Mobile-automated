from appium.webdriver.common import mobileby


class begin():
    mm = mobileby.MobileBy()
    mb = mobileby.By()
    search1 = (mm.ACCESSIBILITY_ID, "搜索")
    search2 = (mb.ID, 'com.tencent.mm:id/bhn')
    search3 = (mb.XPATH, '//*[@resource-id="com.tencent.mm:id/h1s"]')
    search4 = (mb.XPATH, """(//android.widget.FrameLayout[@content-desc="containerFrameLayout"])['
                            '2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                            '.FrameLayout/android.widget.FrameLayout['
                            '1]/android.webkit.WebView/android.view.View/android.view.View/android.view'
                            '.View[3]""")
    search5 = (mm.ANDROID_UIAUTOMATOR, """UiSelector().text("版本查看")""")
    search6 = (mb.XPATH, """//*[@text="wxcff7381e631cf54e:pages/version/version'
                                        '.html:VISIBLE"]/android.view.View[5]""")

    def search_1(self):
        self.find_element(self.search1).click()

    def search_2(self):
        self.send_keys('小程序助手', self.search2)
        self.driver.keyevent(66)

    def search_3(self):
        self.find_element(self.search3).click()

    def search_4(self):
        self.find_element(self.search4).click()

    def search_5(self):
        self.find_element(self.search5).click()

    def search_6(self):
        self.find_element(self.search6).click()
