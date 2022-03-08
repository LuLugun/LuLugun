import time
import streamlit as st
import datetime
import numpy as np
import pandas as pd
import pymysql
import os

def sql_connect():
    global db,cursor,host
    host='8.tcp.ngrok.io'
    port = 14092
    user='a11805'
    passwd='pccua11805'
    database='aiot'
    print('Connecting....')
    print('host:%s\nuser:%s\npassword:********\ndatabase:%s\n'%(host,user,database))
    db=pymysql.connect(host=host,user=user,passwd=passwd,database=database,port=port)
    os.system('clear')
    cursor=db.cursor()
    print('Connection succeed')

def select_data(title_name,table_name,number):
    sql = '''SELECT '''+title_name+''' FROM '''+table_name+''' ORDER BY `time` DESC LIMIT '''+number+''';'''
    print(sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    result = pd.DataFrame(result)
    return result

sql_connect()
sensor = select_data('''`time`, `temperature`, `humidity`, `quality_Potted`, `quality_Reservoir`, `luminance`, `CO2`, `Potted`, `Reservoir`, `smoke`''','sensor_all','2016')
sensor.columns=['時間','溫度','濕度','水質(盆栽)','水質(水池)','亮度','CO2','水溫','水溫(水池)','煙霧']


line_time = sensor["時間"]

sensor_all = sensor
sensor_all.drop(columns = '時間',inplace=True)
sensor_all = pd.DataFrame(sensor_all)
sensor_all.set_index(pd.to_datetime(line_time,format="%Y-%m-%d %H:%M:%S"),inplace=True)
line_chart = st.line_chart(sensor_all)

col1, col2  = st.columns(2)
col3, col4  = st.columns(2)
col5, col6  = st.columns(2)
if col1.checkbox('溫度'):
    temperature = sensor['溫度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(line_time,format="%Y-%m-%d %H:%M:%S"),inplace=True)
    line_chart = col1.line_chart(temperature,height = 200,use_container_width = False)
if col2.checkbox('濕度'):
    humidity = sensor['濕度']
    humidity = pd.DataFrame(humidity)
    humidity.set_index(pd.to_datetime(line_time,format="%Y-%m-%d %H:%M:%S"),inplace=True)
    line_chart = col2.line_chart(humidity,height = 200,use_container_width = False)    #折線圖
