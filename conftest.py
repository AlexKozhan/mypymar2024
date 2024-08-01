import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Pytest fixture to set up the Selenium WebDriver with Chrome options.

    This fixture initializes a Chrome WebDriver
    instance with incognito mode and disabled
    password manager options. The WebDriver instance
    is provided to each test case, and
    it automatically quits after the test execution to clean up resources.

    Returns:
        WebDriver: A Chrome WebDriver instance configured for the test session.
    """
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    yield driver
    driver.quit()
