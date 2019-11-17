Feature: Adjust content of shopping cart


  Scenario: User changes "Quantity" of certain product in cart
    Given "Shopping cart" page is displayed
    And shopping cart isn't empty
    When user changes "Quantity" field in row with appropriate product
    And press "Update" button
    Then page reloads
    And "Total" price for this item changes
    And "Total" price for all items in cart changes

  Scenario: User delete product from shopping cart
    Given "Shopping cart" page is displayed
    And shopping cart has more than one product
    When user press "Remove" button on appropriate product
    Then field with notification about successful deletion displayed
    And item removed from shopping cart
    And "Total" price for all items in cart changes

  Scenario: User delete last product from shopping cart
    Given "Shopping cart" page is displayed
    And shopping cart has one product
    When user press "Remove" button on appropriate product
    Then page with empty shopping cart is displayed
    And "Total" price for all items in cart changes
