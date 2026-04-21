*** Settings ***
Library    DemoQADriverPackagePlaywright
Library    DemoQADriverPackagePlaywright.Elements


*** Test Cases ***
Example Test Case
    DemoQADriverPackagePlaywright.Open Browser
    DemoQADriverPackagePlaywright.Navigate To Page
    Sleep    1m
    DemoQADriverPackagePlaywright.Elements.Navigate To Page
