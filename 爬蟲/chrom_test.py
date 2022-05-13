from os import write
from selenium import webdriver
import time


def save_html(f,driver):
    html = driver.page_source
    f.write(html)

    iframe_lst = driver.find_elements_by_xpath("//iframe")

    frame_lst = driver.find_elements_by_xpath("//frame") 

    print(frame_lst)
    
    for sub_htm in iframe_lst+frame_lst:
        try:
            driver.switch_to_frame(sub_htm)
            #print(sub_htm)

        except:
            pass

        save_html(f,driver)
    

driver = webdriver.Chrome()
#str_url = input()
#driver.get(str_url)
driver.get("https://ap1.pccu.edu.tw/index.asp?user=student")
#登入
account_number = driver.find_element_by_name("Account")
password = driver.find_element_by_name("PassWord")
account_number.send_keys('A7215455')
password.send_keys('7777xxxx')
password.submit()

time.sleep(3)
#移動到我的成績單所在的frame
print(driver.current_url)

iframe = driver.find_element_by_xpath("/html/body/iframe")
driver.switch_to_frame(iframe)
driver.switch_to_frame("downFrame")
driver.switch_to_frame("leftFrame")
#點擊我的成績單
button = driver.find_element_by_xpath('//*[@id="1110"]')
button.click()
#回到預設最外層的frame
driver.switch_to.default_content()
#移動到查詢成績按鈕所在的frame
driver.switch_to_frame(iframe)
driver.switch_to_frame("downFrame")
driver.switch_to_frame("rightFrame")

#點擊查詢

button_select = driver.find_element_by_name("submit")
button_select.click()

#driver.switch_to.parent_frame()

#將html存儲到記憶體
#driver.switch_to.default_content()
html = driver.page_source
#將html的內容存成檔案
file_name = 'test.html'
f = open(file_name,"w")
#save_html(f,driver)
f.write(html)
f.close()

#防止伺服器關閉
str_url = input("完成")