from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_swag_labs():
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
        # Login Steps (Wait for elements)
        username = wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.EditText[@content-desc=\"test-Username\"]")))

        password = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
        login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Assertion (Validate Products Page)
        products_title = wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']"))
        )
        assert products_title.is_displayed(), "Login failed or Products page not visible"

        print("✅ Test Passed: Successfully logged in to Swag Labs mobile app")

    except Exception as e:
        print(f"❌ Test Failed: {e}")
    finally:
        driver.quit()
