from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
video_links = []

Keyword_input = driver.find_element_by_id("search")
Keyword_input.send_keys('車禍')
search_button = driver.find_element_by_id("search-icon-legacy")
search_button.submit()

time.sleep(3)
while True:
    links = driver.find_elements_by_id("video-title")
    for link in links:
        partial_href = link.get_attribute("href")
        partial_title = link.get_attribute("title")
        print(str(partial_title))
        print(str(partial_href))


        video_links.append(str(partial_href))
    driver.execute_script('var q=document.documentElement.scrollTop=100000')
    time.sleep(5)
    str_url = input()
#print(video_links)

str_url = input()
