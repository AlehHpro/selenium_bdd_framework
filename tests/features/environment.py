from pages.authentication_page import AuthenticationPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.kaseyaone_page import KaseyaonePage
from pages.login_page import LoginPage
from utils.capabilities_util import get_driver


def before_all(context):
    # setup global variables.
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"])
    # setup page objects.
    context.login_page = LoginPage(context=context)
    context.authentication_page = AuthenticationPage(context=context)
    context.forgot_password_page = ForgotPasswordPage(context=context)
    context.kaseyaone_page = KaseyaonePage(context=context)
    # open application under test.
    context.login_page.go_to_url(url="https://dev.darkwebid.io/user/login?destination=resellers")


def after_all(context):
    context.login_page.quite()
