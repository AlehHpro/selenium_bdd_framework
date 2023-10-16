from behave import *
from hamcrest import assert_that, is_


@then("KaseyaOne page is displayed.")
def step_impl(context):
    if_kaseyaone_page_is_displayed = context.kaseyaone_page.check_if_kaseyaone_page_is_displayed()
    assert_that(if_kaseyaone_page_is_displayed, is_(True))
