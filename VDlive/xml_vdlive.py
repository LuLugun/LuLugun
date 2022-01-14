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
        content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml')
        soup = BeautifulSoup(content, "html.parser")
        comment = soup.vdlivelist.updatetime.string 
        comment = comment.replace(' ','').strip().replace('T','_').replace('+08:00','').replace('-','').replace(':','_')
        path = local_path+'//xml//'+comment+'VDLiveList.xml'
        str_all = soup.prettify()
        if str_all == '':
            quit()            
        f = open(path, 'w')
        f.write(str_all)
        f.close()

        time.sleep(40)
    except SystemExit as e:
        pass
    except Exception as e:
        print(e,':',path)
        time.sleep(5)
        pass
