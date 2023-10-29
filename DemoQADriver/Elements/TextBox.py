# -*- coding: utf-8 -*-
from DemoQADriver.instances import SELENIUM, screenshot_on_fail, BUILT_IN
from DemoQADriver.data.elements import MAIN_XPATH, TEXT_BOX
from robot.api.deco import keyword


class TextBox():

    @screenshot_on_fail
    @keyword("Navigate To Text Box")
    def navigate_to_page(self):
        SELENIUM.click_element(MAIN_XPATH['text_box'])

    @screenshot_on_fail
    @keyword("Choose Parameters")
    def choose_parameters(self, *params_and_values):
        parameters = params_and_values[::2]
        values = params_and_values[1::2]
        if not parameters or not values:
            raise ValueError("Missing parameters or values.")

        for param, value in zip(parameters, values):
            new_param_name = param.lower().replace(' ', '_')

            if new_param_name in TEXT_BOX['INPUT']:
                xpath = TEXT_BOX['INPUT'][new_param_name]
                SELENIUM.input_text(xpath, value)
            else:
                raise ValueError(f"Missing support for this param: {param}")
        SELENIUM.click_element(TEXT_BOX['BUTTON']['submit'])

    @screenshot_on_fail
    @keyword("Read All Parameters")
    def read_all_parameters(self):
        output = {}
        for param, xpath in TEXT_BOX['READ_ALL_PARAMS'].items():
            rows = SELENIUM.get_text(xpath).split('\n')
            for row in rows:
                row_param, row_val = row.split(':')
                output[row_param] = row_val
        return output

    @screenshot_on_fail
    @keyword("Read And Verify All Parameters")
    def read_and_verify_all_parameters(self, *expected_parameters_values):
        parameters = expected_parameters_values[::2]
        expected_values = expected_parameters_values[1::2]
        if not parameters or not expected_values:
            raise ValueError("Missing parameters or values.")

        output = self.read_all_parameters()
        for parameter, value in zip(parameters, expected_values):
            BUILT_IN.should_be_equal(output[parameter], value)
        return output
