from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver

# open browser
SELENIUM = SeleniumLibrary()
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

# test
SELENIUM.click_element("//h5[contains(text(),'Elements')]")
SELENIUM.click_element("//span[contains(text(),'Text Box')]")
SELENIUM.input_text('//*[@id="userName"]', "Artur Ziolkowski")
SELENIUM.click_button('//*[@id="submit"]')

# teardown
SELENIUM.close_browser()


