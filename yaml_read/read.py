import yaml
from Common.conftest import phone
from Common.Base_page import base_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.mobileby import MobileBy as MBy

# fr = open('/Users/admin/Desktop/my_file/Mobile-automated/yaml_read/yuansu.yaml','r')
# yaml_read = yaml.safe_load(fr)
#
# print(yaml_read)


class yamltest():
    def __init__(self):
        p = phone()
        self.driver = p.set_()
        self.base = base_page()
    def loadStep(self,po_path, key, **kwargs):
        file = open(po_path, 'r', encoding='utf-8')
        po_data = yaml.safe_load(file)
        po_method = po_data[key]
        print(po_method)
        for step in po_method:

            element = self.driver.find_element(by=step['by'], value=step['locator'])

            action = step['action']  # 这里把action的值转化成了小写

            if action == "click":  # 写上小写，yaml文件中也要写上小写
                element.click()

            elif action == "sendkeys":  # 这里要写小写，ymal文件中也要写上小写
                text = str(step['text'])
                self.base.send_keys(step['by'], step['locator'],text)

            elif action == "swipe_down":
                self.base.scroll_down(1)
                # WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((step['by'],step['locator'])))

            elif action == "swipe_up":
                self.base.scroll_up(1)

            else:

                print("UNKONW COMMAND %s" % step)


if __name__ == '__main__':
    loadStep1 = yamltest()
    loadStep1.loadStep('/Users/admin/Desktop/my_file/Mobile-automated/yaml_read/yuansu.yaml','login')