*** Settings ***
Library    ../keywords/library_keywords.py

*** Variables ***
${BOOK_TITLE}    White Fang
${BOOK_AUTHOR}   Jack London
${BOOK_PAGES}    100
${BOOK_ISBN}     1234567890
${USER_NAME}     Alex

*** Test Cases ***
Reserve Book
    ${user}=    Create User    ${USER_NAME}
    ${book}=    Create Book    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Reserve Book    ${user}    ${book}
    ${is_reserved}=    Is Book Reserved    ${book}
    Should Be True    ${is_reserved}

Take Book
    ${user}=    Create User    ${USER_NAME}
    ${book}=    Create Book    ${BOOK_TITLE}    ${BOOK_AUTHOR}    ${BOOK_PAGES}    ${BOOK_ISBN}
    Reserve Book    ${user}    ${book}
    Take Book    ${user}    ${book}
    ${is_taken}=    Is Book Taken    ${book}
    Should Be True    ${is_taken}
