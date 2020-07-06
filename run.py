from Common import cmd,Log
import pytest

if __name__ == '__main__':
    # start = Test_start1()
    # start.test_Enter_the_applet()
    # 'test_xiaochengxu/ --alluredir ./result/'
    loging = Log.MyLog()
    CMD = cmd.cmd_invoke()
    xml_report_path = './Report/xml/'
    html_report_path = './Report/html/'

    # pytest.main(['-s', '-q', '-v', './TestCase/test_xiaochengxu.py', ])
    pytest.main(['-s', '-q', '--alluredir', xml_report_path, './TestCase/test_xiaochengxu.py'])

    cmd = "allure generate %s -o %s --clean" % (xml_report_path, html_report_path)
    # 'allure generate ./ result / -o ./ report / --clean'
    try:
        CMD.popen(cmd)
    except Exception:
        loging.error('执行用例失败，请检查环境配置')
        raise
