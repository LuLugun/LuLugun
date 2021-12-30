import time
import streamlit as st
import datetime
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show

sensor = pd.read_csv('sensor (1).csv')
sensor=sensor.values
sensor = pd.DataFrame(sensor)
sensor.columns=['時間','溫度','濕度','水質(盆栽)','亮度','二氧化碳濃度','水溫(盆栽)','水溫(水池)']

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

if col1.checkbox('溫度'):
    temperature = sensor['溫度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖
        


if col2.checkbox('濕度'):
    temperature = sensor['濕度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖

if col3.checkbox('水質 (盆栽) '):
    temperature = sensor['水質(盆栽)']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖

if col4.checkbox('亮度'):
    temperature = sensor['亮度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖

if col5.checkbox('二氧化碳濃度'):
    temperature = sensor['二氧化碳濃度']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖

if col6.checkbox('水溫 (盆栽) '):
    temperature = sensor['水溫(盆栽)']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖

if col7.checkbox('水溫 (水池) '):
    temperature = sensor['水溫(水池)']
    temperature = pd.DataFrame(temperature)
    temperature.set_index(pd.to_datetime(sensor["時間"],format="%Y/%m/%d %H:%M"),inplace=True)
    line_chart = st.line_chart(temperature)    #折線圖


