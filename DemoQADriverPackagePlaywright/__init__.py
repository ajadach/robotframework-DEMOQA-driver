from DemoQADriverPackagePlaywright.demoqa_driver_package import DemoQADriverPackagePlaywright
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError

from DemoQADriverPackagePlaywright.Forms import forms
from DemoQADriverPackagePlaywright.Elements import elements
from DemoQADriverPackagePlaywright.Elements.TextBox import TextBox
import_text_box = 'Elements.TextBox'
from DemoQADriverPackagePlaywright.Elements.CheckBox import CheckBox
import_check_box = 'Elements.CheckBox'
from DemoQADriverPackagePlaywright.Elements.WebTables import WebTables
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
        RFW.import_library(f'DemoQADriverPackagePlaywright.{name}')
except RobotNotRunningError:
    pass
