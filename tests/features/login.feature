@login
Feature: Login
  As a user I want to be able to login to application.

  @login_1
  Scenario: Login with correct and incorrect data.
    When I enter invalid login on Login Page.
     And click [Login] button on Login Page.
    Then Alert is displayed on Login Page.
    When I enter valid login on Login Page.
     And click [Login] button on Login Page.
    Then Password field is displayed on Login Page.
    When I enter invalid login on Login Page.
     And click [Login] button on Login Page.
    Then Alert is displayed on Login Page.
    When I enter valid login on Login Page.
     And enter valid password on Login Page.
     And click [Login] button on Login Page.
    Then Authentication Page is displayed.
    When I click [Back] button on Authentication Page.
    Then Login page is displayed.
