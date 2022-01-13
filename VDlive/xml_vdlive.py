from bs4 import BeautifulSoup
import urllib.request
import xml.etree.ElementTree as Xet
import pandas as pd
import time
import datetime
import untangle, csv
import os

local_path = os.path.dirname(os.path.abspath(__file__))
while True:
    try:
        local_time = datetime.datetime.now()
        local_time = str(local_time.strftime('%Y%m%d_%H_%M'))
        path = local_path+'//xml//'+local_time+'VDLiveList.xml'
        content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml')
        soup = BeautifulSoup(content, "html.parser")
        str_all = soup.prettify()
        if str_all == '':
            quit()            
        f = open(path, 'w')
        f.write(str_all)
        f.close()

        time.sleep(60)
    except SystemExit as e:
        pass
    except Exception as e:
        print(e,':',path)
        time.sleep(5)
        pass
