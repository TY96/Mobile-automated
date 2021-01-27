
class func():

    xpath = "xpath"
    id = "id"
    name = "name"
    accessibility_id = "accessibility_id"
    android_uiautomator = "android_uiautomator"

class login():
    # 点击发现按钮
    find_button1 = """UiSelector().text("发现")"""

    # 点击小程序
    small_program = "//android.widget.TextView[contains(@text,('小程序'))]"

    # 点击我的小程序"
    my_small_program = """UiSelector().text("我的小程序")"""

    # 点击小程序助手
    clickBB_small_program = """//android.widget.TextView[contains(@text,('小程序助手'))]"""
    cancel = """//*[@text="取消"]"""


    # 选择小程序
    choose_small_program = """//*[@text="选择小程序"]"""

    BB_test = """UiSelector().text("巴比商城测试")"""

    # 点击版本查看
    Version_selection = 'UiSelector().text("版本查看")'


    # 选择体验服
    Experience_serving = '//*[@text="wxcff7381e631cf54e:pages/version/version.html:VISIBLE"]/android.view.View[5]'

class oneorder():
    #微信获取地理位置接受按钮
    accept = '//*[@text="允许"]'
    # 授权微信地理位置
    all_accept = '//android.widget.Button[contains(@text,"始终允许")]'

    # 选择自助点餐
    Buffet_order = 'UiSelector().text("自助点餐")'

    store_name = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]"""

    #请选择门店
    choose_stores = '//*[@text=请选择门店"]'

    # 地址输入框内输入鲜食1号
    Address_input_box = """//*[@text="wx4900dd1d96a468eb:pages/storeLocation/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]"""
    Address_input_box1 = '//*[@text="按照门店名称搜索"]'
    text2 = "鲜食1号"
    xs = 'UiSelector().text("鲜食1号")'

    #关闭优惠券弹框
    close_coupons = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.widget.Image[2]"""

    # 选择店内堂食，点击确定
    sure1 = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View/android.view.View//android.view.View[4]//android.view.View[6]"""

    # 添加红糖馒头到购物车
    hongtang = """//*[@text="红糖馒头"]"""
    add_hongtang = """//*[@text="红糖馒头"]/parent::*/android.view.View[3]/android.view.View[2]/android.view.View"""

    login_fast= 'UiSelector().text("极速登录")'
    # 点击去结算
    settle = 'UiSelector().text("去结算")'

    # 确认支付
    pay_sure = """//*[@text="确认支付"]"""

    lijizhifu = """//android.widget.TextView[@content-desc="立即支付"]"""

