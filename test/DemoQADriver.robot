*** Settings ***
Library          DemoQADriver

Test Setup    Run Keywords    DemoQADriver.Open Browser    AND    DemoQADriver.Navigate To Page
Test Teardown    DemoQADriver.Close Browser

Force Tags    sele

*** Variables ***

*** Test Cases ***

Elements: CheckBox
    DemoQADriver.Elements.Navigate To Page
    DemoQADriver.Elements.CheckBox.Navigate To Page
    DemoQADriver.Elements.CheckBox.Choose Parameters    Downloads   Notes
    ${result}    DemoQADriver.Elements.CheckBox.Read All Parameters
    ${expected_value}    Create List    notes    downloads    wordFile    excelFile
    ${result}    DemoQADriver.Elements.CheckBox.Read And Verify All Parameters    result    ${expected_value}

Elements: TextBox
    DemoQADriver.Elements.Navigate To Page
    DemoQADriver.Elements.TextBox.Navigate To Page
    DemoQADriver.Elements.TextBox.Choose Parameters    Full Name    Artur Ziolkowski
    ${result}    DemoQADriver.Elements.TextBox.Read All Parameters
    ${result}    DemoQADriver.Elements.TextBox.Read And Verify All Parameters    Name    Artur Ziolkowski

Elements: WebTables
    [Tags]    web
    DemoQADriver.Elements.Navigate To Page
    DemoQADriver.Elements.WebTables.Navigate To Page
    DemoQADriver.Elements.WebTables.Choose Parameters    First Name    Artur    Last Name    Ziolkowski    Email    temp@asd.com    Age    30    Salary    10000    Department    Poland
    ${result}    DemoQADriver.Elements.WebTables.Read All Parameters
    DemoQADriver.Elements.WebTables.Update Parameters    0    First Name    Artur
    DemoQADriver.Elements.WebTables.Delete    0


Forms:
    DemoQADriver.Forms.Navigate To Page

*** Keywords ***
