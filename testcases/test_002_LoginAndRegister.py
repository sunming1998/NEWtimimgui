import pytest
from airtest.utils.logger import get_logger
import logging
from Base.BaseAction import BaseAction
from Pages.pages import Pages
import time

class Test_Login_And_Register:
    def setup(self):
        self.base_action = BaseAction()
        self.base_action.start_app()
        time.sleep(2)

    def test_001_login_by_phone(self):
        """
        通过手机号密码登录
        :return:
        """
        Pages().loginbyphone.click_agreement()
        time.sleep(1)
        Pages().loginbyphone.click_login_by_phone()
        time.sleep(1)
        Pages().loginbyphone.enter_phone(10000000099)
        time.sleep(1)
        Pages().loginbyphone.click_agreement()
        time.sleep(1)
        Pages().loginbyphone.click_login_by_password()
        time.sleep(1)
        Pages().loginbyphone.enter_password(111111)
        time.sleep(1)
        Pages().loginbyphone.click_register()

        result = Pages().jurisdiction.one_touch
        if result :
            pass
        else:
            self.base_action.screenshot("login_by_phone_error.png")

        assert result

if __name__ == '__main__':
    pytest.main(['-vs', 'test_002_LoginAndRegister.py'])
