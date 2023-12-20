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
Test Command    true    {}


*** Keywords ***
Test Command
    [Documentation]    Test a given command agaist a assert command,
    ...    used as a test template for data driven tests
    [Arguments]
    ...    ${skip_test}
    ...    ${command_data}
    Skip If     ${skip_test}
    Create Bot

    Connect

    Run Commands    ${command_data}

Run Commands
    [Documentation]    Run the test commands
    [Arguments]    ${commands_data}
    # Run setup command
    FOR    ${command}    IN    @{commands_data}[command_list]
        ${command_name}    Get From Dictionary    ${command}    command_name
        Log To Console    Running setup command ${command_name}
        ${command_output}    Run Command
        ...    ${command_name}
        ...    ${command}[command_parameters]
        Should Not Be Equal    ${command_output}    ${None}
        Should Be True    ${command_output}[success]
        Should Be Equal
        ...    '${command_output}[result]'
        ...    '${command}[expected_command_result]'
    END
