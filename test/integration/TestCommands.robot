*** Settings ***
Documentation        A test suite for MCC.py working
Library    MCCRobotLibrary.py

*** Test Cases ***
Connection To MCC Works Without Authentication
    Create Bot
