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
print(sensor)
line_time = sensor["時間"]
temperature = sensor

temperature.drop(columns = '時間',inplace=True)

temperature = pd.DataFrame(temperature)
temperature.set_index(pd.to_datetime(line_time,format="%Y-%m-%d %H:%M:%S"),inplace=True)

line_chart = st.line_chart(temperature,use_container_width = False)
