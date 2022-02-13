from Base.BaseAction import BaseAction

class Child():
    """
    青少年模式
    """
    base_action = BaseAction()
    set_teen_mode = "com.huiian.timing:id/tv_to_set_youth_mode"
    trun_on_young_mode = [0.48, 0.74]
    know = "com.huiian.timing:id/tv_i_know"


    def click_set_teen_mode(self):
        """
        点击前往设置青少年模式
        :return:
        """
        self.base_action.clickElement(self.set_teen_mode)

    def click_trun_on_young_mode(self):
        """
        确认开启青少年模式
        :return:
        """
        self.base_action.click_coordinate(self.trun_on_young_mode)

