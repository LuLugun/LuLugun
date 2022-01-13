import xml.etree.ElementTree as Xet
import pandas as pd
import time
import datetime
import untangle, csv
import os 
linkid_list = ['3000900115387U', '3000900116276U', '3000900116579U', '3000900117023U', '3000900117598U', '3000900117886U']
def xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime):
    data = {"vdid": str(vdid).replace(' ','').strip(),
                        "linkid": str(linkid).replace(' ','').strip(),
                        "laneid": str(laneid).replace(' ','').strip(),
                        "lanetype": str(lanetype).replace(' ','').strip(),
                        "speed": str(speed).replace(' ','').strip(),
                        "occupancy": str(occupancy).replace(' ','').strip(),
                        "vehicletype": str(vehicletype).replace(' ','').strip(),
                        "volume": str(volume).replace(' ','').strip(),
                        "speed2": str(speed2).replace(' ','').strip(),
                        "status": str(status).replace(' ','').strip(),
                        "datacollecttime": str(datacollecttime).replace(' ','').strip().replace('T',' ').replace('+08:00','')}
    return data

mypath = input("請輸入xml資料夾路徑(ex:D:\VDlive):")

files = os.listdir(mypath)
for i in files:
    try:
        xml = untangle.parse(mypath+ "\\" + str(i))
    
        title = ["vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
        xml_to_csv = []
        for html in xml.vdlivelist.vdlives.vdlive:
            vdid = html.vdid.cdata
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
                        if linkid in linkid_list:
                            xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                    except:
                        for html_vehicle in html.linkflows.linkflow.lanes.lane.vehicles.vehicle:
                            vehicletype = html_vehicle.vehicletype.cdata
                            volume = html_vehicle.volume.cdata
                            try:
                                speed2 = html_vehicle.speed.cdata
                            except AttributeError as e:
                                speed2 = ""
                            if linkid in linkid_list:
                                xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                            if linkid in linkid_list:
                                xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html_laneid.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if linkid in linkid_list:
                                    xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                            if linkid in linkid_list:    
                                xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                        except:
                            for html_vehicle in html_linkid.lanes.lane.vehicles.vehicle:
                                vehicletype = html_vehicle.vehicletype.cdata
                                volume = html_vehicle.volume.cdata
                                try:
                                    speed2 = html_vehicle.speed.cdata
                                except AttributeError as e:
                                    speed2 = ""
                                if linkid in linkid_list:
                                    xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

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
                                if linkid in linkid_list:
                                    xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

                            except:
                                for html_vehicle in html_laneid.vehicles.vehicle:
                                    vehicletype = html_vehicle.vehicletype.cdata
                                    volume = html_vehicle.volume.cdata
                                    try:
                                        speed2 = html_vehicle.speed.cdata
                                    except AttributeError as e:
                                        speed2 = ""
                                    if linkid in linkid_list:
                                        xml_to_csv.append(xml_to_csv_dict(vdid,linkid,laneid,lanetype,speed,occupancy,vehicletype,volume,speed2,status,datacollecttime))

        df = pd.DataFrame(xml_to_csv, columns=title) 
        
        df.to_csv(str(i).replace('xml','csv'), index = False)
        print(str(i).replace('xml','csv'))
    except Exception as e:
        print(e,':',i)
        pass