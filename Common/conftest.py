from appium import webdriver
import pytest


# @pytest.fixture(scope="session")
class phone():

    def set_(self):
        self.desired_caps = dict()
        self.desired_caps["platformName"] = "Android"
        self.desired_caps["platformVersion"] = "8.0.0"
        self.desired_caps["deviceName"] = "HUAWEI P9"
        self.desired_caps["appPackage"] = "com.tencent.mm"
        self.desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        self.desired_caps['automationName'] = 'UiAutomator2'
        self.desired_caps["newCommandTimeout"] = "8000"
        self.desired_caps["noSign"] = True
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.desired_caps["noReset"] = True
        #chromedriver文件位置
        self.desired_caps["chromedriver-executable"] = "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
        # 支持X5内核应用自动化配置
        self.desired_caps["recreateChromeDriverSessions"] = True
        # self.desired_caps["ChromeOptions options"] = "new ChromeOptions()"
        # self.desired_caps["androidProcess"] = "com.tencent.mm:appbrand0"


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(15)

        return self.driver


@pytest.fixture(scope="session")
def test_session():
    print('------------------session之前---------------------------')
    yield
    print('------------------session之后---------------------------')


@pytest.fixture(scope="module")
def test_module():
    print('------------------module之前---------------------------')
    yield
    print('------------------module之后---------------------------')


@pytest.fixture(scope="class")
def test_class():
    print('------------------class之前---------------------------')
    yield
    print('------------------class之后---------------------------')


@pytest.fixture(scope="function")
def test_function():
    print('------------------function之前---------------------------')
    yield
    print('------------------function之后---------------------------')
    # desired_caps = dict()
    # desired_caps["platformName"] = "Android"
    # desired_caps["platformVersion"] = "8.0.0"
    # desired_caps["deviceName"] = "HUAWEI P9"
    # desired_caps["appPackage"] = "com.tencent.mm"
    # desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
    # desired_caps['automationName'] = 'UiAutomator2'
    # desired_caps["newCommandTimeout"] = "8000"
    # desired_caps["noSign"] = True
    # desired_caps["unicodeKeyboard"] = True
    # desired_caps["resetKeyboard"] = True
    # desired_caps["noReset"] = True
    #
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    # driver.implicitly_wait(5)
    #
    # return driver
