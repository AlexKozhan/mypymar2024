"""Tests"""
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage
from contact_list_page import ContactListPage
from add_contact_page import AddContactPage
from contact_details_page import ContactDetailsPage
from edit_contact_page import EditContactPage
import test_data
import logger_module


@pytest.mark.login
def test_login_success(driver):
    """Test login successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    assert test_data.url1 in driver.current_url
    logger_module.logger.info("Test login successfully complete")


@pytest.mark.add_contact
def test_add_contact(driver):
    """Test add contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain2)))
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp.click_first_row()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain3)))
    assert test_data.url3 in driver.current_url
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp = ContactListPage(driver)
    assert clp.find_row() is False
    logger_module.logger.info("Test add contact successfully complete")


@pytest.mark.edit_contact
def test_edit_contact(driver):
    """Test edit contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain2)))
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp.click_first_row()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain3)))
    assert test_data.url3 in driver.current_url

    cdp = ContactDetailsPage(driver)
    cdp.click_edit_button()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain4)))
    ecp = EditContactPage(driver)
    time.sleep(1)
    ecp.edit_contact(test_data.fn_1, test_data.ln_1, test_data.bd_1,
                     test_data.eml1_1, test_data.pn_1, test_data.str1_1,
                     test_data.str2_1, test_data.ct_1, test_data.stpr_1,
                     test_data.pc_1, test_data.cntr_1)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain3)))
    time.sleep(1)
    assert cdp.get_first_name_text() == test_data.fn_1
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp = ContactListPage(driver)
    assert clp.find_row() is False
    logger_module.logger.info("Test edit contact successfully complete")


@pytest.mark.delete_contact
def test_delete_contact(driver):
    """Test delete contact successfully"""
    lp = LoginPage(driver)
    lp.complete_login(test_data.eml, test_data.psw)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    assert test_data.url1 in driver.current_url

    clp = ContactListPage(driver)
    clp.click_add_button()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain2)))
    assert test_data.url2 in driver.current_url

    acp = AddContactPage(driver)
    acp.add_contact(test_data.fn, test_data.ln, test_data.bd,
                    test_data.eml1, test_data.pn, test_data.str1,
                    test_data.str2, test_data.ct, test_data.stpr,
                    test_data.pc, test_data.cntr)
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp.click_first_row()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain3)))
    assert test_data.url3 in driver.current_url
    cdp = ContactDetailsPage(driver)
    cdp.click_delete_button()
    alert = driver.switch_to.alert
    alert.accept()
    (WebDriverWait(driver, 10).until
     (EC.url_contains(test_data.url_contain1)))
    clp = ContactListPage(driver)
    assert clp.find_row() is False
    logger_module.logger.info("Test delete contact successfully complete")
