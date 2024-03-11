from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver
import lxml.html

SELENIUM = SeleniumLibrary()
opt = webdriver.ChromeOptions()


opt.add_argument("--start-maximized")
opt.add_argument("--ignore-certificate-errors")

index_or_alias = SELENIUM.create_webdriver("Chrome", options=opt)

SELENIUM.set_window_size(1920, 1080)
SELENIUM.set_selenium_speed(1)


SELENIUM.maximize_browser_window()
SELENIUM.go_to('https://demoqa.com/')
SELENIUM.click_element("//p[contains(text(), 'Consent')]")


SELENIUM.click_element("//h5[contains(text(),'Forms')]")
SELENIUM.click_element("//span[contains(text(),'Practice Form')]")


inner_html = SELENIUM.get_element_attribute('//*[@id="userForm"]', "innerHTML")
root = lxml.html.fromstring(inner_html)
rows = root.xpath(".//div")

forums = []

for row in rows:
    output = {}
    colums = row.xpath(".//div")
    for colum in colums:
        labal = colum.xpath(".//label")
        inputs = colum.xpath(".//input")
        if labal:
            output["label_value"] = labal[0].text_content()
        else:
            for inp in inputs:
                output[inp.attrib["id"]] = inp.attrib
    forums.append(output)

print(forums)

if forums[0]['label_name'] != 'Name':
    raise ValueError("wrong label name")


name = SELENIUM.get_text('//*[@id="userName-label"]')
if name != 'Name':
    raise ValueError("wrong label name")

name = SELENIUM.get_text('//*[@id="userName-label"]')
if name != 'Name':
    raise ValueError("wrong label name")

val = SELENIUM.get_element_attribute('//*[@id="firstName"]', 'placeholder')
print('--------------')
print(val)

import time
time.sleep(15)

SELENIUM.close_browser()
