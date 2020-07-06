from Common.Base_page1 import base_page
from TestCase import xpath_element
from Common import Log
from time import sleep
from appium.webdriver.webdriver import WebDriver
import allure, sys, inspect,pytest
base = base_page()


# def shot(func):

    # def function(*args, **kwargs):
    #     allure.attach(base.driver.get_screenshot_as_png(),  '此用例执行前的截图', allure.attachment_type.PNG)
    #     i = 1
    #     res = None
    #     while (i <= 3):
    #         try:
    #             res = func(*args, **kwargs)
    #             break
    #         except:
    #             if i == 3:
    #                 raise
    #             i += 1
    #     allure.attach(base.driver.get_screenshot_as_png(),  '此用例执行后的截图', allure.attachment_type.PNG)
    #     return res
    #
    # return function


# @allure.step('case1 step1')
@allure.epic('微信小程序---巴比商城')
@allure.feature('正常流---商品下单')
class TestStart1():

    xp_el = xpath_element

    # @allure.link("www.baidu.com",'百度链接')
    # @allure.testcase("www.baidu.com")
    # @allure.link("www.fanyi.youdao.com",'翻译链接')
    # @allure.issue("www.fanyi.youdao.com","bug记录")
    # @allure.tag('支付时关注的点')
    # @allure.severity(allure.severity_level.CRITICAL)

    # @shot
    @allure.story('进入小程序')
    def test_Enter_the_applet(self):
        # loging = Log.MyLog()
        # loging.log_file("/Users/admin/Desktop/my_file/log")
        with allure.step('点击搜索按钮'):
            base.click(self.xp_el.type_xpath, self.xp_el.search_button)
        with allure.step('搜索框内输入---小程序助手'):
            base.send_keys(self.xp_el.type_id, self.xp_el.search_box, self.xp_el.text1)
        with allure.step('选择第一个搜索结果  "搜一搜  小程序助手"'):
            base.click(self.xp_el.type_xpath, self.xp_el.search_result)
        with allure.step('选择第一个搜索结果'):
            base.click(self.xp_el.type_xpath, self.xp_el.choose_result)
        with allure.step('点击版本查看'):
            base.click(self.xp_el.type_android_uiautomator, self.xp_el.Version_selection)
        with allure.step('选择体验服'):
            base.click(self.xp_el.type_xpath, self.xp_el.Experience_serving)
    # @shot
    @allure.story('进入小程序-选择商品-下单')
    @allure.tag('关注点--支付')
    def test_Place_the_order(self):
        with allure.step('选择自助点餐'):
            base.click(self.xp_el.type_android_uiautomator, self.xp_el.Buffet_order)
        try:
            with allure.step('地址输入框内输入鲜食1号'):
                base.send_keys(self.xp_el.type_xpath, self.xp_el.Address_input_box, self.xp_el.text2)
                base.click(self.xp_el.type_android_uiautomator, self.xp_el.xs)
        except:
            pass
        sleep(5)
        with allure.step('关闭弹出的弹框'):
            try:
                base.click(self.xp_el.type_xpath,self.xp_el.Close_the_bounced)
            except:
                pass
        sleep(5)
        with allure.step('选择打包带走，点击确定'):
            base.click(self.xp_el.type_android_uiautomator, self.xp_el.sure1)
        with allure.step('点击加号，添加"巴比推荐"第一个商品至购物车'):
            base.click(self.xp_el.type_xpath, self.xp_el.choose_one)
        base.find_element(self.xp_el.type_xpath, self.xp_el.name_the_first).get_attribute("text")
        with allure.step('点击购物车，查看商品'):
            base.click(self.xp_el.type_xpath, self.xp_el.view_shopping)
        with allure.step('获取购物车内商品名称'):
            base.find_element(self.xp_el.type_xpath, self.xp_el.name_the_second).get_attribute("text")
        with allure.step('断言选购的商品与购物车是否一致'):
            assert self.xp_el.name_the_first == self.xp_el.name_the_second
        with allure.step('点击去结算'):
            base.click(self.xp_el.type_android_uiautomator, self.xp_el.settle)
        with allure.step('确认支付'):
            base.click(self.xp_el.type_android_uiautomator, self.xp_el.pay_sure)

        print('下单成功')
    # @shot
    @allure.story('关闭程序')
    def test_test_close(self):
        sleep(1)
        base.quit()
# if __name__ == '__main__':
#     start = Test_start1()
#     start.test_Enter_the_applet()
