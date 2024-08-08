"""Add contact page"""

from selenium.webdriver.common.by import By
from base_page import BasePage

first_name = (By.ID, "firstName")
last_name = (By.ID, "lastName")
birthdate = (By.ID, "birthdate")
email = (By.ID, "email")
phone = (By.ID, "phone")
street1 = (By.ID, "street1")
street2 = (By.ID, "street2")
city = (By.ID, "city")
state_province = (By.ID, "stateProvince")
postal_code = (By.ID, "postalCode")
country = (By.ID, "country")
button = (By.ID, "submit")


class AddContactPage(BasePage):
    """Class add contact page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def enter_first_name(self, fn):
        """Enter first name"""
        el_input = self.find_element(first_name)
        el_input.send_keys(fn)

    def enter_last_name(self, ln):
        """Enter last name"""
        el_input = self.find_element(last_name)
        el_input.send_keys(ln)

    def enter_birthdate(self, bd):
        """Enter birthdate"""
        el_input = self.find_element(birthdate)
        el_input.send_keys(bd)

    def enter_email(self, eml1):
        """Enter email"""
        el_input = self.find_element(email)
        el_input.send_keys(eml1)

    def enter_phone(self, pn):
        """Enter phone"""
        el_input = self.find_element(phone)
        el_input.send_keys(pn)

    def enter_street1(self, str1):
        """Enter street 1"""
        el_input = self.find_element(street1)
        el_input.send_keys(str1)

    def enter_street2(self, str2):
        """Enter street 2"""
        el_input = self.find_element(street2)
        el_input.send_keys(str2)

    def enter_city(self, ct):
        """Enter city"""
        el_input = self.find_element(city)
        el_input.send_keys(ct)

    def enter_state_province(self, stpr):
        """Enter state or province"""
        el_input = self.find_element(state_province)
        el_input.send_keys(stpr)

    def enter_postal_code(self, pc):
        """Enter postal code"""
        el_input = self.find_element(postal_code)
        el_input.send_keys(pc)

    def enter_country(self, cntr):
        """Enter country"""
        el_input = self.find_element(country)
        el_input.send_keys(cntr)

    def click_submit_button(self):
        """Click submit button"""
        btn = self.find_element(button)
        btn.click()

    def add_contact(self, fn, ln, bd, eml1, pn, str1, str2,
                    ct, stpr, pc, cntr):
        """Add contact"""
        self.enter_first_name(fn)
        self.enter_last_name(ln)
        self.enter_birthdate(bd)
        self.enter_email(eml1)
        self.enter_phone(pn)
        self.enter_street1(str1)
        self.enter_street2(str2)
        self.enter_city(ct)
        self.enter_state_province(stpr)
        self.enter_postal_code(pc)
        self.enter_country(cntr)
        self.click_submit_button()
