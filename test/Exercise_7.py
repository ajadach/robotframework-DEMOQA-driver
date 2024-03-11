from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver
import lxml.html

SELENIUM = SeleniumLibrary()
# opt = webdriver.ChromeOptions()
#
#
# opt.add_argument("--start-maximized")
# opt.add_argument("--ignore-certificate-errors")
#
# index_or_alias = SELENIUM.create_webdriver("Chrome", options=opt)
#
# SELENIUM.set_window_size(1920, 1080)
# SELENIUM.set_selenium_speed(1)
#
# SELENIUM.maximize_browser_window()
# SELENIUM.go_to('https://demoqa.com/')
# SELENIUM.click_element("//p[contains(text(), 'Consent')]")
#
#
# SELENIUM.click_element("//h5[contains(text(),'Forms')]")
# SELENIUM.click_element("//span[contains(text(),'Practice Form')]")
# SELENIUM.input_text('//*[@id="firstName"]', "Artur")
# SELENIUM.input_text('//*[@id="lastName"]', "Ziolkowski")
# # SELENIUM.select_checkbox('//*[@id="gender-radio-1"]')
# SELENIUM.click_element('//*[@for="gender-radio-1"]')
# SELENIUM.input_text('//*[@id="userNumber"]', 1114445555)
# SELENIUM.click_button('//*[@id="submit"]')
#
# SELENIUM.close_browser()

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
def navigate_to_forms():
    """Navigate to Forms from main page."""
    SELENIUM.click_element("//h5[contains(text(),'Forms')]")
def navigate_to_practice_form():
    """Navigate to Practice Form under Forms subpage."""
    SELENIUM.click_element("//span[contains(text(),'Practice Form')]")
def input_first_name(name_value):
    """Input First Name into Practice Form."""
    SELENIUM.input_text('//*[@id="firstName"]', name_value)
def input_last_name(name_value):
    """Input Last Name into Practice Form."""
    SELENIUM.input_text('//*[@id="lastName"]', name_value)
def input_phone_number(number):
    """Input Phone Numbr into Practice Form."""
    SELENIUM.input_text('//*[@id="userNumber"]', number)
def select_gender(value):
    """ 1 = """
    if value == "Male":
        val = 1
    SELENIUM.click_element(f'//*[@for="gender-radio-{val}"]')

def click_submit_button():
    SELENIUM.click_button('//*[@id="submit"]')
def teardown():
    """Cleanup after test"""
    SELENIUM.close_browser()

open_browser_and_navi_to_page()
navigate_to_forms()
input_first_name()
input_last_name()
input_phone_number()
select_gender()
click_submit_button()
teardown()


def full_fields(**kwargs):
    if type == "input":
        SELENIUM.input_text()
    else type == "radio":
        SELENIUM.click_element()


MAPS= {
    "Male": '//*[@id="gender-radio-1"]',
    "VALu z PAGE": "NA xpath"

}

id: value
id: {value: STRING, type: SELECET/INPUT}


full_fields({"firstName": {"value":"Artur", "type":"input"},
             "lastName": {"value":"Ziolkows", "type":"input"},
             "Gender": {"type": "select", "value": "Male"})

