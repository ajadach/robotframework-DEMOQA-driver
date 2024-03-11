from drivers.DemoQA import SELENIUM


class elements():

    def navigate_to_page(self):
        SELENIUM.click_element('//*[@id="app"]/header/a/img')
        SELENIUM.click_element(f"//h5[contains(text(),'Elements')]")
