import os
import datetime
import pandas as pd
import untangle
import pymysql

def get_id_list(commits_path):
    f = open(commits_path,'r')
    commits_list = f.readlines()
    f.close()
    id_list = []
    for i in commits_list:
        id_list.append(i.replace('\n',''))
    return id_list
    
def vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime):
    data = {"updatetime": str(updatetime).replace(' ','').strip().replace('T',' ').replace('+08:00',''),
                        "vdid": str(vdid).replace(' ','').strip(),
                        "linkid": str(linkid).replace(' ','').strip(),
                        "laneid": str(laneid).replace(' ','').strip(),
                        "lanetype": str(lanetype).replace(' ','').strip(),
                        "speed": str(speed).replace(' ','').strip(),
                        "occupancy": str(occupancy).replace(' ','').strip(),
                        "vehicletype": str(vehicletype).replace(' ','').strip(),
                        "volume": str(volume).replace(' ','').strip(),
                        "speed2": str(speed2).replace(' ','').strip(),
                        "status": str(status).replace(' ','').strip(),
                        "datacollecttime": str(datacollecttime).replace(' ','').strip().replace('T',' ').replace('+08:00','').replace('.000','')}
    return data

def vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime):
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

def avi_xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime):
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

def avi_xml_to_db_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime):
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
    
def sql_connect(host,user,passwd,database):
    global db,cursor
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

def vd_xml_to_csv():
    local_path = os.path.dirname(os.path.abspath(__file__))
    try:
        vdid_list = get_id_list('commits_file.txt')
    except:
        commits_path = input('請輸入commits file完整路徑:')
        vdid_list = get_id_list(commits_path)
    try:
        os.mkdir('vd_csv')
    except FileExistsError as e:
        pass
    mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")
    title = ["updatetime","vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
    files = os.listdir(mypath)
    for i in files:
        try:
            xml = untangle.parse(mypath+ "\\" + str(i))
            xml_to_csv = []
            updatetime = xml.vdlivelist.updatetime.cdata
            for html in xml.vdlivelist.vdlives.vdlive:
                vdid = html.vdid.cdata
                vdid = str(vdid).replace(' ','').strip()
                try:
                    status = html.status.cdata
                except:
                    status = ''
                try:
                    datacollecttime = html.datacollecttime.cdata
                except:
                    datacollecttime = ''
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
                                xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html.linkflows.linkflow.lanes.lane.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if vdid in vdid_list:
                                    xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))
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
                                    xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_laneid.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if vdid in vdid_list:
                                        xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))
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
                                    xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_linkid.lanes.lane.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if vdid in vdid_list:
                                        xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                                        xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                                except:
                                    for html_vehicle in html_laneid.vehicles.vehicle:
                                        vehicletype = html_vehicle.vehicletype.cdata
                                        volume = html_vehicle.volume.cdata
                                        try:
                                            speed2 = html_vehicle.speed.cdata
                                        except AttributeError as e:
                                            speed2 = ""
                                        if vdid in vdid_list:
                                            xml_to_csv.append(vd_xml_to_csv_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))
            df = pd.DataFrame(xml_to_csv, columns=title) 
        
            df.to_csv(local_path+'\\vd_csv\\'+str(i).replace('xml','csv'), index = False)
            print(str(i).replace('xml','csv'))
        except Exception as e:
            print(e,':',i)
            pass

def vd_check_file():
    mypath = input('請輸入檔案路徑:')
    files = os.listdir(mypath)
    start_time = files[0].replace('VDLiveList.xml','')
    start_time = datetime.datetime.strptime(start_time[0:-3], "%Y%m%d_%H_%M")
    print('start:',start_time)
    f = open('lose_file.txt', 'w')

    for file in files:
        file = file.replace('VDLiveList.xml','')
        try:
            file = datetime.datetime.strptime(file[0:-3], "%Y%m%d_%H_%M")
            if file == start_time:
                start_time = start_time + datetime.timedelta(minutes=1)
            else:
                while True:
                    if file == start_time:
                        start_time = start_time + datetime.timedelta(minutes=1)
                        break
                    print('lose:',start_time)
                    start_time_str = datetime.datetime.strftime(start_time, "%Y%m%d_%H_%M")
                    f.write(start_time_str+'\n')
                    start_time = start_time + datetime.timedelta(minutes=1)
        except Exception as e:
            print(e,':',file)
            pass
    f.close()

