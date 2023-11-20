*** Settings ***
Documentation    Test mcc.py comands
Library             DataDriver    file=commands_test_data.json
Library             MCCRobotLibrary.py

Test Template       Test Command


*** Test Cases ***
Test Command    Authenticate    []    None    []    None


*** Keywords ***
Test Command
    [Documentation]    Test a given command agaist a assert command,
    ...    used as a test template for data driven tests
    [Arguments]
    ...    ${command_name}
    ...    ${parameters}
    ...    ${assert_command_name}
    ...    ${assert_command_parameters}
    ...    ${assert_output}
    Log To Console    Creating a new bot to test command ${command_name}
    Create Bot
    # Run the command
    Log To Console    Running the command ${command_name}
    Run Command    ${command_name}    ${parameters}
    # Assert the output is correct
    Log To Console    Disconnecting the bot
    Disconnect
