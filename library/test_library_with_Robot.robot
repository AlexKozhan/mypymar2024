*** Settings ***
Library           test_library.py

*** Test Cases ***
Reserve Book
    [Tags]    Positive
    ${result} =    test_reserve_book
    Should Be Equal    ${result}    Book 'Test Book' is reserved by user User1.

Take Book
    [Tags]    Positive
    ${result} =    test_take_book
    Should Be Equal    ${result}    Book 'Test Book' is taken by user User1.

Return Book
    [Tags]    Positive
    ${result} =    test_return_book
    Should Be Equal    ${result}    Book 'Test Book' is returned by user User1.

Take Reserved Book By Another User
    [Tags]    Negative
    ${result} =    test_take_reserved_book_by_another_user
    Should Be Equal    ${result}    Book 'Test Book' is already reserved by user User1.
