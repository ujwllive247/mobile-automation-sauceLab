from pytest_bdd import given, when, then
from utils.driver_factory import create_driver
from pages.login_page import LoginPage

driver = None

@given("the app is launched")
def launch_app():
    global driver
    driver = create_driver()

@when("I enter valid credentials")
def enter_credentials():
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

@then("I should be logged in")
def verify_login():
    assert "Products" in driver.page_source
    driver.quit()
