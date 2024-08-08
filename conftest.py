"""Conftest module"""
import pytest
from selenium import webdriver
import test_data


@pytest.fixture
def driver():
    """Fixture for initializing and quitting a Chrome WebDriver instance"""
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)
    chrome.get(test_data.url)
    yield chrome
    chrome.quit()
