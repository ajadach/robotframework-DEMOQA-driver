*** Settings ***
Library    DemoQADriverPackagePlaywright
Library    DemoQADriverPackagePlaywright.Elements
Library    DemoQADriverPackagePlaywright.Elements.TextBox


*** Test Cases ***
Example Test Case
    DemoQADriverPackagePlaywright.Open Browser
    DemoQADriverPackagePlaywright.Navigate To Page
    DemoQADriverPackagePlaywright.Elements.Navigate To Page
    DemoQADriverPackagePlaywright.Elements.TextBox.Navigate To Page
    DemoQADriverPackagePlaywright.Close Browser
