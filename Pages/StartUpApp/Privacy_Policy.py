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
        self.agree_button = [777,1650]
        self.jurisdiction = "com.android.permissioncontroller:id/permission_allow_button"
        self.agreement = "com.huiian.timing:id/iv_check"

    def click_agree(self):
        """
        点击同意
        :return:
        """
        zb = self.base_action.get_percentage(self.agree_button)
        self.base_action.click_coordinate(zb)

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
    A.base_action.startApp()
    time.sleep(5)
    A.agree()

