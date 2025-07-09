from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def test_open_youtube_allow_notifications():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.google.android.youtube"
    options.app_activity = "com.google.android.youtube.HomeActivity"
    options.no_reset = False  # Reset so pop-up appears again

    driver = webdriver.Remote("http://localhost:4723", options=options)
    driver.implicitly_wait(10)

    # Click "Allow" if notification pop-up appears
    try:
        allow_button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        allow_button.click()
        print("Notification permission granted.")
    except:
        print("No notification pop-up appeared.")

    time.sleep(5)
    driver.quit()
