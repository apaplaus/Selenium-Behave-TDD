Feature: Open product page


  Scenario: User opens page of product
    Given user have seen block with link to certain product on store page
    When user clicks link with product
    Then page with detailed information about product displayed
    And block with purchase information displayed
