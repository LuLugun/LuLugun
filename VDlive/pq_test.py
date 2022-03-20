'''https://thbapp.thb.gov.tw/opendata/section/livetrafficdata/LiveTrafficListnew.xml'''
from pyquery import PyQuery as pq
import time
from bs4 import BeautifulSoup
import urllib.request
start = time.perf_counter()
html = pq('https://thbapp.thb.gov.tw/opendata/section/livetrafficdata/LiveTrafficListnew.xml')
print(html)
end = time.perf_counter()
print(end-start)
start = time.perf_counter()
content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml')
soup = BeautifulSoup(content, "html.parser")
print(soup)
end = time.perf_counter()
print(end-start)