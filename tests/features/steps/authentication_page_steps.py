from behave import *
from hamcrest import assert_that, is_


@then("Authentication Page is displayed.")
def step_impl(context):
    if_authentication_page_is_displayed = context.authentication_page.check_if_authentication_page_is_displayed()
    assert_that(if_authentication_page_is_displayed, is_(True))


@when("I click [Back] button on Authentication Page.")
def step_impl(context):
    context.authentication_page.click_back_button()
