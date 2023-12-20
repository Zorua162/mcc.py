*** Settings ***
Documentation       Test mcc.py comands

Library             Collections
Library             OperatingSystem
Library             DataDriver    file=commands_test_data.json
Library             MCCRobotLibrary.py

# Suite Setup    Create Bot
# Suite Teardown    Disconnect
Test Teardown       Disconnect
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
    Skip If    ${skip_test}
    Log To Console    Creating Bot
    Create Bot

    Log To Console    Connecting to bot
    Connect

    Log To Console    Running commands
    Run Commands    ${command_data}

    Log To Console    Test finished

Run Commands
    [Documentation]    Run the test commands
    [Arguments]    ${commands_data}
    # Run command
    FOR    ${command}    IN    @{commands_data}[command_list]
        ${command_name}    Get From Dictionary    ${command}    command_name
        Log To Console    Running command ${command_name}
        ${command_output}    Run Command
        ...    ${command_name}
        ...    ${command}[command_parameters]
        Should Not Be Equal    ${command_output}    ${None}
        Should Be True    ${command_output}[success]
        IF    ${command}[expected_is_keys]
            Check All Keys In Dict
            ...    ${command_output}[result]
            ...    ${command}[expected_command_result]
        ELSE
            Should Be Equal
            ...    '${command_output}[result]'
            ...    '${command}[expected_command_result]'
        END
    END

Check All Keys In Dict
    [Documentation]    Loop throgh each item in "expected_items" and check they are in
    ...    result
    [Arguments]    ${result}    ${expected_items}
    FOR    ${expected_item_key}    ${expected_item_value}    IN    &{expected_items}
        Log    ${expected_item_key}
        Should Be Equal    ${result}[${expected_item_key}]    ${expected_item_value}
    END
