import pytest
from airtest.utils.logger import get_logger
import logging
from Base.BaseAction import BaseAction
from Pages.pages import Pages
import time


class Test_Login_And_Register:
    def setup(self):
        self.base_action = BaseAction()