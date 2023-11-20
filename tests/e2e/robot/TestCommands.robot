*** Settings ***
Documentation       Test mcc.py comands

Library             Collections
Library             DataDriver    file=commands_test_data.json
Library             MCCRobotLibrary.py

# Ensure that the bot gets disconnected cleanly, even if the test errors
# Test Teardown       Ensure Clean Disconnect
Test Template       Test Command


*** Test Cases ***
# Empty test, so that RobotFramework notices the data driven tests
Test Command    {}    {}    {}


*** Keywords ***
Test Command
    [Documentation]    Test a given command agaist a assert command,
    ...    used as a test template for data driven tests
    [Arguments]
    ...    ${setup_data}
    ...    ${command_data}
    ...    ${assert_data}

    # Create the bot to test againt
    Log To Console    Creating the Bot
    Create Bot

    # Arrange
    Setup Command    ${setup_data}

    # Act
    Run Test Command    ${command_data}

    # Assert
    Run Assert Command    ${assert_data}

    # Disconnect the bot
    Log To Console    Disconnecting the bot
    Disconnect

Setup Command
    [Documentation]    Run the required setup command
    [Arguments]    ${setup_data}
    # Run setup command
    FOR    ${command}    IN    @{setup_data}[command_list]
        ${command_name}    Get From Dictionary    ${command}    command_name
        Log To Console    Running setup command ${command_name}
        ${setup_output}    Run Command
        ...    ${command_name}
        ...    ${command}[command_parameters]
        Should Be True    ${setup_output}[success]
    END

Run Test Command
    [Documentation]    Run the given test command
    [Arguments]    ${command_data}
    # Run the command
    ${command_name}    Get From Dictionary    ${command_data}    command_name
    Log To Console    Running the command ${command_name}
    ${output}    Run Command    ${command_name}    ${command_data}[command_parameters]
    Should Be True    ${output}[success]

Run Assert Command
    [Documentation]    Run the given assert command
    [Arguments]    ${assert_data}

    ${command_name}    Get From Dictionary    ${assert_data}    command_name
    # Assert the output is correct
    Log To Console    Running assert Command ${command_name}
    ${output}    Run Command    ${command_name}    ${assert_data}[command_parameters]

    Log To Console
    ...    Checking against output of the assert command which was ${output} for
    ...    expected result
    Should Be True    ${output}[success]
    Should Be Equal    '${output}[result]'    '${assert_data}[expected_command_result]'
