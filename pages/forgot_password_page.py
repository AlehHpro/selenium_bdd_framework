from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    __FP_PAGE_TITLE = (By.XPATH, "//h1[text()='Forgot Password']")
    __FP_EMAIL_FIELD = (By.ID, "edit-name")
    __FP_RESET_BUTTON = (By.ID, "edit-submit")
    __FP_BACK_TO_LOGIN_BUTTON = (By.XPATH, "//*[@id='block-system-main']/a")
    __FP_EMAIL_SENT_MESSAGE = (By.XPATH, "//h1[text()='Email Sent']")

    def enter_valid_email(self):
        self.fill(by_locator=self.__FP_EMAIL_FIELD, value=BasePage.VALID_EMAIL)

    def enter_invalid_email(self):
        self.fill(by_locator=self.__FP_EMAIL_FIELD, value=BasePage.INVALID_EMAIL)

    def click_reset_button(self):
        self.click(by_locator=self.__FP_RESET_BUTTON)

    def click_back_to_login_button(self):
        self.click(by_locator=self.__FP_BACK_TO_LOGIN_BUTTON)
        self.explicitly_wait.until(expected_conditions.title_is("Account | Dark Web ID"))

    def check_if_forgot_password_page_is_displayed(self):
        return self.if_element_present(by_locator=self.__FP_PAGE_TITLE)

    def check_if_email_sent_message_is_displayed(self):
        return self.if_element_present(by_locator=self.__FP_EMAIL_SENT_MESSAGE)
