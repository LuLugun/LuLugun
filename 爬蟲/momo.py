from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8281104&osm=Ad07&utm_source=googleshop&utm_medium=googleshop_USC&utm_content=bn&gclid=Cj0KCQjwytOEBhD5ARIsANnRjViXl4TJCFVZUlTlUFhmRTgufYuNTOIufxG97ePn8P4RSrRIvO8ylcIaAto8EALw_wcB")


button_buy = driver.find_element_by_xpath("//*[@id='buy_yes']/a/img")
button_buy.click()
time.sleep(1)


account_number = driver.find_element_by_id("memId")
account_number.send_keys('my_account')

hideIcon_closed = driver.find_element_by_id("showLoginPwd")
hideIcon_closed.click()
passwd_show = driver.find_element_by_id("passwd_show")
passwd_show.click()
password = driver.find_element_by_id("passwd")
password.send_keys('my_password')


#log_in = driver.find_element_by_xpath("//*[@id='loginForm']/dl[2]/dd[7]/input")
#log_in.click()
time.sleep(1)


input()