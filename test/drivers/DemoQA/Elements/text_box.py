from drivers.DemoQA import SELENIUM
from drivers.DemoQA.Elements.elements import elements

INPUT= {
    'full_name': '//*[@id="userName"]',
    'email': '//*[@id="userEmail"]',
    'current_address': '//*[@id="currentAddress"]',
    'permanent_address': '//*[@id="permanentAddress"]'
}

class text_box(elements):

    def navigate_to_page(self):
        elements.navigate_to_page(self)
        SELENIUM.click_element("//span[contains(text(),'Text Box')]")

    def choose_parameters(self, *params_and_values):
        parameters = params_and_values[::2]
        values = params_and_values[1::2]
        for param, value in zip(parameters, values):
            new_param_name = param.lower().replace(' ', '_')

            if new_param_name in INPUT:
                xpath = INPUT[new_param_name]
                SELENIUM.input_text(xpath, value)
            else:
                raise ValueError(f"Missing support for this param: {param}")
        SELENIUM.click_element('//*[@id="submit"]')


    def read_all_params(self, **expected_data):
        ids = ["name", "email", "currentAddress", "permanentAddress"]
        for id in ids:
            try:
                val = SELENIUM.get_text(f'//*[@id="{id}"]').split(':')[-1]
            except Exception:
                pass
