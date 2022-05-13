from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://24h.pchome.com.tw/prod/DRAD1R-A900B8COL?fq=/S/DRAD1R")



button_buy = driver.find_element_by_xpath("//*[@id='ButtonContainer']/button")

button_buy.click()

time.sleep(3)

buy_car = driver.find_element_by_class_name("cart")

buy_car.click()

time.sleep(3)

account_number = driver.find_element_by_id("loginAcc")
account_number.send_keys(my_account)

password = driver.find_element_by_id("loginPwd")
password.send_keys(my_password)

log_in = driver.find_element_by_id("btnLogin")
log_in.click()

time.sleep(3)

input()
