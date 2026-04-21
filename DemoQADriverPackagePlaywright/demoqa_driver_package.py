# -*- coding: utf-8 -*-
import chromedriver_autoinstaller

from .instances import BROWSER, screenshot_on_fail
from robot.api.deco import keyword


class DemoQADriverPackagePlaywright():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'

    def __init__(self, install=True):
        self.path_chromedriver = chromedriver_autoinstaller.install() if install else False

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
        opt = webdriver.ChromeOptions()
        # opt.add_argument("--start-maximized")
        opt.add_argument("--ignore-certificate-errors")

        if headless:
            opt.add_argument("headless")

        index_or_alias = BROWSER.create_webdriver("Chrome", alias=alias, options=opt)
        return index_or_alias

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self, url='https://demoqa.com/'):
        BROWSER.go_to(url)
        try:
            BROWSER.click_element("//p[contains(text(), 'Consent')]")
        except Exception:
            pass

    @keyword("Close Browser")
    def close_browser(self):
        BROWSER.close_browser()
