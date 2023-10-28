# -*- coding: utf-8 -*-
from DemoQADriver.Elements import navigate_to_subpage
from DemoQADriver.instances import screenshot_on_fail
from DemoQADriver.data.elements import XPATH as xpath_elements
from robot.api.deco import keyword


class CheckBox():

    @screenshot_on_fail
    @keyword("Navigate To Check Box")
    def navigate_to_check_box(self):
        navigate_to_subpage(xpath_elements, 'check_box')
