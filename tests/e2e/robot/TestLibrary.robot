*** Settings ***
Documentation        A test suite for MCC.py working
Library    MCCRobotLibrary.py

*** Test Cases ***
Connection To MCC Works
    Skip
    Create Bot

    Disconnect
