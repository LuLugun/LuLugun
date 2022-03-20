from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import os
import pymysql
import pandas as pd
from pyquery import PyQuery as pq

def get_id_list():
    f = open('commits_avifile.txt','r')
    commits_list = f.readlines()
    f.close()
    id_list = []
    for i in commits_list:
        id_list.append(i.replace('\n',''))
    return id_list

def sql_connect():
    global db,cursor,host
    host='localhost'
    user='root'
    passwd='syscom'
    database='syscom'
    print('連線中....')
    print('host:%s\nuser:%s\npassword:********\ndatabase:%s\n'%(host,user,database))
    try:
        db=pymysql.connect(host=host,user=user,passwd=passwd,database=database)
        os.system('cls')
        print('連線成功')
        cursor=db.cursor()
        return True
    except pymysql.Error as e:
        print("連線失敗:"+str(e))
        return False
    
def xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime):
    data = {"updatetime": updatetime,
                        "updateinterval": int(str(updateinterval).replace(' ','').strip()),
                        "authoritycode": str(authoritycode).replace(' ','').strip(),
                        "sectionid": str(sectionid).replace(' ','').strip(),
                        "traveltime": int(str(traveltime).replace(' ','').strip()),
                        "travelspeed": int(str(travelspeed).replace(' ','').strip()),
                        "congestionlevelid": str(congestionlevelid).replace(' ','').strip(),
                        "congestionlevel": str(congestionlevel).replace(' ','').strip(),
                        "hashistorical": str(hashistorical).replace(' ','').strip(),
                        "hasvd": str(hasvd).replace(' ','').strip(),
                        "hasavi": str(hasavi).replace(' ','').strip(),
                        "hasetag": str(hasetag).replace(' ','').strip(),
                        "hasgvp": str(hasgvp).replace(' ','').strip(),
                        "hascvp": str(hascvp).replace(' ','').strip(),
                        "hasothers": str(hasothers).replace(' ','').strip(),
                        "datacollecttime": datacollecttime}
    return data


sql_connect()
aviid_list = get_id_list()
title = ["updatetime","updateinterval","authoritycode","sectionid", "traveltime","travelspeed","congestionlevelid","congestionlevel","hashistorical","hasvd","hasavi","hasetag","hasgvp","hascvp","hasothers","datacollecttime"]

while True:
    try:
        start = time.perf_counter()
        xml_to_csv = []

        html_pq = pq('https://thbapp.thb.gov.tw/opendata/section/livetrafficdata/LiveTrafficListnew.xml')
        updatetime = html_pq('UpdateTime').text()
        updatetime = str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00','')
        updatetime = datetime.datetime.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
        updateinterval = html_pq('UpdateInterval').text()
        authoritycode = html_pq('AuthorityCode').text()
        #print(updatetime,updateinterval,authoritycode)

        sectionid_list = [i.text().replace(' ','').strip() for i in html_pq.items('sectionid')]
        traveltime_list = [i.text() for i in html_pq.items('traveltime')]
        travelspeed_list = [i.text() for i in html_pq.items('travelspeed')]
        congestionlevelid_list = [i.text() for i in html_pq.items('congestionlevelid')]
        congestionlevel_list = [i.text() for i in html_pq.items('congestionlevel')]
        hashistorical_list = [i.text() for i in html_pq.items('hashistorical')]
        hasvd_list = [i.text() for i in html_pq.items('hasvd')]
        hasavi_list = [i.text() for i in html_pq.items('hasavi')]
        hasetag_list = [i.text() for i in html_pq.items('hasetag')]
        hasgvp_list = [i.text() for i in html_pq.items('hasgvp')]
        hascvp_list = [i.text() for i in html_pq.items('hascvp')]
        hasothers_list = [i.text() for i in html_pq.items('hasothers')]
        datacollecttime_list = [datetime.datetime.strptime(i.text().replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000',''), "%Y-%m-%d %H:%M:%S") for i in html_pq.items('datacollecttime')]

        for i in range(len(sectionid_list)):
            sectionid = sectionid_list[i]
            if sectionid in aviid_list:
                traveltime = traveltime_list[i]
                travelspeed = travelspeed_list[i]
                congestionlevelid = congestionlevelid_list[i]
                congestionlevel = congestionlevel_list[i]
                hashistorical = hashistorical_list[i]
                hasvd = hasvd_list[i]
                hasavi = hasavi_list[i]
                hasetag = hasetag_list[i]
                hasgvp = hasgvp_list[i]
                hascvp = hascvp_list[i]
                hasothers = hasothers_list[i]
                datacollecttime = datacollecttime_list[i]
                xml_to_csv.append(xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime))
        df = pd.DataFrame(xml_to_csv, columns=title)
        #print(df)
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        for i,row in df.iterrows():

            sql = "INSERT INTO `thb_section` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            #print(sql, tuple(row))
            cursor.execute(sql, tuple(row))
            db.commit()    

        end = time.perf_counter()
        #print(end-start)
        if end-start < 60:
            time.sleep(60-(end-start))
        
    except SystemExit as e:
        pass
    except Exception as e:
        faillog = open('db_avi_faillog.txt', 'a')
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
        time.sleep(2)
        pass
