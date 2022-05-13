from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import os

local_path = os.path.dirname(os.path.abspath(__file__))
local_time = datetime.datetime.now()
comment = str(local_time.strftime('%Y%m%d_%H_%M_%S'))

while True:
    try:
        start = time.perf_counter()
        content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/section/livetrafficdata/LiveTrafficListnew.xml')
        soup = BeautifulSoup(content, "html.parser")
        str_all = soup.prettify()
        if str_all == '':
            quit()
        comment = soup.updatetime.string
        comment = str(comment).replace(' ','').strip().replace('T','_').replace('+08:00','').replace('-','').replace(':','_')
        path = local_path+'//avi_xml//'+comment+'TrafficListnew.xml'          
        f = open(path, 'w')
        f.write(str_all)
        f.close()
        end = time.perf_counter()
        if end-start < 60:
            time.sleep(60-(end-start))
        
    except SystemExit as e:
        pass
    except Exception as e:
        faillog = open('avi_faillog.txt', 'a')
        try:
            comment = datetime.datetime.strptime(comment[0:-3], "%Y%m%d_%H_%M")
            comment = comment + datetime.timedelta(minutes=1)
            comment = str(comment.strftime('%Y%m%d_%H_%M'))
        except:
            local_time = datetime.datetime.now()
            comment = str(local_time.strftime('%Y%m%d_%H_%M'))
        faillog.write(str(e)+':'+comment+'TrafficListnew.xml\n')
        faillog.close()
        print(e,':',comment+'TrafficListnew.xml')
        time.sleep(5)
        pass
