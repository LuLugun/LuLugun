import xml.etree.ElementTree as Xet
import pandas as pd
import untangle
import os 

def get_id_list():
    f = open('commits_avifile.txt','r')
    commits_list = f.readlines()
    f.close()
    id_list = []
    for i in commits_list:
        id_list.append(i.replace('\n',''))
    return id_list
    
def xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime):
    data = {"updatetime": str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00',''),
                        "updateinterval": str(updateinterval).replace(' ','').strip(),
                        "authoritycode": str(authoritycode).replace(' ','').strip(),
                        "sectionid": str(sectionid).replace(' ','').strip(),
                        "traveltime": str(traveltime).replace(' ','').strip(),
                        "travelspeed": str(travelspeed).replace(' ','').strip(),
                        "congestionlevelid": str(congestionlevelid).replace(' ','').strip(),
                        "congestionlevel": str(congestionlevel).replace(' ','').strip(),
                        "hashistorical": str(hashistorical).replace(' ','').strip(),
                        "hasvd": str(hasvd).replace(' ','').strip(),
                        "hasavi": str(hasavi).replace(' ','').strip(),
                        "hasetag": str(hasetag).replace(' ','').strip(),
                        "hasgvp": str(hasgvp).replace(' ','').strip(),
                        "hascvp": str(hascvp).replace(' ','').strip(),
                        "hasothers": str(hasothers).replace(' ','').strip(),
                        "datacollecttime": str(datacollecttime).replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000','')}
    return data

aviid_list = get_id_list()
mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")
title = ["updatetime","updateinterval","authoritycode","sectionid", "traveltime","travelspeed","congestionlevelid","congestionlevel","hashistorical","hasvd","hasavi","hasetag","hasgvp","hascvp","hasothers","datacollecttime"]
files = os.listdir(mypath)
for i in files:
    try:
        xml = untangle.parse(mypath+ "\\" + str(i))
        xml_to_csv = []
        updatetime = xml.livetrafficlist.updatetime.cdata
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
            if sectionid in aviid_list:
                xml_to_csv.append(xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime))

        df = pd.DataFrame(xml_to_csv, columns=title) 
        
        df.to_csv(str(i).replace('xml','csv'), index = False)
        print(str(i).replace('xml','csv'))
    except Exception as e:
        print(e,':',i)
        pass

