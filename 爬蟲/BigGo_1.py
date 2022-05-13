from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")

def Web_Driver_Wait(chrome_driver,str_xpath):
    i = 1
    while True:
        try:
            element = WebDriverWait(chrome_driver,1,0.5).until(
                EC.presence_of_element_located((By.XPATH,str_xpath))
            )
        except:
            #print("loding")
            js = 'var q=document.documentElement.scrollTop='+ str(500*i)
            driver.execute_script(js)
            i += 1
        else:
            break

driver = webdriver.Chrome(chrome_options = chromeoptions)
driver.maximize_window()
driver.get("https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645")
Web_Driver_Wait(driver,'//*[@id="main"]/div/div[3]/div/div[4]/div[2]/div/div[2]/div[60]/a/div/div/div[2]/div[1]/div/div')
title_list = driver.find_elements(By.XPATH,'//div[@class="ie3A+n bM+7UW Cve6sh"]')
price_list = driver.find_elements(By.XPATH,'//div[@class="vioxXd pw1xTt rVLWG6"]')

for i in title_list:
    print('title:',i.get_attribute("textContent"),end = ' ')
    print('price:',price_list[title_list.index(i)].get_attribute("textContent"))


