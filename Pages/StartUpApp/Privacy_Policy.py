from Base.BaseAction import BaseAction
import time

class PrivacyPolicy():
    """
    隐私政策
    """
    def __init__(self):
        """
        用户隐私政策以及存储权限
        """
        self.base_action = BaseAction()
        self.agree_button = [0.71,0.68]
        self.jurisdiction = "com.android.permissioncontroller:id/permission_allow_button"
        self.agreement = "com.huiian.timing:id/iv_check"

    def click_agree(self):
        """
        点击同意
        :return:
        """
        self.base_action.click_coordinate(self.agree_button)

    def click_jurisdiction(self):
        """
        同意储存信息
        :return:
        """
        self.base_action.clickElement(self.jurisdiction)

    def check_agreement(self):
        """
        勾选同意协议
        :return:
        """
        self.base_action.clickElement(self.agreement)









if __name__ == '__main__':
    A = PrivacyPolicy()
    A.base_action.stopApp()
    time.sleep(2)
    A.base_action.clearApp()
    time.sleep(2)
    A.base_action.startApp()
    time.sleep(5)
    A.click_agree()
    time.sleep(2)
    A.click_jurisdiction()
    time.sleep(2)
    A.check_agreement()

