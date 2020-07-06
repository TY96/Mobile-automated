type_xpath = "xpath"
type_id = 'id'
type_name = "name"
type_accessibility_id = "accessibility_id"
type_android_uiautomator = "android_uiautomator"

# 点击搜索按钮
search_button = """//*[@resource-id="com.tencent.mm:id/f8y"]"""

# 搜索框内输入---小程序助手
search_box = "com.tencent.mm:id/bhn"
text1 = "小程序助手"

# 选择第一个搜索结果  "搜一搜  小程序助手"
search_result = """//*[@resource-id="com.tencent.mm:id/h1s"]"""

# 选择第一个搜索结果
choose_result = '(//android.widget.FrameLayout[@content-desc="containerFrameLayout"])['"2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget"'.FrameLayout/android.widget.FrameLayout[''1]/android.webkit.WebView/android.view.View/android.view.View/android.view''.View[3]'

# 点击版本查看
Version_selection = 'UiSelector().text("版本查看")'

# 选择体验服
Experience_serving = '//*[@text="wxcff7381e631cf54e:pages/version/version''.html:VISIBLE"]/android.view.View[5]'
# ------------------------------------------------------#
# 选择自助点餐
Buffet_order = 'UiSelector().text("自助点餐")'

# 地址输入框内输入鲜食1号
Address_input_box = """//*[@text="wx4900dd1d96a468eb:pages/storeLocation/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]"""
text2 = '鲜食1号'
xs = 'UiSelector().text("鲜食1号")'

# 关闭弹出的弹框
Close_the_bounced = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.widget.Image[2]"""


# 选择打包带走，点击确定
sure1 = 'UiSelector().text("确定")'

# 点击加号，添加"巴比推荐"第一个商品至购物车
choose_one = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Image[1]"""

# 获取第一个商品的名称
name_the_first = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]"""

# 点击购物车，查看商品
view_shopping = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]"""

# 获取购物车内商品名称
name_the_second = """//*[@text="wx4900dd1d96a468eb:pages/index/index.html:VISIBLE"]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]"""

# 点击去结算
settle = 'UiSelector().text("去结算")'

# 确认支付
pay_sure = 'UiSelector().text("确认支付")'

#
# import random,string
#
# def get_name():
#     # first_name = '赵', '钱', '孙', '李'
#     # boy = '鹏', '逸', '越', '文'
#     # girl = '娜', '梅', '雯', '艳'
#     # ming1 =random.choice(list1)
#     # if sex == '男' :
#     #     ming2 = random.choice(list2)
#     # else :
#     #     ming2 = random.choice(list3)
#     #
#     # a = random.randint(0, 1)
#     # print(a)
#     # if a == 0:
#     #     ming3 =' '
#     # else:
#     #     if sex =='男':
#     #         ming3 = random.choice(list2)
#     #     else:
#     #         ming3 = random.choice(list3)
#     # name = ming1+ming2+ming3
#     # print(name)
#     # return name
#     list=[]
#
#     x ='zdadfeaa'
#     y = 'A','Z'
#
#     a = random.randint(0,9)
#     b = random.choice(x)
#     c = random.choice(y)
#
#     e = random.sample(x, 5)
#
#     list.append(str(a))
#     list.append(str(b))
#     list.append(str(c))
#     list.extend(str(e))
#     print(list)
#
#     ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#     print(ran_str)
# if __name__ == '__main__':
#     get_name()
