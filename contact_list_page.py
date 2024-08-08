"""Contact list page"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from base_page import BasePage

add_button = (By.ID, "add-contact")
first_row = (By.XPATH, "//tr[@class='contactTableBodyRow'][1]")


class ContactListPage(BasePage):
    """Class Contact List Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def click_add_button(self):
        """Click add button"""
        btn = self.find_element(add_button)
        btn.click()

    def click_first_row(self):
        """Click first row"""
        row = self.find_element(first_row)
        row.click()

    def find_row(self):
        """Find row"""
        try:
            self.find_element(first_row)
            return True
        except NoSuchElementException:
            return False
