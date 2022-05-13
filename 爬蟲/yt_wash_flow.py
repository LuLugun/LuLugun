from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.common.exceptions import TimeoutException ,InvalidArgumentException
from selenium.webdriver.chrome.options import Options

    
def Web_Driver_Wait(chrome_driver,str_xpath):
    while True:
        try:
            element = WebDriverWait(chrome_driver,10,0.5).until(
                EC.presence_of_element_located((By.XPATH,str_xpath))
            )
        except:
            print("loding")
        else:
            break

url = input('請輸入yt影片連結:')
chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")

driver = webdriver.Chrome(executable_path=r'D:\chromedriver\chromedriver.exe',options = chromeoptions)
driver.get(url)
Web_Driver_Wait(driver,'//*[@id="player"]')
time.sleep(5)
driver.close()

