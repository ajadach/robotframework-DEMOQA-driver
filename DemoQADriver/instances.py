import uuid
from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections

SELENIUM = SeleniumLibrary()
BUILT_IN = BuiltIn()
COL = Collections()


def screenshot_on_fail(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            SELENIUM.capture_page_screenshot(filename=f'fail_screenshot-{uuid.uuid4()}.png')
            raise error
    return wrapper
