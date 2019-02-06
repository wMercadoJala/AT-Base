@acceptance
Feature: Create Projects
  Scenario: Create a Single Project
    Given I set up a "POST" request to "/projects.json" endpoint
      And I set up the data:
      """
      {
      "Content": "API Test",
      "Icon": 4
      }
      """
    When I send the request
    Then I get a "200" status code as response
