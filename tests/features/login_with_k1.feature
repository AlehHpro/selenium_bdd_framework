@login_with_kaseyaone
Feature: Login with KaseyaOne
  As a user I want to be able to login to application with KaseyaOne.

  @login_with_kaseyaone_1
  Scenario: Navigate to KaseyaOne page
    When I click [Login With KaseyaOne] button on Login Page.
    Then KaseyaOne page is displayed.