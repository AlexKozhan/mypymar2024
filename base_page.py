"""Base page"""


class BasePage:
    """Class Base Page"""
    def __init__(self, driver):
        """Initializes an instance of the example Class"""
        self.driver = driver

    def open(self, url):
        """Get driver url method"""
        self.driver.get(url)

    def find_element(self, selector):
        """Find element method"""
        return self.driver.find_element(*selector)
