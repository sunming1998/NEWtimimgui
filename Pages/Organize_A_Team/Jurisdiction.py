from Base.BaseAction import BaseAction
import time

class Jurisdiction():
    """
    权限
    """
    base_action = BaseAction()
    microphone = [0.83, 0.40]
    micophone2 = "com.android.packageinstaller:id/permission_allow_button"
    camera = [0.84 , 0.48]
    camera2 = "com.android.packageinstaller:id/permission_allow_button"
    location = [0.83 , 0.64]
    location2 = "com.android.packageinstaller:id/permission_allow_button"
    child = "com.huiian.timing:id/tv_i_know"
    one_touch = "com.huiian.timing:id/tv_start"


    def click_microphone(self):
        """
        点击给予麦克风按钮权限
        :return:
        """
        self.base_action.click_coordinate(self.microphone)

    def click_microphone2(self):
        """
        点击系统给予麦克风按钮权限
        :return:
        """
        self.base_action.clickElement(self.micophone2)

    def click_camera(self):
        """
        给予相机权限
        :return:
        """
        self.base_action.click_coordinate(self.camera)

    def click_camera2(self):
        """
        给予系统相机权限
        :return:
        """
        self.base_action.clickElement(self.camera2)

    def click_location(self):
        """
        点击获取位置权限
        :return:
        """
        self.base_action.click_coordinate(self.location)

    def click_location2(self):
        """
        点击系统获取位置权限
        :return:
        """
        self.base_action.clickElement(self.location2)

    def click_one_touch(self):
        """
        一键开启
        :return:
        """
        self.base_action.clickElement(self.one_touch)


if __name__ =='__main__':
    a = Jurisdiction()
    a.base_action.startApp()
    time.sleep(1)
    a.click_microphone()
    time.sleep(2)
    a.click_microphone2()
    time.sleep(2)
    a.click_camera()
    time.sleep(2)
    a.click_camera2()
    time.sleep(1)
    a.click_location()
    time.sleep(1)
    a.click_location2()
    time.sleep(1)

