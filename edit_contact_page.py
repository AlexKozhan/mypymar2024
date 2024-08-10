"""Edit contact page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


class EditContactPage(BasePage):
    """Class edit contact page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def edit_first_name(self, fn_1):
        """Edit first name"""
        el_input = self.find_element(first_name)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(first_name, "")))
        el_input.send_keys(fn_1)
        (WebDriverWait(self.driver, 10).
         until(EC.text_to_be_present_in_element_value(first_name, fn_1)))

    def edit_last_name(self, ln_1):
        """Edit last name"""
        el_input = self.find_element(last_name)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(last_name, "")))
        el_input.send_keys(ln_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(last_name, ln_1)))

    def edit_birthdate(self, bd_1):
        """Edit birthdate"""
        el_input = self.find_element(birthdate)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(birthdate, "")))
        el_input.send_keys(bd_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(birthdate, bd_1)))

    def edit_email(self, eml1_1):
        """Edit email"""
        el_input = self.find_element(email)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(email, "")))
        el_input.send_keys(eml1_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(email, eml1_1)))

    def edit_phone(self, pn_1):
        """Edit phone"""
        el_input = self.find_element(phone)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(phone, "")))
        el_input.send_keys(pn_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(phone, pn_1)))

    def edit_street1(self, str1_1):
        """Edit street 1"""
        el_input = self.find_element(street1)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(street1, "")))
        el_input.send_keys(str1_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(street1, str1_1)))

    def edit_street2(self, str2_1):
        """Edit street 2"""
        el_input = self.find_element(street2)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(street2, "")))
        el_input.send_keys(str2_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(street2, str2_1)))

    def edit_city(self, ct_1):
        """Edit city"""
        el_input = self.find_element(city)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(city, "")))
        el_input.send_keys(ct_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(city, ct_1)))

    def edit_state_province(self, stpr_1):
        """Edit state or province"""
        el_input = self.find_element(state_province)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(state_province, "")))
        el_input.send_keys(stpr_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(state_province, stpr_1)))

    def edit_postal_code(self, pc_1):
        """Enter postal code"""
        el_input = self.find_element(postal_code)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(postal_code, "")))
        el_input.send_keys(pc_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(postal_code, pc_1)))

    def edit_country(self, cntr_1):
        """Enter country"""
        el_input = self.find_element(country)
        el_input.clear()
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(country, "")))
        el_input.send_keys(cntr_1)
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value(country, cntr_1)))

    def click_submit_button(self):
        """Click submit button"""
        btn = self.find_element(button)
        btn.click()

    def edit_contact(self, fn_1, ln_1, bd_1, eml1_1, pn_1, str1_1,
                     str2_1, ct_1, stpr_1, pc_1, cntr_1):
        """Edit contact"""
        self.edit_first_name(fn_1)
        self.edit_last_name(ln_1)
        self.edit_birthdate(bd_1)
        self.edit_email(eml1_1)
        self.edit_phone(pn_1)
        self.edit_street1(str1_1)
        self.edit_street2(str2_1)
        self.edit_city(ct_1)
        self.edit_state_province(stpr_1)
        self.edit_postal_code(pc_1)
        self.edit_country(cntr_1)
        self.click_submit_button()
