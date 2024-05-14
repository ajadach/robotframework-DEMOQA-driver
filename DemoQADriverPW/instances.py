import uuid
from Browser import Browser
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections
from robot.libraries.BuiltIn import RobotNotRunningError

BROWSER = Browser()
try:
    BUILT_IN = BuiltIn()
    COL = Collections()
except RobotNotRunningError:
    pass


def screenshot_on_fail(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            BROWSER.take_screenshot(filename=f'fail_screenshot-{uuid.uuid4()}.png')
            raise error
    return wrapper
