#Feature: Reset functionality on login page of Application
#  Scenario: Verification of Reset button
#    Given Open the Firefox and launch the application
#    When Enter the Username and Password
#    Then Reset the credential

Feature: login application
  Scenario: Verification login
    Given Open the Chrome and launch the application
    When Enter the Username and Password
    And Click Search Button
    Then Go to home page

  Scenario: Page Navigation
    Given After Login the application
    When Select New Customer
    Then Can See Add customer form

  Scenario: fill the form
    Given showing add customer page
    When filling the form
    And Click submit button
    Then click the submit the button

