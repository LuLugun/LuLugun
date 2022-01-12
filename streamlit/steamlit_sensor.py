import time
import streamlit as st
import datetime
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show

sensor = pd.read_csv('202112.csv')
sensor=sensor.values
sensor = pd.DataFrame(sensor)
sensor.columns=['時間','溫度','濕度','水質(盆栽)','水質(水池)','亮度','CO2','水溫','水溫(水池)']

col1, col2  = st.columns(2)
col3, col4  = st.columns(2)
col5, col6  = st.columns(2)

if col1.checkbox('溫度'):
    temperature = sensor['溫度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col1.line_chart(temperature,height = 200,use_container_width = False)    #折線圖
        


if col2.checkbox('濕度'):
    temperature = sensor['濕度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col2.line_chart(temperature,height = 200,use_container_width = False)    #折線圖

if col3.checkbox('水質(盆栽)'):
    temperature = sensor['水質(盆栽)']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col3.line_chart(temperature,height = 200,use_container_width = False)    #折線圖

if col4.checkbox('亮度'):
    temperature = sensor['亮度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col4.line_chart(temperature,height = 200,use_container_width = False)    #折線圖

if col5.checkbox('CO2'):
    temperature = sensor['CO2']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col5.line_chart(temperature,height = 200,use_container_width = False)    #折線圖

if col6.checkbox('水溫'):
    temperature = sensor['水溫']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = col6.line_chart(temperature,height = 200,use_container_width = False)    #折線圖




