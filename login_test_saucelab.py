import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.SplashActivity"
    options.no_reset = False

    driver = webdriver.Remote("http://localhost:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    assert driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']").is_displayed()

def test_invalid_username(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("invalid_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    error = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']")
    assert error.is_displayed()

def test_invalid_password(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("wrong_password")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    error = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']")
    assert error.is_displayed()

def test_blank_credentials(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    error = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']")
    assert error.is_displayed()

def test_locked_out_user(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("locked_out_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    error = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']")
    assert error.is_displayed()
