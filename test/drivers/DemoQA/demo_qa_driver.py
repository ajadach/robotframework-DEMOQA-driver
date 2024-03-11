from selenium import webdriver
from . import SELENIUM
from drivers.DemoQA.Elements.elements import elements
from drivers.DemoQA.Elements.text_box import text_box


class demo_qa_driver():

    def __init__(self):
        self.SELENIUM = SELENIUM
        self.ELEMENTS = elements()
        self.TEXT_BOX = text_box()

    def open_browser(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        opt.add_argument("--ignore-certificate-errors")
        self.SELENIUM.create_webdriver("Chrome", options=opt)
        self.SELENIUM.set_selenium_speed(1)
        self.SELENIUM.maximize_browser_window()

    def navigate_to_page(self):
        self.SELENIUM.go_to('https://demoqa.com/')
        try:
            self.SELENIUM.click_element("//p[contains(text(), 'Consent')]")
        except Exception:
            pass

    def navigate_to_menu(self, value):
        if value not in ["Elements", "Forms", "Alerts, Frame & Windows"]:
            raise ValueError("Wrong value for menu")
        else:
            self.SELENIUM.click_element(f"//h5[contains(text(),'{value}')]")



    def close_browser(self):
        self.SELENIUM.close_browser()