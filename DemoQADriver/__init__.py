from DemoQADriver.demoqa_driver import DemoQADriver
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError

from DemoQADriver.Forms import forms
from DemoQADriver.Elements import elements
from DemoQADriver.Elements.TextBox import TextBox
import_text_box = 'Elements.TextBox'
from DemoQADriver.Elements.CheckBox import CheckBox
import_check_box = 'Elements.CheckBox'
from DemoQADriver.Elements.WebTables import WebTables
import_web_tables = 'Elements.WebTables'

__all__ = (
    'forms',
    'elements',
    import_text_box,
    import_check_box,
    import_web_tables

)

try:
    for name in __all__:
        RFW = BuiltIn()
        RFW.import_library(f'DemoQADriver.{name}')
except RobotNotRunningError:
    pass
