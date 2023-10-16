from behave import *
from hamcrest import assert_that, is_


@when("I enter invalid login on Login Page.")
def step_impl(context):
    context.login_page.enter_invalid_login()


@step("click [Login] button on Login Page.")
def step_impl(context):
    context.login_page.click_login_button()


@then("Alert is displayed on Login Page.")
def step_impl(context):
    if_alert_is_present = context.login_page.check_if_alert_is_present()
    assert_that(if_alert_is_present, is_(True))


@when("I enter valid login on Login Page.")
def step_impl(context):
    context.login_page.enter_valid_login()


@then("Password field is displayed on Login Page.")
def step_impl(context):
    if_password_field_is_present = context.login_page.check_if_password_field_is_present()
    assert_that(if_password_field_is_present, is_(True))


@step("enter valid password on Login Page.")
def step_impl(context):
    context.login_page.enter_valid_password()


@then("Login page is displayed.")
def step_impl(context):
    if_login_page_is_displayed = context.login_page.check_if_login_page_is_displayed()
    assert_that(if_login_page_is_displayed, is_(True))


@then("[Forgot Password] link is present on Login Page.")
def step_impl(context):
    if_forgot_password_link_is_displayed = context.login_page.check_if_forgot_password_link_is_present()
    assert_that(if_forgot_password_link_is_displayed, is_(True))


@when("I click [Forgot Password] link on Login Page.")
def step_impl(context):
    context.login_page.click_forgot_password_link()


@when("I click [Login With KaseyaOne] button on Login Page.")
def step_impl(context):
    context.login_page.click_login_with_kaseyaone_button()
