from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver

# open browser
SELENIUM = SeleniumLibrary()
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("--ignore-certificate-errors")

SELENIUM.create_webdriver("Chrome", options=opt)
SELENIUM.go_to("https://demoqa.com/")
SELENIUM.set_selenium_speed(1)
SELENIUM.maximize_browser_window()

# accpet cookies
SELENIUM.click_element("//p[contains(text(), 'Consent')]")


SELENIUM.close_browser()
