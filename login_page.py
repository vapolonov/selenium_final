from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url('login')
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, substring):
        # реализуйте проверку на корректный url адрес
        full_string = self.browser.execute_script("return document.documentURI;")
        assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD), "Registration password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), "Registration confirm password is not presented"
