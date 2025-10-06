from DemoQADriverPackage.demoqa_driver_package import DemoQADriverPackage
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError

from DemoQADriverPackage.Forms import forms
from DemoQADriverPackage.Elements import elements
from DemoQADriverPackage.Elements.TextBox import TextBox
import_text_box = 'Elements.TextBox'
from DemoQADriverPackage.Elements.CheckBox import CheckBox
import_check_box = 'Elements.CheckBox'
from DemoQADriverPackage.Elements.WebTables import WebTables
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
        RFW.import_library(f'DemoQADriverPackage.{name}')
except RobotNotRunningError:
    pass
