
import pytest
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_case:
    desired_caps = dict()
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "8.0.0"
    desired_caps["deviceName"] = "HUAWEI P9"
    desired_caps["appPackage"] = "com.tencent.mm"
    desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps["newCommandTimeout"] = "8000"
    desired_caps["noSign"] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps["noReset"] = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)

    @pytest.mark.search
    def test_search(self):
        sleep(20)
        # 点击搜索框
        try:
            search_ele = self.driver.find_element_by_accessibility_id('搜索')
            search_ele.click()
        except:
            pass
        sleep(5)
        # 定位搜索框输入"小程序助手"
        self.driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys('小程序助手')
        self.driver.keyevent(66)
        # 选择第一个搜索结果  "搜一搜  小程序助手"
        xcxzs1 = self.driver.find_element_by_xpath("""//*[@resource-id="com.tencent.mm:id/h1s"]""")
        xcxzs1.click()
        sleep(3)
        # 权限弹窗
        try:
            self.driver.find_element_by_xpath('//*[@resource-id="com.android.packageinstaller:id'
                                              '/permission_allow_button"]').click()
        except:
            pass
        sleep(5)
        # 选择小程序助手
        self.driver.find_element_by_xpath('(//android.widget.FrameLayout[@content-desc="containerFrameLayout"])['
                                          '2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                          '.FrameLayout/android.widget.FrameLayout['
                                          '1]/android.webkit.WebView/android.view.View/android.view.View/android.view'
                                          '.View[3]').click()
        sleep(5)
        # 版本选择
        Version_selection = self.driver.find_element_by_android_uiautomator('UiSelector().text("版本查看")')
        Version_selection.click()
        sleep(5)
        # 选择体验服
        Version_selection = self.driver.find_element_by_xpath('//*[@text="wxcff7381e631cf54e:pages/version/version'
                                                              '.html:VISIBLE"]/android.view.View[5]')

        Version_selection.click()
        sleep(10)

    @pytest.mark.test_store
    def test_store(self):
        # 选择自助点餐
        Buffet_order = self.driver.find_element_by_android_uiautomator('UiSelector().text("自助点餐")')
        Buffet_order.click()
        sleep(5)
        # 选择打包带走，立即取餐
        sure1 = self.driver.find_elements_by_android_uiautomator('UiSelector().text("确定")')

        # self.driver.find_element_by_xpath("""//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android
        #                                     .view.View[1]/android.view.View[4]/android.view.View[6]""")
        sure1[1].click()

        # 点击加号，添加"巴比推荐"第一个商品至购物车

        choose1 = self.driver.find_element_by_xpath("""//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Image[1]""")
        choose1.click()
        # # 已经添加过商品，再添加  +
        # choose2 = self.driver.find_element_by_xpath("""//*[@@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android .view.View [1] /android.view.View [7] /android.view.View [1] /android.view.View [1] /android.view.View [1] /android.view.View [ 1] /android.view.View [2] /android.view.View [2] /android.widget.Image [2]""")
        # choose2.click()

        # 获取第一个商品的名称
        name = self.driver.find_element_by_xpath("""//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]""").get_attribute('text')

        # 点击购物车，查看商品
        car = self.driver.find_element_by_xpath("""//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]""")
        car.click()
        # 获取购物车内商品名称
        name2 = self.driver.find_element_by_xpath("""//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]""").get_attribute('text')
        assert name == name2
        print('准备下单')

        settle = self.driver.find_element_by_android_uiautomator('UiSelector().text("去结算")')
        settle.click()
        sleep(3)
        pay_sure = self.driver.find_element_by_android_uiautomator('UiSelector().text("确认支付")')
        pay_sure.click()
        sleep(6)



    def test_close(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-v', 'all_xiao.py'])
# app-inspector -u C4Y7N16926002531 --verbose
