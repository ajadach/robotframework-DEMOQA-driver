# -*- coding: utf-8 -*-
# import chromedriver_autoinstaller

# from selenium import webdriver
from .instances import BROWSER, screenshot_on_fail
from robot.api.deco import keyword


class DemoQADriverPW():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'

    # def __init__(self, install=True):
    #     self.path_chromedriver = chromedriver_autoinstaller.install() if install else False

    @keyword("Open Browser")
    def open_browser(self, alias=None, headless=False):
        """ Open Browser to the Demo QA

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | alias | alias for session name | first_session |
        | headless | boolen True or Flase | False |

        *Return*
        | index_or_alias | index of session or alias |
        """
        BROWSER.open_browser('https://demoqa.com/')
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument("--start-maximized")
    #     opt.add_argument("--ignore-certificate-errors")
    #
    #     if headless:
    #         opt.add_argument("headless")
    #
    #     index_or_alias = SELENIUM.create_webdriver("Chrome", alias=alias, options=opt)
    #     SELENIUM.set_window_size(1920, 1080)
    #     SELENIUM.set_selenium_speed(1)
    #     SELENIUM.maximize_browser_window()
    #     return index_or_alias
    #
    # @screenshot_on_fail
    # @keyword("Navigate To Page")
    # def navigate_to_page(self):
    #     SELENIUM.go_to('https://demoqa.com/')
    #     try:
    #         SELENIUM.click_element("//p[contains(text(), 'Consent')]")
    #     except Exception:
    #         pass
    #
    # @keyword("Close Browser")
    # def close_browser(self):
    #     SELENIUM.close_browser()
