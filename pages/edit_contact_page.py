from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EditContactPage:
    """
    This class represents the Edit Contact page
    of the application. It provides methods to
    interact with the form
    for editing contact details.
    """
    def __init__(self, driver):
        """
        Initializes the page object with the
        provided WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance
            to use for interacting with the web page.
        """
        self.driver = driver
        self.fields = {
            "firstName": (By.ID, "firstName"),
            "lastName": (By.ID, "lastName"),
            "birthdate": (By.ID, "birthdate"),
            "email": (By.ID, "email"),
            "phone": (By.ID, "phone"),
            "street1": (By.ID, "street1"),
            "street2": (By.ID, "street2"),
            "city": (By.ID, "city"),
            "stateProvince": (By.ID, "stateProvince"),
            "postalCode": (By.ID, "postalCode"),
            "country": (By.ID, "country")
        }
        self.submit_button = (By.ID, "submit")

    def update_contact(self, updated_info):
        """
        Updates the contact information in the form with
        the provided details.

        Args:
            updated_info (dict): A dictionary containing
            the updated contact information.
                                 Keys are field IDs and
                                 values are the new
                                 values for those fields.
        """
        for field_id, value in updated_info.items():
            field = self.driver.find_element(*self.fields[field_id])
            field.clear()
            field.send_keys(Keys.CONTROL + "a")  # Select all text
            field.send_keys(Keys.DELETE)  # Delete selected text
            field.send_keys(value)
        self.driver.find_element(*self.submit_button).click()
