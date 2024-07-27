*** Settings ***
Library    ../keywords/bank_keywords.py

*** Test Cases ***
Deposit Money
    [Documentation]    Test depositing money
    Log To Console    Creating bank instance for deposit test
    Create Bank
    Log    Bank instance created
    Log To Console    Calculating final money for deposit
    Calculate Final Money    125    7    0.25    154.09
    Log    Final money calculated for deposit
