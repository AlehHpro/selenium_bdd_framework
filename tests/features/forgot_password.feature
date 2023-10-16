@forgot_password
Feature: Forgot password
  As a user I want to be able to restore my password.

  @forgot_password_1
  Scenario: Restore password with 'Forgot password' link.
    When I enter valid login on Login Page.
     And Click [Login] button on Login Page.
    Then [Forgot Password] link is present on Login Page.
    When I click [Forgot Password] link on Login Page.
    Then Forgot Password Page is displayed.
    When I enter valid login on Forgot Password Page.
     And Click [Reset Password] button on Forgot Password Page.
    Then 'Email Sent' message is displayed on Forgot Password Page.
    When I click Back to Login button on Forgot Password Page.
    Then Login Page is displayed.