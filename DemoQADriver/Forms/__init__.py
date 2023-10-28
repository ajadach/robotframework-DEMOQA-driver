# -*- coding: utf-8 -*-
from DemoQADriver.instances import SELENIUM, screenshot_on_fail
from DemoQADriver.data.main_page import XPATH as xpath_main
from robot.api.deco import keyword


def navigate_to_subpage(self, xpath_dict, subpage_name):
    SELENIUM.click_element(xpath_dict[subpage_name])


class forms():

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        SELENIUM.click_element(xpath_main['forms'])
