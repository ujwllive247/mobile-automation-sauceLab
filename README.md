# mobile-automation-sauceLab
Mobile Automation Setup Guide with Python, Appium, and Pytest (Android)
This document provides a complete step-by-step setup for mobile automation using Python, Appium, and Pytest on an Ubuntu/Linux environment.

✅ 1. Install Java JDK (Required for Android SDK)
sudo apt update
sudo apt install openjdk-11-jdk
java -version

✅ 2. Install Python and Required Packages
sudo apt install python3-pip
pip3 install Appium-Python-Client pytest

✅ 3. Install Node.js and Appium Server
sudo apt install curl
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v

# Install Appium and Appium Doctor
npm install -g appium
npm install -g @appium/doctor

# Verify installation
appium -v
appium-doctor

✅ 4. Install Android Studio (for SDK & Emulator)
Go to: https://developer.android.com/studio
Download the .deb file and install:
sudo dpkg -i android-studio-*.deb
sudo apt --fix-broken install
Open Android Studio:
Install SDK Tools: platform-tools, emulator, build-tools, etc.
Create and start a virtual device (AVD).

✅ 5. Set ANDROID_HOME and Environment Variables
Edit the file:
nano ~/.bashrc
Add at the bottom:
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
Then apply the changes:
source ~/.bashrc
Verify SDK paths:
echo $ANDROID_HOME

✅ 6. Verify ADB and Emulator
adb devices
emulator -list-avds

✅ 7. Launch Appium Inspector (Optional for Element Inspection)
Download .AppImage from: https://github.com/appium/appium-inspector/releases
Make it executable:
chmod +x Appium-Inspector-*.AppImage
./Appium-Inspector-*.AppImage
Start Appium server:
appium

✅ 8. Sample conftest.py with Pytest for Appium
import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "13",
        "deviceName": "emulator-5554",
        "appPackage": "com.example.android",
        "appActivity": ".MainActivity",
        "automationName": "UiAutomator2",
        "noReset": True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

✅ 9. Sample Test File test_sample.py
def test_example(driver):
    el = driver.find_element("id", "com.example.android:id/button")
    el.click()
    assert driver.find_element("id", "com.example.android:id/text").is_displayed()
Run the test:
pytest test_sample.py -v

🛠 Recommended Tools
Tool
Use
Appium Inspector
Visual element locator
ADB
Device control
uiautomatorviewer
Android UI inspection
Charles Proxy / Wireshark
Network inspection
Allure
Test reports


