Feature: Find item user want to buy


  Scenario: Open category with desired item
    Given store main page is displayed
    When user click on "<category>" and choose paragraph with desired item
        | category            |
        | Desktops            |
        | Laptops & Notebooks |
        | Components          |
        | Tablets             |
        | Software            |
        | Phones & PDAs       |
        | Cameras             |
        | MP3 Players         |

    Then first page with items of chosen "<category>" paragraph displayed