import streamlit as st
import pandas as pd
import os
from datetime import datetime
S_volume = []
S_speed = []
M_volume = []
M_speed = []
L_volume = []
L_speed = []
T_volume = []
T_speed = []
S_datacollecttime = []
M_datacollecttime = []
L_datacollecttime = []
T_datacollecttime = []
files = os.listdir('LuLugun/VDlive/20220102/)
executions = 0


st.caption('VD-42-0090-162-01 : 3000900116276U')
for i in files:
    st.caption(str(i))
    try:
        vdlive = pd.read_csv(str(i))
        vdlive = vdlive.values
        vdlive = pd.DataFrame(vdlive)
        vdlive.columns = ["vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
        linkid_list = vdlive["linkid"]
        speed2_list = vdlive["speed2"]
        volume_list = vdlive["volume"]
        vehicletype_list = vdlive["vehicletype"]
        datacollecttime_list = vdlive["datacollecttime"]
        number = 0
        for i in vdlive["vdid"]:
            if i == 'VD-42-0090-162-01':
                if linkid_list[number] == '3000900116276U':
                    if vehicletype_list[number] == 'S':
                        S_datacollecttime.append(datacollecttime_list[number])
                        S_volume.append(volume_list[number])
                        S_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'L':
                        L_datacollecttime.append(datacollecttime_list[number])
                        L_volume.append(volume_list[number])
                        L_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'M':
                        M_datacollecttime.append(datacollecttime_list[number])
                        M_volume.append(volume_list[number])
                        M_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'T':
                        T_datacollecttime.append(datacollecttime_list[number])
                        T_volume.append(volume_list[number])
                        T_speed.append(speed2_list[number])
                    
            number = number+1
    except FileNotFoundError as e:
        pass
    except:
        pass

M_volume = pd.DataFrame(M_volume)
M_volume.columns=['M_volume']
M_volume.set_index(pd.to_datetime(M_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(M_volume)

M_speed = pd.DataFrame(M_speed)
M_speed.columns=['M_speed']
M_speed.set_index(pd.to_datetime(M_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(M_speed)

S_volume = pd.DataFrame(S_volume)
S_volume.columns=['S_volume']
S_volume.set_index(pd.to_datetime(S_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(S_volume)

S_speed = pd.DataFrame(S_speed)
S_speed.columns=['S_speed']
S_speed.set_index(pd.to_datetime(S_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(S_speed)

L_volume = pd.DataFrame(L_volume)
L_volume.columns=['L_volume']
L_volume.set_index(pd.to_datetime(L_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(L_volume)

L_speed = pd.DataFrame(L_speed)
L_speed.columns=['L_speed']
L_speed.set_index(pd.to_datetime(L_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(L_speed)

T_volume = pd.DataFrame(T_volume)
T_volume.columns=['T_volume']
T_volume.set_index(pd.to_datetime(L_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(T_volume)

T_speed = pd.DataFrame(T_speed)
T_speed.columns=['T_speed']
T_speed.set_index(pd.to_datetime(T_datacollecttime,format="%Y-%m-%d %H:%M:%S"),inplace=True)
st.line_chart(T_speed)
