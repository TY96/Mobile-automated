from Common.Base_page import base_page
from time import sleep

base = base_page()


def reinstall():
    base.reinstall_app('com.tencent.mm', "/Users/admin/Desktop/my_file/aa-person/package/weixin7012.apk")
    sleep(5)
    base.driver.launch_app()
    base.click('id', 'com.tencent.mm:id/f34')
    base.send_keys('id', 'com.tencent.mm:id/bem', '微信号')
    base.click('id', 'com.tencent.mm:id/dw1')
    base.click('id', 'com.tencent.mm:id/dj6')
    base.click('id', 'android:id/button1')
    base.send_keys('xpath', "//*[@text='请填写微信密码']", '微信密码')
    base.click('id', 'com.tencent.mm:id/dw1')
    print('滑块自动化不会，自行操作')


if __name__ == '__main__':
    reinstall()
