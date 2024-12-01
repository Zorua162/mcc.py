*** Settings ***
Documentation       Test misc commands in mcc.py as per tested_commands.md

Library             DataDriver    file=entities_commands_test_data.json
Library             MCCRobotLibrary.py
Resource            TestCommands.resource

Test Teardown       Disconnect
Test Template       Test Command Keyword


*** Test Cases ***
# Empty test, so that RobotFramework notices the data driven tests
Test Command Keyword    true    {}


*** Keywords ***
Test Command Keyword
    [Documentation]    Wrapper so that Test Template can use the Test Comand keyword
    ...    from the TestCommands resource file
    [Arguments]    ${skip_test}    ${command_data}
    Test Command    ${skip_test}    ${command_data}
