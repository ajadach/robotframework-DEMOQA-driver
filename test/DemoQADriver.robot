*** Settings ***
Library          DemoQADriver

*** Variables ***

*** Test Cases ***
Library Instance
    [Documentation]    Get the library instance.
    ...                This will prove that the library could be imported
    ...                w/o problems.
    ${instance}=    Get Library Instance    DemoQADriver
    Should Be True    ${instance}

test2
    DemoQADriver.Example

*** Keywords ***
