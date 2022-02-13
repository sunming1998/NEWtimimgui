import pytest
from airtest.utils.logger import get_logger
import logging
from Base.BaseAction import BaseAction
from Pages.pages import Pages
import time


class Test_StartUpApp:
    def setup(self):
        self.base_action = BaseAction()
        self.base_action.clearApp()
        self.base_action.start_app()
        time.sleep(2)

    def test_001_start_app(self):
        """
        点击同意进入首页
        :return:
        """
        Pages().privacypolicy.click_agree()                # 点击同意
        time.sleep(1)
        Pages().privacypolicy.click_jurisdiction()         # 点击同意存储信息
        time.sleep(1)
        Pages().privacypolicy.check_agreement()            # 勾选同意协议
        time.sleep(1)
        result = self.base_action.isExistsEment(Pages().loginbyphone.login_by_phone)       # 实例化一个页面的元素
        if result is True:                                       # 判断这个元素是否存在，如果存在就pass，不存在就调用截图方法
            pass
        else:
            self.base_action.screenshot('start_app_error.png')

        assert result

    def test_002_disagree_quit_app(self):
        """
        点击不同意退出app
        :return:
        """
        Pages().privacypolicy.click_disagree()         # 点击不同意
        time.sleep(2)
        Pages().privacypolicy.click_still_disagree()   # 仍不同意
        time.sleep(1)
        Pages().privacypolicy.click_quit()             # 点击退出
        result = self.base_action.isExistsEment(Pages().privacypolicy.agreement)
        if result is True:
            self.base_action.screenshot('quit_app_error.png')
        else:
            pass

        assert not result

    def test_003_disagree_and_agree(self):
        """
        不同意又同意
        :return:
        """
        Pages().privacypolicy.click_disagree()
        time.sleep(1)
        Pages().privacypolicy.click_agree()
        time.sleep(1)
        Pages().privacypolicy.click_jurisdiction()
        time.sleep(1)
        Pages().privacypolicy.check_agreement()
        result = self.base_action.isExistsEment(Pages().loginbyphone.login_by_phone)
        if result:
            pass
        else:
            self.base_action.screenshot('disagree_and_agree_error.png')

        assert result

    def teardown(self):
        self.base_action.kill_app()


if __name__ == '__main__':
    pytest.main(['-vs', 'test_001_StartUpApp.py'])
