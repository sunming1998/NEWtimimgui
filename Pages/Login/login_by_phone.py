from Base.BaseAction import BaseAction
import time


class LoginByPhone:
    """
    手机号登录
    """
    base_action = BaseAction()
    login_by_phone = "com.huiian.timing:id/iv_phone"
    send_phone = "com.huiian.timing:id/phone_et"
    take_captcha = "com.huiian.timing:id/login_verify_tv"
    login_by_pwd = "com.huiian.timing:id/activity_banner_right_tv"
    agreement = "com.huiian.timing:id/iv_check"
    send_phone_2 = "com.huiian.timing:id/et_phone"
    send_password = "com.huiian.timing:id/et_password"
    register = "com.huiian.timing:id/tv_login_verify"

    def click_login_by_phone(self):
        """
        点击手机登录按钮
        :return:
        """
        self.base_action.clickElement(self.login_by_phone)

    def enter_phone(self,phone):
        """
        输入手机号
        :return:
        """
        self.base_action.set_text(self.send_phone,phone)

    def click_take_captcha(self):
        """
        点击获取验证码按钮
        :return:
        """
        self.base_action.clickElement(self.take_captcha)

    def click_agreement(self):
        """
        勾选用户协议
        :return:
        """
        self.base_action.clickElement(self.agreement)

    def click_login_by_password(self):
        """
        点击密码登录
        :return:
        """
        self.base_action.clickElement(self.login_by_pwd)

    def enter_phone_by_pwd(self, phone):
        """
        输入手机号使用密码登录
        :return:
        """
        self.base_action.findElement(self.send_phone_2).set_text(phone)

    def enter_password(self,pwd):
        """
        输入手机号对应的密码
        :return:
        """
        self.base_action.set_text(self.send_password,pwd)

    def click_register(self):
        """
        点击登录
        :return:
        """
        self.base_action.clickElement(self.register)


if __name__ =='__main__':
    a = LoginByPhone()
    # a.base_action.clearApp()
    # time.sleep(1)
    # a.base_action.startApp()
    # time.sleep(2)
    a.click_login_by_phone()
    time.sleep(1)
    a.click_agreement()
    time.sleep(1)
    a.click_login_by_password()
    time.sleep(1)
    a.enter_phone_by_pwd(10000000099)
    time.sleep(2)
    a.enter_password(111111)
    time.sleep(2)
    a.click_register()
