*** Settings ***
Library    ../keywords/library_keywords.py

*** Test Cases ***
Reserve Book
    [Documentation]    Test reserving a book
    Log To Console    Creating user and book for reservation test
    Create User    Alex
    Create Book    White Fang    Jack London    100    1234567890
    Log    User 'Alex' and book 'White Fang' created
    Log To Console    Reserving the book 'White Fang' for user 'Alex'
    Reserve Book   Alex    White Fang
    Log    Book 'White Fang' reserved by user 'Alex'
