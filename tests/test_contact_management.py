import time
from pages.login_page import LoginPage
from pages.contact_list_page import ContactListPage
from pages.add_contact_page import AddContactPage
from pages.edit_contact_page import EditContactPage


def test_add_contact(driver):
    """
    Test case for adding a new contact to the contact list.

    This test logs into the application, navigates to the add contact page,
    fills in the contact details, and submits the form.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wqwq@mail.ru", "sasassasas")

    contact_list_page = ContactListPage(driver)
    contact_list_page.click_add_contact()

    contact_info = {
        "firstName": "Test",
        "lastName": "User",
        "birthdate": "2000-01-01",
        "email": "testuser@example.com",
        "phone": "1234567890",
        "street1": "123 Test St",
        "street2": "Apt 1",
        "city": "Test City",
        "stateProvince": "Test State",
        "postalCode": "12345",
        "country": "Test Country"
    }

    add_contact_page = AddContactPage(driver)
    add_contact_page.add_contact(contact_info)

    time.sleep(5)  # Pause for visual inspection


def test_update_contact(driver):
    """
    Test case for updating an existing contact in
    the contact list.

    This test logs into the application, navigates
    to the contact edit page,
    updates the contact details, and submits the form.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wqwq@mail.ru", "sasassasas")

    contact_list_page = ContactListPage(driver)
    contact_list_page.select_first_contact()
    contact_list_page.click_edit_contact()

    updated_info = {
        "firstName": "Updated",
        "lastName": "User",
        "birthdate": "1990-01-01",
        "email": "updateduser@example.com",
        "phone": "0987654321",
        "street1": "456 Updated St",
        "street2": "Apt 2",
        "city": "Updated City",
        "stateProvince": "Updated State",
        "postalCode": "54321",
        "country": "Updated Country"
    }

    edit_contact_page = EditContactPage(driver)
    edit_contact_page.update_contact(updated_info)

    time.sleep(5)  # Pause for visual inspection


def test_delete_contact(driver):
    """
    Test case for deleting an existing contact from the contact list.

    This test logs into the application, navigates to
    the contact details page,
    and deletes the contact.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wqwq@mail.ru", "sasassasas")

    contact_list_page = ContactListPage(driver)
    contact_list_page.select_first_contact()
    contact_list_page.click_delete_contact()

    time.sleep(5)  # Pause for visual inspection
