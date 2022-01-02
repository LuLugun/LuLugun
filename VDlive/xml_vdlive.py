from bs4 import BeautifulSoup
import urllib.request
import time
import datetime

while True:
    try:
        local_time = datetime.datetime.now()
        local_time = str(local_time.strftime('%Y%m%d_%H_%M'))
        path = local_time+'VDLiveList.xml'
        content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml')
        soup = BeautifulSoup(content)
        str_all = soup.prettify()
        f = open(path, 'w')
        f.write(str_all)
        f.close()

        time.sleep(60)
    except:
        print(path)
        pass
