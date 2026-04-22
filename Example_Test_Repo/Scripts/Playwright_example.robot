*** Settings ***
Library    DemoQADriverPackagePlaywright
Library    DemoQADriverPackagePlaywright.Elements


*** Test Cases ***
Example Test Case
    DemoQADriverPackagePlaywright.Open Browser
    DemoQADriverPackagePlaywright.Navigate To Page
    DemoQADriverPackagePlaywright.Elements.Navigate To Page
