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
SELENIUM.input_text('//*[@id="firstName"]', "Artur")
SELENIUM.input_text('//*[@id="lastName"]', "Ziolkowski")
# SELENIUM.select_checkbox('//*[@id="gender-radio-1"]')
SELENIUM.click_element('//*[@for="gender-radio-1"]')
SELENIUM.input_text('//*[@id="userNumber"]', 1114445555)
SELENIUM.click_button('//*[@id="submit"]')


inner_html = SELENIUM.get_element_attribute('//*[@class="table-responsive"]/table/tbody', "innerHTML")
root = lxml.html.fromstring(inner_html)

rows = root.xpath(".//tr")

output = {}
for row in rows:
    tds = row.xpath(".//td")
    import pdb
    pdb.set_trace()
    output[tds[0].text_content()] = tds[1].text_content()

SELENIUM.click_button('//*[@id="closeLargeModal"]')


print(output)





import time
time.sleep(15)

SELENIUM.close_browser()