"""Login page"""
from selenium.webdriver.common.by import By

from base_page import BasePage

email = (By.ID, "email")
password = (By.ID, "password")
button = (By.ID, "submit")


class LoginPage(BasePage):
    """Class Login Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def enter_email(self, eml):
        """Enter email"""
        el_input = self.find_element(email)
        el_input.send_keys(eml)

    def enter_password(self, psw):
        """Enter password"""
        el_input = self.find_element(password)
        el_input.send_keys(psw)

    def click_login_button(self):
        """Click login button"""
        btn = self.find_element(button)
        btn.click()

    def complete_login(self, eml, psw):
        """Complete login"""
        self.enter_email(eml)
        self.enter_password(psw)
        self.click_login_button()
