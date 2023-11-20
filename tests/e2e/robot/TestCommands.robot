*** Settings ***
Documentation       Test mcc.py comands

Library             DataDriver    file=commands_test_data.json
Library             MCCRobotLibrary.py

# Ensure that the bot gets disconnected cleanly, even if the test errors
Test Teardown       Ensure Clean Disconnect
Test Template       Test Command


*** Test Cases ***
# Dummy test, so that RobotFramework notices the data driven tests
Test Command    DummyCommandName    []    None    []    None


*** Keywords ***
Test Command
    [Documentation]    Test a given command agaist a assert command,
    ...    used as a test template for data driven tests
    [Arguments]
    ...    ${command_name}
    ...    ${parameters}
    ...    ${assert_command_name}
    ...    ${assert_command_parameters}
    ...    ${expected_assert_command_result}

    # Create the bot to test againt
    Log To Console    Test
    Create Bot

    # Run the command
    Log To Console    Running the command ${command_name}
    ${output}    Run Command    ${command_name}    ${parameters}
    Should Be True    ${output}[success]

    # Assert the output is correct
    Log To Console    Running assert Command ${assert_command_name}
    ${assert_output}    Run Command
    ...    ${assert_command_name}
    ...    ${assert_command_parameters}

    Should Be True    ${assert_output}[success]
    Should Be Equal
    ...    '${assert_output}[result]'
    ...    '${expected_assert_command_result}'

    # Disconnect the bot
    Log To Console    Disconnecting the bot
    Disconnect
