from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import os
import pandas as pd
import untangle
import pymysql

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

def get_id_list():
    f = open('commits_file.txt','r')
    commits_list = f.readlines()
    f.close()
    id_list = []
    for i in commits_list:
        id_list.append(i.replace('\n',''))
    return id_list

def xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime):
    data = {"updatetime": updatetime,
                        "vdid": str(vdid).replace(' ','').strip(),
                        "linkid": str(linkid).replace(' ','').strip(),
                        "laneid": str(laneid).replace(' ','').strip(),
                        "lanetype": str(lanetype).replace(' ','').strip(),
                        "speed": float(str(speed).replace(' ','').strip()),
                        "occupancy": float(str(occupancy).replace(' ','').strip()),
                        "vehicletype": str(vehicletype).replace(' ','').strip(),
                        "volume": float(str(volume).replace(' ','').strip()),
                        "speed2": float(str(speed2).replace(' ','').strip()),
                        "status": str(status).replace(' ','').strip(),
                        "datacollecttime": datacollecttime}
    return data


local_path = os.path.dirname(os.path.abspath(__file__))
local_time = datetime.datetime.now()
comment = str(local_time.strftime('%Y%m%d_%H_%M_%S'))

vdid_list = get_id_list()
sql_connect()
title = ["updatetime","vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
while True:
    try:
        start = time.perf_counter()
        content = urllib.request.urlopen('https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml')
        soup = BeautifulSoup(content, "html.parser")
        str_all = soup.prettify()
        if str_all == '':
            quit()
        path = 'VDLiveList.xml'            
        f = open(path, 'w')
        f.write(str_all)
        f.close()
        xml = untangle.parse(path)
        xml_to_csv = []
        updatetime = xml.vdlivelist.updatetime.cdata
        updatetime = str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00','')
        updatetime = datetime.datetime.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
        for html in xml.vdlivelist.vdlives.vdlive:
            vdid = html.vdid.cdata
            vdid = str(vdid).replace(' ','').strip()
            try:
                status = html.status.cdata
            except:
                status = ''
            try:
                datacollecttime = html.datacollecttime.cdata
                datacollecttime = str(datacollecttime).replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000','')
                datacollecttime = datetime.datetime.strptime(datacollecttime, "%Y-%m-%d %H:%M:%S")
            except:
                datacollecttime = updatetime
            try:
                linkid = html.linkflows.linkflow.linkid.cdata
                linkid = str(linkid).replace(' ','').strip()
                try:
                    laneid = html.linkflows.linkflow.lanes.lane.laneid.cdata  # 有多個laneid
                    lanetype = html.linkflows.linkflow.lanes.lane.lanetype.cdata
                    speed = html.linkflows.linkflow.lanes.lane.speed.cdata
                    occupancy = html.linkflows.linkflow.lanes.lane.occupancy.cdata
                    try:
                        vehicletype = html.linkflows.linkflow.lanes.lane.vehicles.vehicle.vehicletype.cdata  # 有多個vehicletype
                        volume = html.linkflows.linkflow.lanes.lane.vehicles.vehicle.volume.cdata
                        try:
                            speed2 = html.linkflows.linkflow.lanes.lane.vehicles.vehicle.speed.cdata
                        except AttributeError as e:
                            speed2 = ""
                        if vdid in vdid_list:
                            xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                    except:
                        for html_vehicle in html.linkflows.linkflow.lanes.lane.vehicles.vehicle:
                            vehicletype = html_vehicle.vehicletype.cdata
                            volume = html_vehicle.volume.cdata
                            try:
                                speed2 = html_vehicle.speed.cdata
                            except AttributeError as e:
                                speed2 = ""
                            if vdid in vdid_list:
                                xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                except:
                    for html_laneid in html.linkflows.linkflow.lanes.lane:
                        laneid = html_laneid.laneid.cdata
                        lanetype = html_laneid.lanetype.cdata
                        speed = html_laneid.speed.cdata
                        occupancy = html_laneid.occupancy.cdata
                        try:
                            vehicletype = html_laneid.vehicles.vehicle.vehicletype.cdata
                            volume = html_laneid.vehicles.vehicle.volume.cdata
                            try:
                                speed2 = html_laneid.vehicles.vehicle.speed.cdata
                            except AttributeError as e:
                                speed2 = ""
                            if vdid in vdid_list:
                                xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html_laneid.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if vdid in vdid_list:
                                    xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

            except:
                for html_linkid in html.linkflows.linkflow:
                    linkid = html_linkid.linkid.cdata
                    linkid = str(linkid).replace(' ','').strip()
                    try:
                        laneid = html_linkid.lanes.lane.laneid.cdata
                        lanetype = html_linkid.lanes.lane.lanetype.cdata
                        speed = html_linkid.lanes.lane.speed.cdata
                        occupancy = html_linkid.lanes.lane.occupancy.cdata
                        try:
                            vehicletype = html_linkid.lanes.lane.vehicles.vehicle.vehicletype.cdata
                            volume = html_linkid.lanes.lane.vehicles.vehicle.volume.cdata
                            try:
                                speed2 = html_linkid.lanes.lane.vehicles.vehicle.speed.cdata
                            except AttributeError as e:
                                speed2 = ""
                            if vdid in vdid_list:    
                                xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html_linkid.lanes.lane.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if vdid in vdid_list:
                                    xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                    except:
                        for html_laneid in html_linkid.lanes.lane:
                            laneid = html_laneid.laneid.cdata
                            lanetype = html_laneid.lanetype.cdata
                            speed = html_laneid.speed.cdata
                            occupancy = html_laneid.occupancy.cdata
                            try:
                                vehicletype = html_laneid.vehicles.vehicle.vehicletype.cdata
                                volume = html_laneid.vehicles.vehicle.volume.cdata
                                try:
                                    speed2 = html_laneid.vehicles.vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if vdid in vdid_list:
                                    xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_laneid.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if vdid in vdid_list:
                                        xml_to_csv.append(xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

        df = pd.DataFrame(xml_to_csv, columns=title) 
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        for i,row in df.iterrows():

            sql = "INSERT INTO `vdlive` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            #print(sql, tuple(row))
            cursor.execute(sql, tuple(row))
            db.commit()
        end = time.perf_counter()
        if end-start < 60:
            time.sleep(60-(end-start))

    except SystemExit as e:
        pass
    except Exception as e:
        faillog = open('db_vd_faillog.txt', 'a')
        try:
            comment = datetime.datetime.strptime(comment[0:-3], "%Y%m%d_%H_%M")
            comment = comment + datetime.timedelta(minutes=1)
            comment = str(comment.strftime('%Y%m%d_%H_%M'))
        except:
            local_time = datetime.datetime.now()
            comment = str(local_time.strftime('%Y%m%d_%H_%M'))
        faillog.write(str(e)+':'+comment+'VDLiveList.xml\n')
        faillog.close()
        print(e,':',comment+'VDLiveList.xml')
        time.sleep(5)
        pass
