from DemoQADriver import DemoQADriver
DEMO_QA = DemoQADriver(install=False)

DEMO_QA.open_browser()
DEMO_QA.navigate_to_page()

from DemoQADriver.Elements import elements
ELEMENTS = elements()
#
# ELEMENTS.navigate_to_page()
# ELEMENTS.TEXTBOX.navigate_to_page()
# ELEMENTS.TEXTBOX.choose_parameters("Full Name", "Artur Ziolkowski",
#                                    "Email", "temp_email@temp.com",
#                                    "Current Address", "Temp Address Street")
#
# print(ELEMENTS.TEXTBOX.read_all_parameters())


ELEMENTS.navigate_to_page()
ELEMENTS.WEBTABLES.navigate_to_page()
# ELEMENTS.WEBTABLES.update_parameters(1,
#                                      "First Name", "Artur",
#                                      "Last Name", "Ziolkowski",
#                                      "Email", "temp@asd.com",
#                                      "Age", "30",
#                                      "Salary", "10000",
#                                      "Department", "Poland")

ELEMENTS.navigate_to_page()
ELEMENTS.WEBTABLES.navigate_to_page()
ELEMENTS.WEBTABLES.delete(1)


import time
time.sleep(60)