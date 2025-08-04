import time
from pages.login_page import LoginPage
from utils.data_reader import load_user_data
from utils.driver_factory import create_driver

def test_valid_login(driver):
    user = load_user_data("valid_user")  # ← Loads from JSON
    driver = create_driver()
    login = LoginPage(driver)
    login.enter_username(user["username"])
    login.enter_password(user["password"])
    login.click_login()
    time.sleep(5)
    assert "PRODUCTS" in driver.page_source
    driver.quit()


def test_invalid_username(driver):
    user = load_user_data("invalid_username")
    driver = create_driver()
    login = LoginPage(driver)
    login.enter_username(user["username"])
    login.enter_password(user["password"])
    login.click_login()
    time.sleep(2)
    assert "Username and password do not match" in driver.page_source
    driver.quit()

def test_invalid_password(driver):
    user = load_user_data("invalid_password")
    driver = create_driver()
    login = LoginPage(driver)
    login.enter_username(user["username"])
    login.enter_password(user["password"])
    login.click_login()
    time.sleep(2)
    assert "Username and password do not match" in driver.page_source
    driver.quit()

def test_blank_username(driver):
    user = load_user_data("blank_username")
    driver = create_driver()
    login = LoginPage(driver)
    login.enter_username(user["username"])
    login.enter_password(user["password"])
    login.click_login()
    time.sleep(2)
    assert "Username is required" in driver.page_source
    driver.quit()

def test_blank_password(driver):
    user = load_user_data("blank_password")
    driver = create_driver()
    login = LoginPage(driver)
    login.enter_username(user["username"])
    login.enter_password(user["password"])
    login.click_login()
    time.sleep(2)
    assert "Password is required" in driver.page_source
    driver.quit()

