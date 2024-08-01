from selenium.webdriver.common.by import By


class LoginPage:
    """
    This class represents the Login page of the application.
    It provides methods to perform login actions.
    """
    def __init__(self, driver):
        """
        Initializes the page object with the provided
        WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance to
            use for interacting with the web page.
        """
        self.driver = driver
        self.url = "https://thinking-tester-contact-list.herokuapp.com/"
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

    def load(self):
        """
        Loads the Login page.
        """
        self.driver.get(self.url)

    def login(self, email, password):
        """
        Performs login action using the provided email and password.

        Args:
            email (str): The email address to use for login.
            password (str): The password to use for login.
        """
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
