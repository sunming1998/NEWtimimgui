from Base.BaseAction import BaseAction
import time

class Publish_Journal():
    base_action = BaseAction()
    publish = "com.huiian.timing:id/iv_publish"
    take_a_video = [0.31, 0.57]
    take_a_video2 = "com.huiian.timing:id/mTouchRecordBtn"
    confirm = "com.huiian.timing:id/mTouchSendView"
    take_a_text = "com.huiian.timing:id/edit_content"
    release = "com.huiian.timing:id/tv_publish"
    publish_text = [0.69, 0.57]
    take_a_text2 = "com.huiian.timing:id/content_et"
    release2 = "com.huiian.timing:id/activity_banner_right_tv"

    def click_publish(self):
        """
        点击发布按钮
        :return:
        """
        self.base_action.clickElement(self.publish)

    def click_take_a_video(self):
        """
        点击拍视频按钮
        :return:
        """
        self.base_action.click_coordinate(self.take_a_video)

    def holdiong_down(self):
        """
        按住拍视频
        :return:
        """
        self.base_action.clickElementLongTime(self.take_a_video2)

    def click_confim(self):
        """
        点击确认
        :return:
        """
        self.base_action.clickElement(self.confirm)

    def import_text(self,text):
        """
        输入内容
        :return:
        """
        self.base_action.findElement(self.take_a_text).set_text(text)

    def click_release(self):
        """
        点击发布
        :return:
        """
        self.base_action.clickElement(self.release)

    def click_pulish_text(self):
        """
        点击发布图文日记
        :return:
        """
        self.base_action.clickElement(self.publish_text)

    def import_text2(self,text):
        """
        输入日记内容
        :return:
        """
        self.base_action.findElement(self.take_a_text2).set_text(text)

    def click_replease2(self):
        """
        点击发布
        :return:
        """
        self.base_action.clickElement(self.release2)

if __name__ =='__main__':
    a = Publish_Journal()
    a.base_action.startApp()
    a.click_publish()
    time.sleep(1)
    a.click_take_a_video()
    time.sleep(2)
    a.holdiong_down()
    time.sleep(3)
    a.click_confim()
    time.sleep(1)
    a.import_text("啊哈哈")
    time.sleep(3)
    a.click_release()

