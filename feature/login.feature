Feature: Swag Labs Login

  Scenario: Valid user login
    Given the app is launched
    When I enter valid credentials
    Then I should be logged in
