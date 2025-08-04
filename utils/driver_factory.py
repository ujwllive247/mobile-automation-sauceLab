from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait


def create_driver():
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
    return driver
