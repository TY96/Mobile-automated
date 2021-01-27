from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy as MBy
from appium.webdriver.common.touch_action import TouchAction
from Common.conftest import phone
import time,allure




def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), '执行之前截图', allure.attachment_type.PNG)
        res = None
        try:
            res = func(*args, **kwargs)
        except:
            pass

        allure.attach(args[0].driver.get_screenshot_as_png(), "执行之后截图", allure.attachment_type.PNG)
        return res
    return function

    #     allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)
    #     i = 1
    #     res = None
    #     while(i <= 3):
    #         try:
    #             res = func(*args, **kwargs)
    #             break
    #         except:
    #             if i == 3:
    #                 raise
    #             i += 1
    #     allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
    #     return res
    # return function


class base_page:

    def __init__(self):
        # self.driver = driver

        p = phone()
        self.driver = p.set_()

    def find_element(self, type, xpath):
        """
        通过元素的类型和xpath定位，返回一个对象
        :param type:  ID，name, xpath, accessibility_id, android_uiautomator
        :param xpath: 元素xpath
        :return:
        """
        try:
            if type == "id":
                try:
                    return self.driver.find_element(By.ID, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False

            elif type == "name":
                try:
                    return self.driver.find_element(By.NAME, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False

            elif type == "xpath":
                try:
                    return self.driver.find_element(By.XPATH, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False

            elif type == "accessibility_id":
                try:
                    return self.driver.find_element(MBy.ACCESSIBILITY_ID, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False

            elif type == "android_uiautomator":
                try:
                    return self.driver.find_element(MBy.ANDROID_UIAUTOMATOR, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False

        except:
            allure.attach(self.driver.get_screenshot_as_png(), '未找到元素', allure.attachment_type.PNG)

        # """重写find_element方法，显式等待"""
        #
        # try:
        #     WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(xpath))
        #     return self.driver.find_element(xpath)
        # except Exception as e:
        #     raise e

    def find_elements(self, type, xpath):
        """
        通过元素的类型和xpath定位，返回多个对象
        :param type:  ID，name, xpath, accessibility_id, android_uiautomator
        :param xpath: 元素xpath
        :return:
        """
        try:
            if type == "id":

                try:
                    return self.driver.find_elements(By.ID, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False
            elif type == "name":

                try:
                    return self.driver.find_elements(By.NAME, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False
            elif type == "xpath":

                try:
                    return self.driver.find_elements(By.XPATH, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False
            elif type == "accessibility_id":

                try:
                    return self.driver.find_elements(MBy.ACCESSIBILITY_ID, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False
            elif type == "android_uiautomator":

                try:
                    return self.driver.find_elements(MBy.ANDROID_UIAUTOMATOR, xpath)
                except:
                    print("未找到%dstype--%dsvalue" % (type, xpath))
                    return False
        except:
            self.screen_shot()

    # def click1(self,xpath):
    #     self.driver.find_element_by_android_uiautomator(xpath).click()

    @shot
    def click(self, type, xpath):
        """
        根据元素的类型和xpath定位元素并点击
        :param type: 同上
        :param xpath: 同上
        :return:
        """
        # self.find_element(type, self.xpath).click()
        # self.driver.find_element(type, xpath).click()
        el = self.find_element(type, xpath)
        TouchAction(self.driver).tap(el).perform()

    # @shot
    def send_keys(self, type, xpath, text):
        """
        根据元素的类型和xpath定位元素后，再传输文本内容
        :param type: 同上
        :param xpath: 同上
        :param text: 传输的文本内容
        :return:
        """
        self.driver.find_element(type, xpath).clear()
        self.driver.find_element(type, xpath).send_keys(text)
        # self.driver.send_keys(text)

    # @shot
    def scroll_down(self, n):
        """
        手机左上角为原点坐标，手机屏幕向下滚动，默认滚动时间为1000ms
        :param n: 滚动的次数
        :return:
        """
        # 获取屏幕宽度
        x = self.driver.get_window_size()["width"]
        # 获取屏幕长度
        y = self.driver.get_window_size()["height"]
        # 横坐标为xw
        xw = int(x * 0.5)
        # 纵坐标为yh1滑到yh2，即从上向下滑动，屏幕实现下滑操作
        yh1 = int(y * 0.5)
        yh2 = int(y * 0.2)
        for i in range(n):
            self.driver.swipe(xw, yh1, xw, yh2, 1000)
            time.sleep(1)

    # @shot
    def scroll_up(self, n):
        """
        参考向下滚动：scroll_down
        :param n:
        :return:
        """
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        xw = int(x * 0.5)
        yh1 = int(y * 0.8)
        yh2 = int(y * 0.5)
        for i in range(n):
            self.driver.swipe(xw, yh1, xw, yh2, 1000)
            time.sleep(1)

    # @shot
    def scroll_left(self, n):
        """
        参考向下滚动：scroll_down
        :param n:
        :return:
        """
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        yh = y * 0.7
        xw1 = x * 0.2
        xw2 = x * 0.3
        for i in range(n):
            self.driver.swipe(xw1, yh, xw2, yh, 1000)
            time.sleep(1)

    # @shot
    def scroll_right(self, n):
        """
        参考向下滚动：scroll_down
        :param n:
        :return:
        """
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        yh = y * 0.7
        xw1 = x * 0.3
        xw2 = x * 0.2
        for i in range(n):
            self.driver.swipe(xw1, yh, xw2, yh, 1000)
            time.sleep(1)

    def t_Time(self):
        """
        获取时间戳
        :return:
        """
        Time = int(time.time())
        return Time

    def screen_shot(self):
        """
        截图,默认截图位置，文件名通过时间戳命名
        :return:
        """
        time_ = self.t_Time
        filename = "/Users/admin/Desktop/my_file/图片/%s.png" % time_
        # # self.driver.save_screenshot('screen.jpg')
        # return self.driver.get_screenshot_as_file(filename)
        #
        self.driver.get_screenshot_as_file(filename)

    def get_screen(self, filename):
        """
        截图1，输入保存目录位置
        :param filename:
        :return:
        """
        # time_ = self.getTime()
        # filename = "/Users/admin/Desktop/my_file/图片/%s.png" % time_
        # self.driver.save_screenshot()
        self.driver.screenshot_as_file(filename)

    # @shot
    def back(self):
        """
        返回
        :return:
        """
        self.driver.keyevent(4)

    # @shot
    def long_press(self, type, loc):
        """
        长按元素
        :param type:
        :param loc:
        :return:
        """
        if type == "xpath":
            el = self.driver.find_element_by_xpath(loc)
            TouchAction(self.driver).long_press(el).perform()
        elif type == "id":
            el = self.driver.find_element_by_id(loc)
            TouchAction(self.driver).long_press(el).perform()
        elif type == "text":
            el = self.driver.file_detector_context(loc)
            TouchAction(self.driver).long_press(el).perform()
        elif type == "android_uiautomator":
            el = self.driver.file_detector_context(loc)
            TouchAction(self.driver).long_press(el).perform()

    # @shot
    def tap_el(self, x, y, duration=50):
        """
        点击坐标
        :param x:
        :param y:
        :param duration:
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        a = [float(x) / width] * width
        x1 = int(a)
        b = [float(y) / height] * height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    def el_exist(self, xpath):
        if self.driver.find_element_by_xpath(xpath):
            return True
        else:
            return False

    def reinstall_app(self,package_name,package_path):
        if self.driver.is_app_installed(package_name):
            print('准备卸载')
            self.driver.remove_app(package_name)
            print('正在安装，请稍等...')
            self.driver.install_app(package_path)
            print("重装成功")
        else:
            self.driver.install_app(package_path)
            print("安装成功")

    # @shot
    def quit(self):
        """
        关闭软件
        :return:
        """
        self.driver.quit()
