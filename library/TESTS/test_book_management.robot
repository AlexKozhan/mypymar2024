*** Settings ***
Library  my_keywords.py

*** Test Cases ***
Reserve Book Successfully
    ${result}  Reserve Book  User1  Test Book  Author  100  12345
    Should Contain  ${result}  reserved by user User1

Take Book Successfully
    ${result}  Take Book  User1  Test Book  Author  100  12345
    Should Contain  ${result}  taken by user User1

Return Book Successfully
    Take Book  User1  Test Book  Author  100  12345
    ${result}  Return Book  User1  Test Book  Author  100  12345
    Should Contain  ${result}  returned by user User1

Take Book Already Reserved By Another User
    Reserve Book  User1  Test Book  Author  100  12345
    ${result}  Take Book  User2  Test Book  Author  100  12345
    Should Contain  ${result}  already reserved by user User1
