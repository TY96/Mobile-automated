from Common.Base_page import base_page
from Common.Log import MyLog
from pages.xpath_element import func,login,oneorder

from time import sleep
import allure


@allure.epic('微信小程序---巴比商城')
@allure.feature('正常流---商品下单')
class TestStart1():
    MyLog.info('开始测试...')
    base = base_page()
    # @allure.link("www.baidu.com",'百度链接')
    # @allure.testcase("www.baidu.com")
    # @allure.link("www.fanyi.youdao.com",'翻译链接')
    # @allure.issue("www.fanyi.youdao.com","bug记录")
    # @allure.tag('支付时关注的点')
    # @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('进入小程序')
    def test_Cfind_button(self):
        with allure.step('点击发现按钮'):
            sleep(5)
            self.base.click(func.android_uiautomator, login.find_button1)

    def test_small_program(self):
        if self.base.el_exist(login.small_program):
        #     with allure.step('点击小程序'):
            self.base.click(func.xpath, login.small_program)
        else:
            self.base.scroll_down(1)
        #     with allure.step('点击小程序'):
            self.base.click(func.xpath, login.small_program)
    def test_my_small_program(self):
        # with allure.step('点击我的小程序'):
        self.base.click(func.android_uiautomator, login.my_small_program)
        if self.base.el_exist(login.clickBB_small_program):
        #     with allure.step('点击小程序助手'):
            self.base.click(func.xpath, login.clickBB_small_program)
            if self.base.el_exist(login.cancel):
                self.base.click(func.xpath, login.cancel)
        else:
            MyLog.error("请将'小程序助手'添加至'我的小程序'后再试")
            self.base.quit()
        sleep(3)
    def test_choose_small_program(self):
        if self.base.el_exist(login.choose_small_program):

            self.base.click(func.android_uiautomator, login.BB_test)
            self.base.click(func.android_uiautomator, login.Version_selection)
        else:

            self.base.click(func.android_uiautomator, login.Version_selection)
        sleep(3)
        self.base.click(func.xpath, login.Experience_serving)
        sleep(5)

    def test_Version_selection(self):
        self.base.click(func.android_uiautomator, login.Version_selection)

    def test_Experience_serving(self):
        self.base.click(func.xpath, login.Experience_serving)

    @allure.story('进入小程序-选择商品-下单')
    @allure.tag('关注点--支付')
    def test_Caccept(self):
        sleep(5)
        try :
        # if self.base.el_exist(oneorder.accept):
            self.base.click(func.xpath, oneorder.accept)

            self.base.click(func.xpath, oneorder.all_accept)

        except:
            self.base.click(func.xpath, oneorder.all_accept)


    def test_Buffet_order(self):

        with allure.step('选择自助点餐'):
            self.base.click(func.android_uiautomator, oneorder.Buffet_order)

    def test_choose_stores(self):
        try:
            self.base.click(func.xpath, oneorder.sure1)
        except:
            pass

        if self.base.find_element(func.xpath, oneorder.store_name).get_attribute("text")!= '鲜食1号':

            self.base.click(func.xpath, oneorder.store_name)

            self.base.click(func.xpath, oneorder.Address_input_box)
            self.base.send_keys(func.xpath, oneorder.Address_input_box1, oneorder.text2)
            self.base.click(func.android_uiautomator, oneorder.xs)

        # 切换门店到鲜食1号
        elif self.base.el_exist(oneorder.choose_stores):
            with allure.step('地址输入框内输入鲜食1号'):
                self.base.click(func.xpath, oneorder.Address_input_box)
                self.base.send_keys(func.xpath, oneorder.Address_input_box1, oneorder.text2)
                self.base.click(func.android_uiautomator, oneorder.xs)


    def test_Csure1(self):

        with allure.step('选择店内堂食，点击确定'):
            self.base.click(func.xpath, oneorder.sure1)

    def test_close_coupons(self):
        sleep(5)
        if self.base.el_exist(oneorder.close_coupons):
            self.base.click(func.xpath, oneorder.close_coupons)

    def test_Csure2(self):
        with allure.step('选择店内堂食，点击确定'):
            self.base.click(func.xpath, oneorder.sure1)

    def test_add_hongtang(self):
        if self.base.el_exist(oneorder.hongtang):
            with allure.step('点击加号，添加"红糖馒头"'):
                self.base.click(func.xpath, oneorder.add_hongtang)
        else:
                self.base.scroll_down(1)
                self.base.click(func.xpath, oneorder.add_hongtang)



    def test_settle(self):

        with allure.step('点击去结算'):
            self.base.click(func.android_uiautomator, oneorder.settle)
        sleep(3)

    def test_pay_sure(self):
        with allure.step('确认支付'):
            self.base.click(func.xpath, oneorder.pay_sure)
        sleep(6)
        text = self.base.find_element(func.xpath, oneorder.lijizhifu).get_attribute('text')
        assert text=='立即支付'
        print('已拉起支付')

    def test_back(self):
        self.base.back()

        print('下单成功')

    @allure.story('关闭程序')
    def jtest_test_close(self):
        sleep(1)
        self.base.quit()
# if __name__ == '__main__':
#     start = Test_start1()
#     start.test_Enter_the_applet()
