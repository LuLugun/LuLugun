from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.whatismyip.com.tw/tw/")
str_ip_element = driver.find_element_by_xpath("/html/body/b")
str_ip = str_ip_element.get_attribute("textContent")
print(str_ip)
