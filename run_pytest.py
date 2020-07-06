import pytest
import os
if __name__ == '__main__':
    # xml_report_path = './Report/xml/'
    # command_line = ["-s", "./TestCase/test_xiaochengxu.py", "--alluredir", xml_report_path]
    # pytest.main(command_line)
    # cmd = 'allure generate ./Report/xml/ -o ./Report/html/ --clean'
    # os.system(cmd)

    cmd = 'pytest ./TestCase/test_xiaochengxu.py --alluredir ./Report'
    os.system(cmd)
