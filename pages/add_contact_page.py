from selenium.webdriver.common.by import By


class AddContactPage:
    """
    This class represents the Add Contact
    page of the application.
    It provides methods to interact with
    the page's elements and add a new contact.
    """

    def __init__(self, driver):
        """
        Initializes the page object with the provided
        WebDriver instance and sets up the locators.

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

    def add_contact(self, contact_info):
        """
        Fills out the contact form with the provided
        contact information and submits it.

        Args:
            contact_info (dict): A dictionary containing
            the contact information to be entered.
                                 Keys are field IDs and values
                                 are the data to be filled in.
        """
        for field_id, value in contact_info.items():
            field = self.driver.find_element(*self.fields[field_id])
            field.send_keys(value)
        self.driver.find_element(*self.submit_button).click()
