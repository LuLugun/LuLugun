from time import strftime
import csv
import pymysql
import pandas as pd
import os
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import matplotlib.ticker as mticker
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as md
import pyimgur

import matplotlib.transforms as transforms
from matplotlib.ticker import MaxNLocator

color=['none','green','blue','yellow','black','red','cyan','violet','pink']
def jpg_to_url(a):
    client_id = "d71e4a049aa4219"
    client_secret = '8205a0eedeaaed605421c765665f70294d39da9f'
    api = pyimgur.Imgur(client_id,client_secret)
    path = a
    upload_image = api.upload_image(path)
    os.remove(path)
    return upload_image.link

def sql_connect():
    global db,cursor,host
    host='localhost'
    port = 3306
    user='root'
    passwd=''
    database='aiot'
    #print('Connecting....')
    #print('host:%s\nuser:%s\npassword:********\ndatabase:%s\n'%(host,user,database))
    db=pymysql.connect(host=host,user=user,passwd=passwd,database=database,port=port)
    #os.system('clear')
    cursor=db.cursor()
    print('Connection succeed')
    
def sql_disconnect():
    db.close()
    print('Database is disconnected')

def select(table,field):   #table,field all are in string format
    sql = "SELECT " + field + " FROM " + table 
    try:    
        cursor.execute(sql) 
        data = cursor.fetchall()  
        db.commit()  
        return data
    except pymysql.Error as e:
        print("Select failed："+str(e))
        #line_push('資料查詢異常')
        with open("fail.csv",'a',newline='') as f:
            write = csv.writer(f)
            write.writerow([sql,str(e)])
            return False
    
      
def select_where(table,field,startdate,enddate):  #table,field,startdate and enddate all are in string format
    sql = "SELECT " + field + " FROM " + table  + " WHERE time >= \'" + startdate +'\' AND time < \' ' + enddate + '\''
    try:    
        cursor.execute(sql) 
        data = cursor.fetchall() 
        db.commit()   
        return data
    except pymysql.Error as e:
        print("Select failed："+str(e))
        #line_push('資料查詢異常')
        with open("fail.csv",'a',newline='') as f:
            write = csv.writer(f)
            write.writerow([sql,str(e)])
            return False
    
