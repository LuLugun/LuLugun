from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")
driver = webdriver.Chrome(chrome_options = chromeoptions)
f = open('output.csv', 'w', encoding='UTF-8')
driver.get("https://www.319papago.idv.tw/lifeinfo/sinyi/sinyi-02.html")
list_to_csv = []
for i in range(1,158):
    name = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr['+str(i)+']/td[1]')
    name_str = name.get_attribute("textContent")
    number = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr['+str(i)+']/td[2]')
    number_str = number.get_attribute("textContent")
    address = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr['+str(i)+']/td[3]')
    address_str = address.get_attribute("textContent")
    print(name_str,', ',number_str,', ',address_str)
    f.write(name_str+', '+number_str+', '+address_str+'\n')

driver.close()
f.close()