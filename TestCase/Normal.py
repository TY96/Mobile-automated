from Common.Base_page import base_page
from Common.Log import MyLog
from pages.xpath_element import func,login,oneorder


class Test_BABI(base_page):
    MyLog.info('进入小程序...')

    def test_Cfind_button(self):
        self.click(func.android_uiautomator, login.find_button1)

    def test_small_program(self):
        self.click(func.xpath, login.small_program)

    def test_my_small_program(self):
        self.click(func.android_uiautomator, login.my_small_program)

    def test_clickBB_small_program(self):
        self.click(func.xpath, login.clickBB_small_program)

    def test_Version_selection(self):
        self.click(func.android_uiautomator, login.Version_selection)

    def test_Experience_serving(self):
        self.click(func.xpath, login.Experience_serving)

class Test_one_order(base_page):
    MyLog.info('一键订餐')

    def test_Buffet_order(self):
        self.click(func.android_uiautomator, oneorder.Buffet_order)

    def test_Csure1(self):
        self.click(func.xpath, oneorder.sure1)

    def test_add_hongtang(self):
        self.click(func.xpath, oneorder.add_hongtang)

    def test_settle(self):
        self.click(func.android_uiautomator, oneorder.settle)

    def test_pay_sure(self):
        self.click(func.xpath, oneorder.pay_sure)
        try:
            text = self.find_element(func.xpath, oneorder.lijizhifu).get_attribute('text')
            assert text == '立即支付'
        except Exception as e:
            MyLog.error('%s-断言出错' % e)

    def test_back(self):
        self.back()

    def test_test_close(self):
        self.quit()