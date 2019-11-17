Feature: Add item for purchase to shopping cart


  Scenario: User complete "Available Options" block
    Given page of product displayed
    And block with "Available Options" is representing
    When user completes all required fields
        | fields      |
        | Select      |

    Then user can add item to shopping cart


  Scenario: Add item to shopping cart
    Given user has logged in
    And page with desired product displayed
    And block "Available Options" is not present or filled up with valid data
    And user has chosen quantity of product
    When user clicks on "Add to cart" button
    Then product adds to users cart
    And field with notification about successful operation displayed
    And button representing shopping cart changes in accordance with the addition
