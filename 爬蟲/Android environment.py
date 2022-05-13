# Android environment
import unittest
from appium import webdriver
import time

desired_caps = dict(
    platformName='Android',
    platformVersion='11',
    automationName='UiAutomator2',
    skipUnlock=False,
    deviceName='Pixel 4 API 30',
    browserName = 'Chrome',
    chromedriverExecutable = "D:\\chromedriver_83.0.4103\\chromedriver.exe"
    )

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

while True:
    webview = driver.contexts
    #print(type(webview))
    #print(webview[-1])
    webview_list = driver.contexts
    print(webview_list)
    #driver.switch_to.context(webview[-1])
    time.sleep(5)

'''driver.get("https://www.youtube.com/")

time.sleep(10)

while True:
    links = driver.find_elements_by_xpath('//a[@class="large-media-item-thumbnail-container"]')
    for link in links:
        partial_href = link.get_attribute("href")
        print(str(partial_href))
        
    driver.swipe(519,1864,519,519, 500)'''

'''html = driver.page_source
file_name = 'test_1.html'
f = open(file_name,"w",encoding='utf8')
f.write(html)
f.close()'''
