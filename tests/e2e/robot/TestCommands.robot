*** Settings ***
Library    DataDriver    file=commands_test_data.json
Library    MCCRobotLibrary.py
Test Template    Test Command

*** Test Cases ***
Test Command    Authenticate    {}    None     None

*** Keywords ***
Test Command
    [Arguments]    ${command_name}    ${parameters}    ${assert_command}    ${assert_output}
    Log To Console    Creating a new bot to test command ${command_name}
    Create Bot
    # Run the command
    Log To Console    Running the command ${command_name}
    Run command    ${command_name}    ${parameters}
    # Assert the output is correct
    Log To Console    Disconnecting the bot
    Disconnect
