from behave import *
from hamcrest import assert_that, is_


@then("Forgot Password Page is displayed.")
def step_impl(context):
    if_forgot_password_page_is_displayed = context.forgot_password_page.check_if_forgot_password_page_is_displayed()
    assert_that(if_forgot_password_page_is_displayed, is_(True))


@when("I enter valid login on Forgot Password Page.")
def step_impl(context):
    context.forgot_password_page.enter_valid_email()


@step("Click [Reset Password] button on Forgot Password Page.")
def step_impl(context):
    context.forgot_password_page.click_reset_button()


@then("'Email Sent' message is displayed on Forgot Password Page.")
def step_impl(context):
    if_email_sent_message_is_displayed = context.forgot_password_page.check_if_email_sent_message_is_displayed()
    assert_that(if_email_sent_message_is_displayed, is_(True))


@when("I click Back to Login button on Forgot Password Page.")
def step_impl(context):
    context.forgot_password_page.click_back_to_login_button()