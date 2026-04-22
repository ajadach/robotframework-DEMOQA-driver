# -*- coding: utf-8 -*-
from DemoQADriverPackageSelenium.instances import SELENIUM, screenshot_on_fail
from DemoQADriverPackageSelenium.data.main_page import XPATH as xpath_main
from robot.api.deco import keyword
from DemoQADriverPackageSelenium.Elements.TextBox import TextBox
from DemoQADriverPackageSelenium.Elements.CheckBox import CheckBox
from DemoQADriverPackageSelenium.Elements.WebTables import WebTables


class elements():

    def __init__(self):
        self.TEXTBOX = TextBox()
        self.CHECKBOX = CheckBox()
        self.WEBTABLES = WebTables()

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        SELENIUM.click_element(xpath_main['elements'])
