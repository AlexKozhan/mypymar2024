*** Settings ***
Library     ../keywords/bank_keywords.py

*** Variables ***
${INITIAL_MONEY}    125
${DURATION}         7
${EXPECTED_FINAL}   328.75  # Example value, calculate based on the formula

*** Test Cases ***
Deposit Money
    ${bank}=    Create Bank
    ${final_amount}=    Deposit Money    ${bank}    ${INITIAL_MONEY}    ${DURATION}
    Should Be Equal    ${final_amount}    ${EXPECTED_FINAL}
