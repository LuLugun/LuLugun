from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import os
import pymysql
import pandas as pd
from pyquery import PyQuery as pq

def get_id_list():
    f = open('etag_ETagPairID.txt','r')
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
    passwd='*****'
    database='*****'
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

def xml_to_csv_dict(updatetime,updateinterval,authoritycode,eTagPairID,startETagStatus,endETagStatus,vehicleType,travelTime,standardDeviation,spaceMeanSpeed,vehicleCount,startTime,endTime,datacollecttime):
    data = {"updatetime": updatetime,
                        "updateinterval": int(str(updateinterval).replace(' ','').strip()),
                        "authoritycode": str(authoritycode).replace(' ','').strip(),
                        "eTagPairID": str(eTagPairID).replace(' ','').strip(),
                        "startETagStatus": str(startETagStatus).replace(' ','').strip(),
                        "endETagStatus": str(endETagStatus).replace(' ','').strip(),
                        "vehicleType": str(vehicleType).replace(' ','').strip(),
                        "travelTime": int(str(travelTime).replace(' ','').strip()),
                        "standardDeviation": int(str(standardDeviation).replace(' ','').strip()),
                        "spaceMeanSpeed": int(str(spaceMeanSpeed).replace(' ','').strip()),
                        "vehicleCount": int(str(vehicleCount).replace(' ','').strip()),
                        "startTime": startTime,
                        "endTime": endTime,
                        "datacollecttime": datacollecttime}
    return data

sql_connect()
etagid_list = get_id_list()
title = ["updatetime","updateinterval","authoritycode","eTagPairID","startETagStatus","endETagStatus","vehicleType","travelTime","standardDeviation","spaceMeanSpeed","vehicleCount","startTime","endTime","datacollecttime"]
while True:
    try:
        start = time.perf_counter()
        xml_to_csv = []

        html_pq = pq('https://thbapp.thb.gov.tw/opendata/etagpair/five/ETagPairLive.xml')
        updatetime = html_pq('UpdateTime').text()
        updatetime = str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00','')
        updatetime = datetime.datetime.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
        updateinterval = html_pq('UpdateInterval').text()
        authoritycode = html_pq('AuthorityCode').text()


        ETagPairID_list = [i.text().replace(' ','').strip() for i in html_pq.items('ETagPairID')]
        StartETagStatus_list = [i.text().replace(' ','').strip() for i in html_pq.items('StartETagStatus')]
        EndETagStatus_list = [i.text().replace(' ','').strip() for i in html_pq.items('EndETagStatus')]

        VehicleType_list = [i.text().replace(' ','').strip() for i in html_pq.items('VehicleType')]
        TravelTime_list = [i.text().replace(' ','').strip() for i in html_pq.items('TravelTime')]
        StandardDeviation_list = [i.text().replace(' ','').strip() for i in html_pq.items('StandardDeviation')]
        SpaceMeanSpeed_list = [i.text().replace(' ','').strip() for i in html_pq.items('SpaceMeanSpeed')]
        VehicleCount_list = [i.text().replace(' ','').strip() for i in html_pq.items('VehicleCount')]

        StartTime_list = [datetime.datetime.strptime(i.text().replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000',''), "%Y-%m-%d %H:%M:%S") for i in html_pq.items('StartTime')]
        EndTime_list = [datetime.datetime.strptime(i.text().replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000',''), "%Y-%m-%d %H:%M:%S") for i in html_pq.items('EndTime')]
        datacollecttime_list = [datetime.datetime.strptime(i.text().replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000',''), "%Y-%m-%d %H:%M:%S") for i in html_pq.items('DataCollectTime')]

        for i in range(len(ETagPairID_list)):
            ETagPairID = ETagPairID_list[i]
            #print(ETagPairID,etagid_list)
            if str(ETagPairID) in etagid_list:
                print(updatetime,ETagPairID,etagid_list)
                StartETagStatus = StartETagStatus_list[i]
                EndETagStatus = EndETagStatus_list[i]
                VehicleType = VehicleType_list[i]
                TravelTime = TravelTime_list[i]
                StandardDeviation = StandardDeviation_list[i]
                SpaceMeanSpeed = SpaceMeanSpeed_list[i]
                VehicleCount = VehicleCount_list[i]
                StartTime = StartTime_list[i]
                EndTime = EndTime_list[i]
                datacollecttime = datacollecttime_list[i]

                xml_to_csv.append(xml_to_csv_dict(updatetime,updateinterval,authoritycode,ETagPairID,StartETagStatus,EndETagStatus,VehicleType,TravelTime,StandardDeviation,SpaceMeanSpeed,VehicleCount,StartTime,EndTime,datacollecttime))
        df = pd.DataFrame(xml_to_csv, columns=title)
        #print(df)
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        for i,row in df.iterrows():

            sql = "INSERT INTO `thb_etag` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
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
        faillog = open('E:\\交通部資料\\db_ETAG_faillog.txt', 'a')
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
    


