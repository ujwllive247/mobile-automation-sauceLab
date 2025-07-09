from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_full_integration_flow():
    # Desired Capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.SplashActivity"
    options.no_reset = False

    # Launch App
    driver = webdriver.Remote("http://localhost:4723", options=options)
    wait = WebDriverWait(driver, 20)

    try:
        # Login
        wait.until(EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Username"))).send_keys("standard_user")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

        # Add to cart
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")))
        driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()

        # Go to cart
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='YOUR CART']")))

        # Checkout
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT").click()

        # Fill user info
        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-First Name"))).send_keys("John")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Last Name").send_keys("Doe")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code").send_keys("12345")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE").click()

        # Finish checkout
        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-FINISH"))).click()
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT: COMPLETE!']")))

        # Back to home
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-BACK HOME").click()

        # Logout
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Menu").click()
        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT"))).click()

        print("✅ Integration Test Passed: Full checkout flow completed.")

    except Exception as e:
        print(f"❌ Test Failed: {e}")

    finally:
        driver.quit()
