import pytest
from Base.BaseAction import BaseAction
from Pages.pages import Pages
import time

class Test_Jurisdiction:
    def setup(self):
        self.base_action = BaseAction()
        self.base_action.start_app()


    def test_001_one_touch(self):
        Pages().jurisdiction.click_one_touch()
        time.sleep(1)
        Pages().jurisdiction.click_camera2()
        time.sleep(1)
        Pages().jurisdiction.click_microphone2()
        time.sleep(1)
        Pages().jurisdiction.click_location2()

        result = Pages().child.set_teen_mode

        if result:
            pass
        else:
            self.base_action.screenshot("jurisdiction.png")

        assert result

    def teardown(self):
        self.base_action.kill_app()

if __name__ == '__main__':
    pytest.main(['-vs', 'test_003_Jurisdiction'])