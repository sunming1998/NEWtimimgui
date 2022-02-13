import pytest
from Base.BaseAction import BaseAction
from Pages.pages import Pages
import time

class Test_ConnectionProcess:
    """
    连线房间回归测试
    """
    def setup(self):
        self.base_action = BaseAction()
        self.base_action.start_app()

    def test_001_start_connection(self):
        Pages().startconnecting.click_fm()
        time.sleep(1)
        Pages().startconnecting.click_connect()
        time.sleep(1)
        Pages().startconnecting.click_channel_description()
        time.sleep(1)
        Pages().startconnecting.send_text("学习")
        time.sleep(1)
        Pages().startconnecting.click_determine()
        time.sleep(1)
        Pages().startconnecting.click_online()
        time.sleep(1)
        Pages().startconnecting.click_more()
        time.sleep(1)
        Pages().startconnecting.click_record_video()
        time.sleep(1)
        Pages().startconnecting.click_share()
        time.sleep(1)
        Pages().startconnecting.click_recent_chat()
        time.sleep(1)
        Pages().startconnecting.click_send()
        time.sleep(1)
        Pages().startconnecting.click_more()
        time.sleep(1)
        Pages().startconnecting.click_micophone()
        time.sleep(1)
        Pages().startconnecting.click_camera()
        time.sleep(1)
        Pages().startconnecting.click_screen_sharing()
        time.sleep(1)
        Pages().startconnecting.click_sharing_by_phone()
        time.sleep(1)
        Pages().startconnecting.click_system_window()
        time.sleep(2)
        Pages().startconnecting.click_stop_sharing()
        time.sleep(1)
        Pages().startconnecting.click_end()
        time.sleep(1)
        Pages().startconnecting.click_right()

        result = Pages().startconnecting.take_new_connect
        if result:
            pass
        else:
            self.base_action.screenshot("connection,error.png")

        assert result

    def teardown(self):
        self.base_action.kill_app()

if __name__ == '__main__':
    pytest.main(['-v','test_004_WiredIntercom.py'])