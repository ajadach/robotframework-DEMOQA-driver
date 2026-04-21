# -*- coding: utf-8 -*-
from DemoQADriverPackagePlaywright.instances import BROWSER, screenshot_on_fail
from DemoQADriverPackagePlaywright.data.main_page import XPATH as xpath_main
from robot.api.deco import keyword
from DemoQADriverPackagePlaywright.Elements.TextBox import TextBox
from DemoQADriverPackagePlaywright.Elements.CheckBox import CheckBox
from DemoQADriverPackagePlaywright.Elements.WebTables import WebTables


class elements():

    def __init__(self):
        self.TEXTBOX = TextBox()
        self.CHECKBOX = CheckBox()
        self.WEBTABLES = WebTables()

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        BROWSER.click_element(xpath_main['elements'])
