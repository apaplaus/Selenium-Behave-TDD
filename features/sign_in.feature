Feature: Logging into system


  Scenario: user sign in on site
    Given page with sign in "<fields>" is displayed
    And user has account on site
    When user fills sign in "<fields>" with valid data
            | fields         |
            | E-Mail Address |
            | Password       |
    Then user signs in
    And user have access to "<user pages>"
        | user page     |
        | My Account    |
        | Order History |
        | Transactions  |
        | Downloads     |
