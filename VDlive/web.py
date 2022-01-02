import time
import streamlit as st
import numpy as np
import pandas as pd
import datetime
S_volume = []
S_speed = []
M_volume = []
M_speed = []
L_volume = []
L_speed = []
T_volume = []
T_speed = []
local_time = datetime.datetime.now() + datetime.timedelta(minutes=-1)
local_time = local_time.strftime('%Y%m%d_%H_%M')
file_time = datetime.datetime.now() + datetime.timedelta(minutes=-1440)

executions = 0
st.caption('VD-42-0090-162-01 : 3000900116276U')
while executions < 1440:
    try:
        executions = executions+1
        str_time = str(file_time.strftime('%Y%m%d_%H_%M'))
        file_time = file_time + datetime.timedelta(minutes=1)
        vdlive = pd.read_csv(str_time+'VDLiveList.csv')
        file_time = file_time + datetime.timedelta(minutes=1)
        vdlive = vdlive.values
        vdlive = pd.DataFrame(vdlive)
        vdlive.columns = ["vdid", "linkid","laneid","lanetype","speed","occupancy","vehicletype","volume","speed2","status","datacollecttime"]
        linkid_list = vdlive["linkid"]
        speed2_list = vdlive["speed2"]
        volume_list = vdlive["volume"]
        vehicletype_list = vdlive["vehicletype"]
        number = 0
        for i in vdlive["vdid"]:
            if i == 'VD-42-0090-162-01':
                if linkid_list[number] == '3000900116276U':
                    if vehicletype_list[number] == 'S':
                        S_volume.append(volume_list[number])
                        S_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'L':
                        L_volume.append(volume_list[number])
                        L_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'M':
                        M_volume.append(volume_list[number])
                        M_speed.append(speed2_list[number])
                    if vehicletype_list[number] == 'T':
                        T_volume.append(volume_list[number])
                        T_speed.append(speed2_list[number])
            number = number+1
    except FileNotFoundError as e:
        pass

col1, col2 = st.columns(2)
S_volume = pd.DataFrame(S_volume)
S_volume.columns=['S_volume']
col1.line_chart(S_volume,720,90)

S_speed = pd.DataFrame(S_speed)
S_speed.columns=['S_speed']
col2.line_chart(S_speed,720,90)

col1, col2 = st.columns(2)

M_volume = pd.DataFrame(M_volume)
M_volume.columns=['M_volume']
col1.line_chart(M_volume,720,90)

M_speed = pd.DataFrame(M_speed)
M_speed.columns=['M_speed']
col2.line_chart(M_speed,720,90)

col1, col2 = st.columns(2)

L_volume = pd.DataFrame(L_volume)
L_volume.columns=['L_volume']
col1.line_chart(L_volume,720,90)

L_speed = pd.DataFrame(L_speed)
L_speed.columns=['L_speed']
col2.line_chart(L_speed,720,90)

col1, col2 = st.columns(2)

T_volume = pd.DataFrame(T_volume)
T_volume.columns=['T_volume']
col1.line_chart(T_volume,720,90)

T_speed = pd.DataFrame(T_speed)
T_speed.columns=['T_speed']
col2.line_chart(T_speed,720,90)