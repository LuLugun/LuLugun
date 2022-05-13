import unittest
from appium import webdriver
import time

desired_caps = dict(
    platformName='Android',
    platformVersion='11',
    automationName='UiAutomator2',
    skipUnlock=False,
    deviceName='Pixel 4 API 30',
    appPackage ="com.google.android.youtube",
    appActivity ="com.google.android.apps.youtube.app.WatchWhileActivity"
    )

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

webview_list = driver.contexts
print(webview_list)
