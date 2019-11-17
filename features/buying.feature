Feature: Order items


  Scenario Outline: User filling up "<Delivery/Billing Details>" block with new address
    Given user has been logged in
    And shopping cart isn't empty
    And "Checkout" page is displayed
    And "Use new address" box is checked
    When user fills up "<required fields>" with valid data
    Then next "Step" field opens

    Examples: Valid data fields
    | First Name | Last Name | Address 1 | City | Country        | Region / State |
    | Test       | Test      | myAddress | City | Czech Republic | Jihocesky      |

  Scenario: User completes Checkout and confirm Order
    Given user has been logged in
    And "Checkout" page is displayed
    And steps 1, 2 and 3 in "Checkout" are completed
    When user choose "Delivery Method"
    And choose "Payment Method" with confirmation of "Terms & Conditions"
    And click "Confirm Order" button in "Step 6" box
    Then page with successful order placement displayed
    And shopping cart becomes empty
    And order adds to "Order History" user's page
