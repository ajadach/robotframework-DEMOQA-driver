*** Settings ***
Library          DemoQADriverPW

Test Setup    Run Keywords    DemoQADriverPW.Open Browser    AND    DemoQADriverPW.Navigate To Page
Test Teardown    DemoQADriverPW.Close Browser

Force Tags    PW

*** Variables ***

*** Test Cases ***

Elements: CheckBox
    DemoQADriverPW.Elements.Navigate To Page
    DemoQADriverPW.Elements.CheckBox.Navigate To Page
    DemoQADriverPW.Elements.CheckBox.Choose Parameters    Downloads   Notes
    ${result}    DemoQADriverPW.Elements.CheckBox.Read All Parameters
    ${expected_value}    Create List    notes    downloads    wordFile    excelFile
    ${result}    DemoQADriverPW.Elements.CheckBox.Read And Verify All Parameters    result    ${expected_value}

Elements: TextBox
    DemoQADriverPW.Elements.Navigate To Page
    DemoQADriverPW.Elements.TextBox.Navigate To Page
    DemoQADriverPW.Elements.TextBox.Choose Parameters    Full Name    Artur Ziolkowski
    ${result}    DemoQADriverPW.Elements.TextBox.Read All Parameters
    ${result}    DemoQADriverPW.Elements.TextBox.Read And Verify All Parameters    Name    Artur Ziolkowski

Elements: WebTables
    DemoQADriverPW.Elements.Navigate To Page
    DemoQADriverPW.Elements.WebTables.Navigate To Page
    DemoQADriverPW.Elements.WebTables.Choose Parameters    First Name    Artur    Last Name    Ziolkowski    Email    temp@asd.com    Age    30    Salary    10000    Department    Poland
    ${result}    DemoQADriverPW.Elements.WebTables.Read All Parameters
    DemoQADriverPW.Elements.WebTables.Update Parameters    0    First Name    Artur
    DemoQADriverPW.Elements.WebTables.Delete    0


Forms:
    DemoQADriverPW.Forms.Navigate To Page

*** Keywords ***
