from PageObjectLibrary import PageObject

from robot.libraries.BuiltIn import BuiltIn


class LoginPage(PageObject):
    PAGE_TITLE = "Tokenize Xchange | Digital Currency Trading Platform"
    PAGE_URL = "/login?redirectUrl=https://tokenize-dev.com/sso-callback"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "welcome_back_text": "//h4[text()='Welcome Back']",
        "we_are_so_excited_to_see_you_again": "//p[contains(., 'We are so excited to see you again.')]",
        "email": "//label[text()='Email']/following-sibling::div//input[@type='text']",
        "password": "//label[text()='Password']/following-sibling::div//input[@type='password']",
        "submit_button": "//button[.//p[text()='Log In']]"
    }

    def log_in_page_should_show_welcome_text(self):
        config = BuiltIn().get_variable_value("${CONFIG}")
        
    def login_as_a_normal_user(self):
        config = BuiltIn().get_variable_value("${CONFIG}")
        self.enter_email(config.email)
        self.enter_password(config.password)
        with self._wait_for_page_refresh():
            self.click_the_submit_button()

    def enter_email(self, email):
        """Enter the given string into the email field"""
        self.selib.input_text(self.locator.email, email)

    def enter_password(self, password):
        """Enter the given string into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_submit_button(self):
        """Click the submit button, and wait for the page to reload"""
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_button)
