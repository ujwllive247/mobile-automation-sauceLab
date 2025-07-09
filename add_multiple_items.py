
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_multiple_items_to_cart():
    # Desired Capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.SplashActivity"
    options.no_reset = False

    # Start Appium session
    driver = webdriver.Remote("http://localhost:4723", options=options)
    wait = WebDriverWait(driver, 20)

    try:
        # Login
        username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username")))
        password = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password")
        login_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        # Wait for product list
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")))

        # Add 3 items to cart
        for i in range(3):
            add_btns = driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']")
            if i < len(add_btns):
                add_btns[i].click()
            else:
                break

        # Go to cart
        cart_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart")
        cart_icon.click()

        # Wait for cart page
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='YOUR CART']")))

        # Validate 3 items present in cart
        cart_items = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='test-Item title']")
        assert len(cart_items) == 3, f"Expected 3 items in cart, but found {len(cart_items)}"

        print("✅ Test Passed: 3 items successfully added and present in cart")

    except Exception as e:
        print(f"❌ Test Failed: {e}")
    finally:
        driver.quit()
