from Base.BaseAction import BaseAction
import time

class StartConnecting():
    """
    连线
    """
    base_action = BaseAction()
    fm = "com.huiian.timing:id/iv_FM"                                 # 点击fm按钮
    take_new_connect = "com.huiian.timing:id/iv_start_press"          # ”电话“按钮
    channel_description = "com.huiian.timing:id/tv_dynamics_content"  # 频道描述按钮
    take_text = "com.huiian.timing:id/content_et"                     # 输入按钮
    determine = "com.huiian.timing:id/activity_banner_right_tv"       # 确定按钮
    online = "com.huiian.timing:id/tv_start_online"                   # 上线按钮
    more = "com.huiian.timing:id/iv_function"                         # 更多
    record_video = "com.huiian.timing:id/tv_record"                   # 录制视频按钮
    share = "com.huiian.timing:id/tv_share"                           # 分享按钮
    recent_chat = [0.69, 0.41]                                        # 最近分享
    send = "com.huiian.timing:id/iv_forward"                          # 发送
    take_micophone = "com.huiian.timing:id/tv_mic"                    # 开麦
    take_camera = "com.huiian.timing:id/tv_camera"                    # 摄像头
    screen_sharing = "com.huiian.timing:id/tv_share_screen"           # 屏幕共享
    sharing_by_phone = "com.huiian.timing:id/tv_share_phone"          # 手机屏幕共享
    system_window = "android:id/button1"                                     # 系统弹窗点击确定
    stop_sharing = "com.huiian.timing:id/iv_stop"                     # 停止系统共享
    system_window2 = [0.90, 0.26]                                     # 点击确定
    back = "向上导航"                                                  # 通过name点击返回
    system_window3 = "android:id/button1"                             # 点击立即开始
    end = "com.huiian.timing:id/ll_line"                              # 结束
    right = "com.huiian.timing:id/popupwindow_confirm_right_tv"       # 确定

    def click_fm(self):
        """
        点击fm按钮
        :return:
        """
        self.base_action.clickElement(self.fm)

    def click_connect(self):
        """
        点击连麦按钮
        :return:
        """
        self.base_action.clickElement(self.take_new_connect)

    def click_channel_description(self):
        """
        点击输入描述按钮
        :return:
        """
        self.base_action.clickElement(self.channel_description)

    def send_text(self,text):
        """
        输入你的描述
        :return:
        """
        self.base_action.findElement(self.take_text).set_text(text)

    def click_determine(self):
        """
        点击确认按钮
        :return:
        """
        self.base_action.clickElement(self.determine)

    def click_online(self):
        """
        点击上线
        :return:
        """
        self.base_action.clickElement(self.online)

    def click_more(self):
        """
        点击更多按钮
        :return:
        """
        self.base_action.clickElement(self.more)

    def click_record_video(self):
        """
        点击录制视频
        :return:
        """
        self.base_action.clickElement(self.record_video)

    def click_share(self):
        """
        点击分享
        :return:
        """
        self.base_action.clickElement(self.share)

    def click_recent_chat(self):
        """
        点击发送给最近分享
        :return:
        """
        self.base_action.click_coordinate(self.recent_chat)

    def click_send(self):
        """
        点击分享
        :return:
        """
        self.base_action.clickElement(self.send)

    def click_micophone(self):
        """
        打开麦克风
        :return:
        """
        self.base_action.clickElement(self.take_micophone)

    def click_camera(self):
        """
        打开摄像头
        :return:
        """
        self.base_action.clickElement(self.take_camera)

    def click_screen_sharing(self):
        """
        点击屏幕共享
        :return:
        """
        self.base_action.clickElement(self.screen_sharing)

    def click_sharing_by_phone(self):
        """
        选择手机屏幕共享
        :return:
        """
        self.base_action.clickElement(self.sharing_by_phone)

    def click_system_window(self):
        """
        点击系统弹窗确定
        :return:
        """
        self.base_action.clickElement(self.system_window)

    def click_stop_sharing(self):
        """
        点击结束分享
        :return:
        """
        self.base_action.clickElement(self.stop_sharing)

    def click_system_window2(self):
        """
        点击系统弹窗2
        :return:
        """
        self.base_action.clickElement(self.system_window2)

    def click_back(self):
        """
        点击返回
        :return:
        """
        self.base_action.clickElement(self.back)

    def click_system_window3(self):
        """
        点击系统弹窗
        :return:
        """
        self.base_action.clickElement(self.system_window3)

    def click_end(self):
        """
        结束连线
        :return:
        """
        self.base_action.clickElement(self.end)

    def click_right(self):
        """
        点击确定
        :return:
        """
        self.base_action.clickElement(self.right)


if __name__ == '__main__':
    a = StartConnecting()
    a.click_fm()
    time.sleep(1)
    a.click_connect()
    time.sleep(1)
    a.click_channel_description()
    time.sleep(1)
    a.send_text("学习")
    time.sleep(1)
    a.click_determine()
    time.sleep(1)
    a.click_online()
    time.sleep(1)
    a.click_more()
    a.click_record_video()
    time.sleep(3)
    a.click_share()
    time.sleep(1)
    a.click_recent_chat()
    time.sleep(1)
    a.click_send()
    time.sleep(1)
    a.click_more()
    time.sleep(1)
    a.click_micophone()
    time.sleep(1)
    a.click_camera()
    time.sleep(2)
    a.click_screen_sharing()
    time.sleep(1)
    a.click_sharing_by_phone()
    time.sleep(4)
    a.click_system_window()
    time.sleep(5)
    a.click_stop_sharing()
    time.sleep(3)
    a.click_end()
    time.sleep(1)
    a.click_right()
    time.sleep(1)