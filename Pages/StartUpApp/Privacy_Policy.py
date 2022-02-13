from Base.BaseAction import BaseAction
import time

class PrivacyPolicy():
    """
    点击隐私政策
    """
    base_action = BaseAction()
    agree_button = [0.69, 0.73]
    disagree_button = 'disagree.png'
    still_disagree = 'still_disagree.png'
    quit = "com.huiian.timing:id/tv_disagree"
    agree = "com.huiian.timing:id/tv_agree"
    jurisdiction = "com.android.packageinstaller:id/permission_allow_button"
    agreement = "com.huiian.timing:id/iv_check"

    def click_agree_button(self):
        """
        点击同意
        :return:
        """
        self.base_action.click_coordinate(self.agree_button)

    def click_disagree(self):
        """
        点击不同意
        :return:
        """
        self.base_action.touchImg(self.disagree_button)

    def click_still_disagree(self):
        """
        点击仍不同意
        :return:
        """
        self.base_action.touchImg(self.still_disagree)

    def click_agree(self):
        """
        后悔了，点击同意
        :return:
        """
        self.base_action.clickElement(self.agree)

    def click_quit(self):
        """
        点击退出
        :return:
        """
        self.base_action.clickElement(self.quit)

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
    A.base_action.clearApp()
    A.base_action.start_app()
    # time.sleep(1)
    # A.base_action.screenshot('error2.jpg')
    # time.sleep(3)
    # A.click_disagree()
    # time.sleep(2)
    # A.base_action.start_app()
    # time.sleep(2)
    # A.click_agree()
    # time.sleep(2)
    # A.click_jurisdiction()
    # time.sleep(2)
    # A.check_agreement()
    # A.base_action.kill_app()
    # time.sleep(2)
    # A.base_action.start_app()

