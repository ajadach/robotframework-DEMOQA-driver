from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver

SELENIUM = SeleniumLibrary()

def open_browser_and_navi_to_page():
    """Open Browser, navigate to https://demoqa.com/ and accept cookies."""
    # open browser
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    opt.add_argument("--ignore-certificate-errors")

    index_or_alias = SELENIUM.create_webdriver("Chrome", options=opt)
    SELENIUM.set_window_size(1920, 1080)
    SELENIUM.set_selenium_speed(1)
    SELENIUM.maximize_browser_window()

    # navi
    SELENIUM.go_to('https://demoqa.com/')
    SELENIUM.click_element("//p[contains(text(), 'Consent')]")

def navigate_to_elements():
    """Navigate to elements from main page."""
    SELENIUM.click_element("//h5[contains(text(),'Elements')]")

def navigate_to_text_box():
    """Navigate to text box under Elements subpage."""
    SELENIUM.click_element("//span[contains(text(),'Text Box')]")

def input_user_name(name_value):
    """Input user name into Text Box."""
    SELENIUM.input_text('//*[@id="userName"]', name_value)

def teardown():
    """Cleanup after test"""
    SELENIUM.close_browser()


open_browser_and_navi_to_page()
navigate_to_elements()
navigate_to_text_box()
input_user_name("Artur")
teardown()
