*** Settings ***
Documentation       Resources for testing mcc.py comands

Library             Collections
Library             OperatingSystem
Library             MCCRobotLibrary.py
Library             matcher_utils.py


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
        IF    "${command}[command_name]" == "Sleep"
            Log To Console    Sleeping for ${command}[command_parameters] seconds
            Sleep    ${command}[command_parameters]
            CONTINUE
        END
        ${command_name}    Get From Dictionary    ${command}    command_name
        Log To Console    Running command ${command_name}
        ${command_output}    Run Command
        ...    ${command_name}
        ...    ${command}[command_parameters]
        Should Not Be Equal    ${command_output}    ${None}
        Should Be True    ${command_output}[success]
        Handle Assert    ${command}    ${command_output}
    END

Handle Assert
    [Documentation]    Handles the assertation on the command output
    [Arguments]    ${command}    ${command_output}
    IF    "${command}[expected_type]" == "keys"
        Check All Keys In Dict
        ...    ${command_output}[result]
        ...    ${command}[expected_command_result]
    ELSE IF    "${command}[expected_type]" == "type_match_keys"
        Check Type Match Keys
        ...    ${command_output}[result]
        ...    ${command}[expected_command_result]
    ELSE IF    "${command}[expected_type]" == "type_match"
        Check Type Match
        ...    ${command_output}[result]
        ...    ${command}[expected_command_result]
    ELSE IF    "${command}[expected_type]" == "contains"
        Should Contain
        ...    ${command_output}[result]
        ...    ${command}[expected_command_result]
    ELSE IF    "${command}[expected_type]" == "list_contains"
        List Contains
        ...    ${command_output}[result]
        ...    ${command}[expected_command_result]
    ELSE
        Should Be Equal
        ...    '${command_output}[result]'
        ...    '${command}[expected_command_result]'
    END

Check All Keys In Dict
    [Documentation]    Loop throgh each item in "expected_items" and check they are in
    ...    result
    [Arguments]    ${result}    ${expected_items}
    FOR    ${expected_item_key}    ${expected_item_value}    IN    &{expected_items}
        Log    ${expected_item_key}
        Should Be Equal    ${result}[${expected_item_key}]    ${expected_item_value}
    END

Check Type Match Keys
    [Documentation]    Check the type given for all the given keys matches their values
    [Arguments]    ${result}    ${expected_items}
    FOR    ${expected_item_key}    ${expected_value_type}    IN    &{expected_items}
        Log    Checking type of key ${expected_item_key}
        Check Type    ${result}[${expected_item_key}]    ${expected_value_type}
    END

Check Type Match
    [Documentation]    Check the type given for all the given keys matches their values
    [Arguments]    ${result}    ${expected_type}
    Log    Checking type of key ${expected_type}
    Check Type    ${result}    ${expected_type}
