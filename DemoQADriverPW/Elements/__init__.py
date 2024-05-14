# -*- coding: utf-8 -*-
from DemoQADriverPW.instances import BROWSER, screenshot_on_fail
from DemoQADriver.data.main_page import XPATH as xpath_main
from robot.api.deco import keyword
from DemoQADriverPW.Elements.TextBox import TextBox
from DemoQADriverPW.Elements.CheckBox import CheckBox
from DemoQADriverPW.Elements.WebTables import WebTables


class elements():

    def __init__(self):
        self.TEXTBOX = TextBox()
        self.CHECKBOX = CheckBox()
        self.WEBTABLES = WebTables()

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        BROWSER.click(xpath_main['elements'])