def date(year,month,day):
    year = int(year)
    month = int(month) 
    day = int(day)
    if month == 12 and day == 31 :
        year = year + 1
        month = 1
        day = 1
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day == 31 :
        month = month + 1
        day = 1
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
        month = month + 1
        day = 1
    elif  (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and month == 2 and day == 29 :
        month = month + 1
        day = 1
    elif month == 2 and day == 28 :
        month = month + 1
        day = 1
    else :
        day = day + 1
   
    date = str(year) + ' ' + str(month) + ' ' + str(day)
    return date
def SensorString(aa):
    sum1='time,'
    for i in range(7,len(aa),1):
        if(i==len(aa)-1):
            sum1=sum1+aa[i]
        else:
            sum1=sum1+aa[i]+','
    return sum1

def listadd(aa):
    aList = ['time']
    for i in range(7,len(aa),1):
        aList.append(aa[i])

    return aList

sql_connect()
        
def mtm1(a):   #輸入範例: 1 2021 12 1 2021 12 24 濕度....
    fig,ax=plt.subplots(figsize=(15,6)) #畫布大小
    plt.grid()  #顯示網格    
    nn=0  
    f1=0.0
    start=str(a[1]+"-"+a[2]+"-"+a[3])
    end = date(a[4],a[5],a[6])
    end=end.split()#分割字串
    
    field=SensorString(a)
    data=select_where("sensor_all",field,start,str(end[0]+"-"+end[1]+"-"+end[2]))

    data = pd.DataFrame(data)
   
    field=field.split(',')
    list1=listadd(a)
    data.columns=list1
   
    data.set_index(pd.to_datetime(data["time"],format="%Y-%m-%d"),inplace=True)
    for i in range(1,len(list1),1):
        if(list1[i]=='temperature' or 'humidity' or 'quality_Potted' or 'quality_Reservoir' or 'luminance' or 'CO2' or 'Potted' or 'Reservoir'):
            ax.plot(data["time"],data[list1[i]],label=list1[i],color=color[i],linestyle = "-")
        
    if(len(a)==8):
        for x in range(0,len(data),1):
            nn=nn+data.values[x][1]
        unit=''
        if(list1[1]=='temperature' or list1[1]=='Potted' or list1[1]=='Reservoir'):
            unit="°C"
        if(list1[1]=='humidity'):
            unit="%"
        if(list1[1]=='quality'):
            unit="ppm"       
        plt.axhline(y=float(nn/len(data)))
        ans=round(float(nn/len(data)),2) 
        trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
        ax.text(1.1,ans, "{}".format(ans)+unit,color="red", transform=trans, ha="right", va="center")
    #ax.set_ylabel("度",color="blue",fontsize=20,rotation=0)
        plt.title(list1[1]+" "+"chart"+"("+unit+")",color="limegreen",fontsize=20)
    plt.legend() #標籤顯示
    plt.xticks(rotation=45) 
    tick_spacing =data.index.size/2
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(xfmt) 
    ax.xaxis.set_major_locator(MaxNLocator(10))
    tick_spacing = 10

    fig.savefig('data_to_jpg.jpg')
    
def mtm3(a):   #輸入範例: 1 2021 12 1 2021 12 24 濕度....
    fig,ax=plt.subplots(figsize=(15,6)) #畫布大小
    plt.grid()  #顯示網格    
    nn=0  
    f1=0.0
    start=str(a[1]+"-"+a[2]+"-"+a[3])
    end = date(a[4],a[5],a[6])
    end=end.split()#分割字串
    
    field=SensorString(a)
    data=select_where("sensor_all",field,start,str(end[0]+"-"+end[1]+"-"+end[2]))

    data = pd.DataFrame(data)
   
    list1=listadd(a)
    
    data.columns=list1
    data['time']=data['time'].dt.date
    data['time'] = pd.to_datetime(data['time'],format="%Y-%m-%d")
    
    data=data.groupby("time", as_index=False).max()


    
    
    #data['time'] = data['time'].astype(float)
    #data["time"]=datetime.datetime(data["time"])

 
    for i in range(1,len(list1),1):
        if(list1[i]=='temperature' or 'humidity' or 'quality_Potted' or 'quality_Reservoir' or 'luminance' or 'CO2' or 'Potted' or 'Reservoir'):
            ax.bar(data["time"],data[list1[i]],label=list1[i],color=color[i],linestyle = "-")
        
    if(len(a)==8):
        for x in range(0,len(data),1):
            nn=nn+data.values[x][1]
        unit=''
        if(list1[1]=='temperature' or list1[1]=='Potted' or list1[1]=='Reservoir'):
            unit="°C"
        if(list1[1]=='humidity'):
            unit="%"
        if(list1[1]=='quality'):
            unit="ppm"       
        plt.axhline(y=float(nn/len(data)))
        ans=round(float(nn/len(data)),2) 
        trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
        ax.text(1.1,ans, "{}".format(ans)+unit,color="red", transform=trans, ha="right", va="center")
    #ax.set_ylabel("度",color="blue",fontsize=20,rotation=0)
        plt.title(list1[1]+" "+"chart"+"("+unit+")",color="limegreen",fontsize=20)
    plt.legend() #標籤顯示
    plt.xticks(rotation=45) 
    

    xfmt = md.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(xfmt) 
    

    fig.savefig('data_to_jpg.jpg')
def main(a):
    a=a.split()   #e=分割使用者輸入字串
    #1 2022 3 20 2022 3 23 temperature
    if(a[0]=="1"): # 2020 8  2020 9 濕度
        mtm1(a)
    #if(a[0]=="1" and ('\u4e00'>str(a[3]) or str(a[3])> '\u9fa5')and('\u4e00'>str(a[4]) or str(a[4])> '\u9fa5')): # 2020 8  2020 9 濕度
    if(a[0]=="3"):    #if(int(a[3])>1000):
        mtm3(a)   #輸入範例:   1    2020 8 2020 9 濕度....
            
            
    #if(a[0]=="2" and ('\u4e00'>str(a[3]) or str(a[3])> '\u9fa5')and('\u4e00'>str(a[4]) or str(a[4])> '\u9fa5')): # 2020 8  2020 9 濕度
        #if(int(a[3])>1000):
           # mtm2(a)   #輸入範例:   2    2020 8 2020 9 濕度....
            
 
    return jpg_to_url('data_to_jpg.jpg')

