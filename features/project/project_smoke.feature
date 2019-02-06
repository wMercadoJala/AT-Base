@smoke
Feature: Get Projects
  Scenario: Get All Projects
    Given I set up a "GET" request to "/projects.json" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get All Projects II
    Given I set up a retrieve of all Projects
    When I send the request
    Then I get an OK response