def vd_updata_to_db():
    try:    
        vdid_list = get_id_list('commits_file.txt')
    except:
        commits_path = input('請輸入commits file完整路徑:')
        vdid_list = get_id_list(commits_path)
    mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")
    title = ["updatetime","vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
    files = os.listdir(mypath)
    for i in files:
        try:
            xml = untangle.parse(mypath+ "\\" + str(i))
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
                                xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html.linkflows.linkflow.lanes.lane.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if vdid in vdid_list:
                                    xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                                    xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_laneid.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if vdid in vdid_list:
                                        xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                                    xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_linkid.lanes.lane.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if vdid in vdid_list:
                                        xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                                        xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                                except:
                                    for html_vehicle in html_laneid.vehicles.vehicle:
                                        vehicletype = html_vehicle.vehicletype.cdata
                                        volume = html_vehicle.volume.cdata
                                        try:
                                            speed2 = html_vehicle.speed.cdata
                                        except AttributeError as e:
                                            speed2 = ""
                                        if vdid in vdid_list:
                                            xml_to_csv.append(vd_xml_to_db_dict(updatetime,vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

            df = pd.DataFrame(xml_to_csv, columns=title) 
            cols = "`,`".join([str(i) for i in df.columns.tolist()])
            print(i)
            for i,row in df.iterrows():

                sql = "INSERT INTO `vdlive` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                #print(sql, tuple(row))
                cursor.execute(sql, tuple(row))
                db.commit()
        except Exception as e:
            print(e,':',i)
            pass
    db.close() 

def avi_check_file():
    mypath = input('請輸入檔案路徑:')
    files = os.listdir(mypath)
    start_time = files[0].replace('TrafficListnew.xml','')
    start_time = datetime.datetime.strptime(start_time[0:-3], "%Y%m%d_%H_%M")
    print('start:',start_time)
    f = open('lose_file.txt', 'w')

    for file in files:
        file = file.replace('TrafficListnew.xml','')
        try:
            file = datetime.datetime.strptime(file[0:-3], "%Y%m%d_%H_%M")
            if file == start_time:
                start_time = start_time + datetime.timedelta(minutes=1)
            else:
                while True:
                    if file == start_time:
                        start_time = start_time + datetime.timedelta(minutes=1)
                        break
                    print('lose:',start_time)
                    start_time_str = datetime.datetime.strftime(start_time, "%Y%m%d_%H_%M")
                    f.write(start_time_str+'\n')
                    start_time = start_time + datetime.timedelta(minutes=1)
        except Exception as e:
            print(e,':',file)
            pass
    f.close()

def avi_xml_to_csv():
    local_path = os.path.dirname(os.path.abspath(__file__))
    try:
        aviid_list = get_id_list('commits_avifile.txt')
    except:
        commits_path = input('請輸入commits file完整路徑:')
        aviid_list = get_id_list(commits_path)
    try:
        os.mkdir('avi_csv')
    except FileExistsError as e:
        pass
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
                    xml_to_csv.append(avi_xml_to_csv_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime))

            df = pd.DataFrame(xml_to_csv, columns=title) 
            
            df.to_csv(local_path+'\\avi_csv\\'+str(i).replace('xml','csv'), index = False)
            print(str(i).replace('xml','csv'))
        except Exception as e:
            print(e,':',i)
            pass

def avi_updata_to_db():
    try:
        aviid_list = get_id_list('commits_avifile.txt')
    except:
        commits_path = input('請輸入commits file完整路徑:')
        aviid_list = get_id_list(commits_path)
    mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")
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
                    xml_to_csv.append(avi_xml_to_db_dict(updatetime,updateinterval,authoritycode,sectionid,traveltime,travelspeed,congestionlevelid,congestionlevel,hashistorical,hasvd,hasavi,hasetag,hasgvp,hascvp,hasothers,datacollecttime))
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

if __name__ == '__main__':
    while True:
        print('(1) vd\n(2) avi\n(-1) 離開')
        vd_or_avi = input('請輸入選項:')
        if vd_or_avi == '1' :
            print('(1) 將xml轉csv\n(2) 檢查缺漏的xml\n(3) 將xml上傳DB\n輸入任意離開')
            vd_choose = input('請輸入選項:')
            if vd_choose== '1':
                vd_xml_to_csv()
            if vd_choose== '2':
                vd_check_file()
            if vd_choose== '3':
                host = input('host:')
                user = input('user:')
                passwd = input('passwd:')
                database = input('database:')
                if sql_connect(host,user,passwd,database) == True:
                    vd_updata_to_db()
        if vd_or_avi == '2' :
            print('(1) 將xml轉csv\n(2) 檢查缺漏的xml\n(3) 將xml上傳DB\n輸入任意離開')
            avi_choose = input('請輸入選項:')
            if avi_choose == '1':
                avi_xml_to_csv()
            if avi_choose == '2':
                avi_check_file()
            if avi_choose == '3':
                host = input('host:')
                user = input('user:')
                passwd = input('passwd:')
                database = input('database:')
                if sql_connect(host,user,passwd,database) == True:
                    avi_updata_to_db()
        if vd_or_avi == '-1' :
            break
