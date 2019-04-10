Feature: Open the facebook page

  Scenario: Open the facebook page
    Given I open the browser
    And I type the url in the address bar
    Then I verify the "Facebook - Log In or Sign Up" is displayed
    And I quit the browser
