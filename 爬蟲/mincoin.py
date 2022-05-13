from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

driver.get("https://www.maicoin.com/market/ETH?invitation_token=ce0fcc72a597d1b89dc077420ccd0301")


while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    virtual_currency = soup.find_all('div', {'class': "css-1dbjc4n r-1awozwy r-13awgt0 r-18u37iz"})
    NT_Amount = soup.find_all('div', {'dir': "auto"},{'class': "css-901oao"})
    now = time.localtime()
    print(now.tm_year,"-",now.tm_mon,"-",now.tm_mday,"   ",now.tm_hour,":",now.tm_min)
    virtual_str = []
    for virtual in virtual_currency:
        name_virtual_currency = virtual.find('div',{'dir':"auto"},{'class':"css-901oao r-1inkyih r-13hce6t r-3s2u2q"})

        if name_virtual_currency:

            virtual_str.append(name_virtual_currency.getText())
            #print(name_virtual_currency.getText())

    nt_str = []
    for nt in NT_Amount:
        post = nt.find('span', {'class': 'css-901oao css-16my406 css-bfa6kz r-1tyxmls r-yy2aun'})
 
        if post:
            nt_str.append(post.getText())

    for i in range(len(nt_str)):
        print(virtual_str[i],"=> NT:",nt_str[i])

    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    time.sleep(100)
    #driver.refresh()
    #time.sleep(5)

driver.quit()