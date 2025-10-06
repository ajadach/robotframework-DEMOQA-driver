# -*- coding: utf-8 -*-
from DemoQADriverPackage.instances import SELENIUM, screenshot_on_fail
from DemoQADriverPackage.data.main_page import XPATH as xpath_main
from robot.api.deco import keyword


class forms():

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        SELENIUM.click_element(xpath_main['forms'])
