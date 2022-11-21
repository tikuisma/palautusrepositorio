*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kissa1
    Set Password  kissa123
    Set Password Confirmation  kissa123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  tk
    Set Password  kissa456
    Set Password Confirmation  kissa456
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  koira
    Set Password  koira1
    Set Password Confirmation  koira1
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  orava
    Set Password  orava123
    Set Password Confirmation  orava456
    Submit Credentials
    Register Should Fail With Message  Passwords doesn't match with each other

Login After Successful Registration
    Set Username  ankka
    Set Password  ankka123
    Set Password Confirmation  ankka123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  ankka
    Set Password  ankka123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kana
    Set Password  kanat123
    Set Password Confirmation  ankka123
    Submit Credentials
    Register Should Fail With Message  Passwords doesn't match with each other
    Go To Login Page
    Login Page Should Be Open
    Set Username  kana
    Set Password  ankka123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kissa  kissa123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}