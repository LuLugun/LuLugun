import pymysql
import os
import untangle
import pandas as pd
import datetime


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

def get_id_list():
    f = open('commits_avifile.txt','r')
    commits_list = f.readlines()
    f.close()
    id_list = []
    for i in commits_list:
        id_list.append(i.replace('\n',''))
    return id_list
    
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
#mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")
local_path = os.path.dirname(os.path.abspath(__file__))
mypath = local_path+'//avi_xml'
title = ["updatetime","updateinterval","authoritycode","sectionid", "traveltime","travelspeed","congestionlevelid","congestionlevel","hashistorical","hasvd","hasavi","hasetag","hasgvp","hascvp","hasothers","datacollecttime"]
files = os.listdir(mypath)
for i in files:
    try:
        xml = untangle.parse(mypath+ "\\" + str(i))
        xml_to_csv = []
        updatetime = xml.livetrafficlist.updatetime.cdata
        updatetime = str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00','')
        updatetime = datetime.datetime.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
        updateinterval = xml.livetrafficlist.updateinterval.cdata
        authoritycode = xml.livetrafficlist.authoritycode.cdata
        for html in xml.livetrafficlist.livetraffics.livetraffic:
            sectionid = html.sectionid.cdata
            sectionid = str(sectionid).replace(' ','').strip()
            traveltime = html.traveltime.cdata
            travelspeed = html.travelspeed.cdata
            congestionlevelid = html.congestionlevelid.cdata
            congestionlevel = html.congestionlevel.cdata

            hashistorical = html.datasources.hashistorical.cdata
            hasvd = html.datasources.hasvd.cdata
            hasavi = html.datasources.hasavi.cdata
            hasetag = html.datasources.hasetag.cdata
            hasgvp = html.datasources.hasgvp.cdata
            hascvp = html.datasources.hascvp.cdata
            hasothers = html.datasources.hasothers.cdata
            datacollecttime = html.datacollecttime.cdata
            datacollecttime = str(datacollecttime).replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000','')
            datacollecttime = datetime.datetime.strptime(datacollecttime, "%Y-%m-%d %H:%M:%S")
            if sectionid in aviid_list:
                xml_to_csv.append(xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime))
        df = pd.DataFrame(xml_to_csv, columns=title)
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        print(i)
        for i,row in df.iterrows():

            sql = "INSERT INTO `thb_section` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            #print(sql, tuple(row))
            cursor.execute(sql, tuple(row))
            db.commit()

    except Exception as e:
        print(e,':',i)
        pass
db.close() 