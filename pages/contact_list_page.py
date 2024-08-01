from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactListPage:
    """
    This class represents the Contact List page of the application.
    It provides methods to interact with the list of
    contacts and perform actions such as adding, editing,
    and deleting contacts.
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
        self.add_contact_button = (By.ID, "add-contact")
        self.first_contact_row = \
            (By.XPATH, "//tr[@class='contactTableBodyRow'][1]")
        self.edit_button = (By.ID, "edit-contact")
        self.delete_button = (By.ID, "delete")

    def click_add_contact(self):
        """
        Clicks the button to navigate to the Add Contact page.

        Waits until the 'Add Contact' button is clickable before
        clicking it.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_contact_button)
        ).click()

    def select_first_contact(self):
        """
        Selects the first contact in the contact list.

        Waits until the first contact row is clickable before
        clicking it.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_contact_row)
        ).click()

    def click_edit_contact(self):
        """
        Clicks the button to navigate to the Edit Contact
        page for the selected contact.

        Waits until the 'Edit Contact' button is clickable before clicking it.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_button)
        ).click()

    def click_delete_contact(self):
        """
        Clicks the button to delete the selected contact.

        Waits until the 'Delete' button is clickable before clicking it.
        After clicking, waits for an alert to appear
        and then accepts the alert to confirm deletion.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
