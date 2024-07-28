import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    """
    Set up the Selenium WebDriver with Chrome options and return the driver instance.
    """
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def login(driver, email, password):
    """
    Log in to the application using the provided email and password.

    Args:
        driver: The Selenium WebDriver instance.
        email: The email address to use for login.
        password: The password to use for login.
    """
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()


def test_add_contact(driver):
    """
    Test case for adding a new contact to the contact list.

    This test will log in to the application, navigate to the add contact page,
    fill in the contact details, and submit the form.
    """
    login(driver, "wqwq@mail.ru", "sasassasas")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-contact")))
    driver.find_element(By.ID, "add-contact").click()

    driver.find_element(By.ID, "firstName").send_keys("Test")
    driver.find_element(By.ID, "lastName").send_keys("User")
    driver.find_element(By.ID, "birthdate").send_keys("2000-01-01")
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "phone").send_keys("1234567890")
    driver.find_element(By.ID, "street1").send_keys("123 Test St")
    driver.find_element(By.ID, "street2").send_keys("Apt 1")
    driver.find_element(By.ID, "city").send_keys("Test City")
    driver.find_element(By.ID, "stateProvince").send_keys("Test State")
    driver.find_element(By.ID, "postalCode").send_keys("12345")
    driver.find_element(By.ID, "country").send_keys("Test Country")
    driver.find_element(By.ID, "submit").click()

    time.sleep(5)  # Pause for visual inspection


def test_update_contact(driver):
    """
    Test case for updating an existing contact in the contact list.

    This test will log in to the application, navigate to the contact edit page,
    update the contact details, and submit the form.
    """
    login(driver, "wqwq@mail.ru", "sasassasas")

    (WebDriverWait(driver, 10).until
     (EC.element_to_be_clickable((By.XPATH, "//tr[@class='contactTableBodyRow'][1]"))).click())
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "edit-contact"))).click()

    fields = {
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

    for field_id, value in fields.items():
        field = driver.find_element(By.ID, field_id)
        field.clear()
        field.send_keys("")
        field.send_keys(value)

    driver.find_element(By.ID, "submit").click()

    time.sleep(5)  # Pause for visual inspection


def test_delete_contact(driver):
    """
    Test case for deleting an existing contact from the contact list.

    This test will log in to the application, navigate to the contact details page,
    and delete the contact.
    """
    login(driver, "wqwq@mail.ru", "sasassasas")

    (WebDriverWait(driver, 10).until
     (EC.element_to_be_clickable((By.XPATH, "//tr[@class='contactTableBodyRow'][1]"))).click())
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "delete"))).click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(5)  # Pause for visual inspection
