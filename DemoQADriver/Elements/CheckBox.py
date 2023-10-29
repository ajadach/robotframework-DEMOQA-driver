# -*- coding: utf-8 -*-
from DemoQADriver.instances import SELENIUM, screenshot_on_fail, BUILT_IN
from DemoQADriver.data.elements import MAIN_XPATH, CHECK_BOX
from robot.api.deco import keyword


class CheckBox():

    @screenshot_on_fail
    @keyword("Navigate To Page")
    def navigate_to_page(self):
        SELENIUM.click_element(MAIN_XPATH['check_box'])

    def _expand_all(self):
        SELENIUM.click_element(CHECK_BOX['BUTTON']['expand'])

    def _collapse_all(self):
        SELENIUM.click_element(CHECK_BOX['BUTTON']['collapse'])

    @screenshot_on_fail
    @keyword("Choose Parameters")
    def choose_parameters(self, *parameters):

        self._expand_all()
        for param in parameters:
            new_param_name = param.lower().replace(' ', '_')

            if new_param_name in CHECK_BOX['CHECK_BOX']:
                xpath = CHECK_BOX['CHECK_BOX'][new_param_name]
                SELENIUM.click_element(xpath)
            else:
                raise ValueError(f'Missing support for this paramter: {param}')

    @screenshot_on_fail
    @keyword("Read All Parameters")
    def read_all_parameters(self):

        output = {}
        for param, xpath in CHECK_BOX['READ_ALL_PARAMS'].items():
            output[param] = SELENIUM.get_text(xpath).split('\n')[1:]
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
