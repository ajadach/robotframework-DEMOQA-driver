import chromedriver_autoinstaller
from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver

chromedriver_autoinstaller.install()
SELENIUM = SeleniumLibrary()

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--user-data-dir=chrome-data")
index_or_alias = SELENIUM.create_webdriver("Chrome", options=opt)
SELENIUM.set_window_size(1920, 1080)
SELENIUM.set_selenium_speed(1)
SELENIUM.go_to('https://demoqa.com/')
