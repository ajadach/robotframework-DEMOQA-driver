import uuid
from SeleniumLibrary import SeleniumLibrary

SELENIUM = SeleniumLibrary()


def screenshot_on_fail(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            SELENIUM.capture_page_screenshot(filename=f'fail_screenshot-{uuid.uuid4()}.png')
            raise error
    return wrapper
