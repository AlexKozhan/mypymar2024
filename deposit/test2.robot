*** Settings ***
Library           test_deposit.py

*** Test Cases ***
Deposit Positive
    [Tags]    Positive
    ${result} =    test_deposit_positive
    Should Be Equal As Numbers    ${result}    250.99

Deposit Zero Money
    [Tags]    Negative
    ${result} =    test_deposit_zero_money
    Should Be Equal As Numbers    ${result}    0.00

Deposit Zero Duration
    [Tags]    Negative
    ${result} =    test_deposit_zero_duration
    Should Be Equal As Numbers    ${result}    125.00

Deposit Negative Money
    [Tags]    Negative
    ${result} =    test_deposit_negative_money
    Should Be Equal As Numbers    ${result}    -250.99

Deposit Negative Duration
    [Tags]    Negative
    ${result} =    test_deposit_negative_duration
    Should Be Equal As Numbers    ${result}    62.25
