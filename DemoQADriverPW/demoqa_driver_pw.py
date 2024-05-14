# -*- coding: utf-8 -*-
# import chromedriver_autoinstaller

# from BROWSER import webdriver
from .instances import BROWSER, screenshot_on_fail
from robot.api.deco import keyword


class DemoQADriverPW():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'

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

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        BROWSER.go_to('https://demoqa.com/')
        try:
            BROWSER.click("//p[contains(text(), 'Consent')]")
        except Exception:
            pass

    @keyword("Close Browser")
    def close_browser(self):
        BROWSER.close_browser()