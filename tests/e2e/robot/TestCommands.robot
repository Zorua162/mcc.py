*** Settings ***
Documentation       Test mcc.py comands

Library             Collections
Library             DataDriver    file=commands_test_data.json
Library             MCCRobotLibrary.py

# Suite Setup         Create Bot
# Suite Teardown      Disconnect
Test Teardown    Disconnect
Test Template       Test Command


*** Test Cases ***
# Empty test, so that RobotFramework notices the data driven tests
Test Command    true    {}    {}    {}


*** Keywords ***
Test Command
    [Documentation]    Test a given command agaist a assert command,
    ...    used as a test template for data driven tests
    [Arguments]
    ...    ${skip_test}
    ...    ${setup_data}
    ...    ${command_data}
    ...    ${assert_data}
    Skip If     ${skip_test}
    Create Bot

    Connect

    # Arrange
    Setup Command    ${setup_data}

    # Act
    Run Test Command    ${command_data}

    # Assert
    Run Assert Command    ${assert_data}

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
        Should Not Be Equal    ${setup_output}    ${None}
        Should Be True    ${setup_output}[success]
        Should Be Equal
        ...    '${setup_output}[result]'
        ...    '${command}[expected_command_result]'
    END

Run Test Command
    [Documentation]    Run the given test command
    [Arguments]    ${command_data}
    # Run the command
    ${command_name}    Get From Dictionary    ${command_data}    command_name
    Log To Console    Testing the command ${command_name}
    ${output}    Run Command    ${command_name}    ${command_data}[command_parameters]
    Should Not Be Equal     ${output}    ${None}
    Should Be True    ${output}[success]
    Should Be Equal
    ...    '${output}[result]'
    ...    '${command_data}[expected_command_result]'

Run Assert Command
    [Documentation]    Run the given assert command
    [Arguments]    ${assert_data}

    ${command_name}    Get From Dictionary    ${assert_data}    command_name
    # Assert the output is correct
    Log To Console    Running assert Command ${command_name}
    ${output}    Run Command    ${command_name}    ${assert_data}[command_parameters]

    Log To Console    Assert command output was ${output}
    Log To Console    Asserting against output
    Should Be True    ${output}[success]
    Should Be Equal    '${output}[result]'    '${assert_data}[expected_command_result]'
