"""Contact details page"""

from selenium.webdriver.common.by import By
from base_page import BasePage

edit_button = (By.ID, "edit-contact")
delete_button = (By.ID, "delete")
first_name = (By.ID, "firstName")


class ContactDetailsPage(BasePage):
    """Class Contact Details Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        super().__init__(driver)

    def click_edit_button(self):
        """Click edit button"""
        btn = self.find_element(edit_button)
        btn.click()

    def get_first_name_text(self):
        """Get first name text"""
        f_name = self.find_element(first_name)
        return f_name.text

    def click_delete_button(self):
        """Click delete button"""
        btn = self.find_element(delete_button)
        btn.click()
