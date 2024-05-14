from DemoQADriverPW.demoqa_driver_pw import DemoQADriverPW
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError

from DemoQADriverPW.Elements.TextBox import TextBox
from DemoQADriverPW.Forms import forms
from DemoQADriverPW.Elements import elements
import_text_box = 'Elements.TextBox'
from DemoQADriverPW.Elements.CheckBox import CheckBox
import_check_box = 'Elements.CheckBox'
from DemoQADriverPW.Elements.WebTables import WebTables
import_web_tables = 'Elements.WebTables'

TEXTBOX = TextBox()

__all__ = (
    'forms',
    'elements',
    import_text_box,
    import_check_box,
    import_web_tables,

)

try:
    for name in __all__:
        RFW = BuiltIn()
        RFW.import_library(f'DemoQADriverPW.{name}')
except RobotNotRunningError:
    pass
