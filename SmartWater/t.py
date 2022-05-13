import pandas as pd
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta
import datetime

import warnings
warnings.filterwarnings('ignore')

for h in range(18):
    df=pd.read_csv("107_NTU_1310803040"+str(h+47)+".csv")
    #np.where("NEW" in df.columns, df=df.rename(columns={"NEW":"forward_totalize"}), df=df.rename(columns={"value_c":"forward_totalize"}))

    #if "NEW" in df.columns:
        #df=df.rename(columns={"NEW":"forward_totalize"})
    #else:
        #df=df.rename(columns={"value_c":"forward_totalize"})
       
    df=df.rename(columns={"interface_id":"id",'value_c':"forward_totalize", 'value_i':"add_forward_totalize","Unnamed: 4":"datetime"})
    df=df.drop(columns="rcvtime")
    #print(df)
   
    #n=0
    #add_forward_totalize_list=[]
    #try:
        #for i in df["forward_totalize"]:
            #add_forward_totalize=(df["forward_totalize"][n+1])-(df["forward_totalize"][n])
            #n=n+1
            #add_forward_totalize_list.append(add_forward_totalize)
                #print(add_forward_totalize)
    #except Exception as e:
        #print(e)
    #add_forward_totalize_list=["NaN"]+add_forward_totalize_list

    #df['add_forward_totalize']=add_forward_totalize_list
    df=df[["id","datetime","forward_totalize","add_forward_totalize"]]
    df['datetime']=pd.to_datetime(df['datetime'],format="%Y/%m/%d %H:%M:%S")

    df['date'] = [i.date() for i in df['datetime']]
    df['time'] = [i.time() for i in df['datetime']]
    df=df[["id","datetime","date","time","forward_totalize","add_forward_totalize"]]

    print(df)


    st1=str(df["date"][0])[:]
    end1=str(df["date"][0]).find('-')
    year=st1[:end1]

    start2=str(df["date"][0]).find('-')+1
    st2=str(df["date"][0])[start2: ]
    end2=st2.find("-")
    month=st2[:end2]

    start3=st2.find('-')+1
    date=st2[start3:]

    dstart=datetime.date(int(year), int(month), int(date))

        #print(str(df["date"][len(df["date"])-1])[:])
    st11=str(df["date"][len(df["date"])-1])[:]
    end11=str(df["date"][len(df["date"])-1]).find('-')
    yearr=st11[:end11]

    start22=str(df["date"][len(df["date"])-1]).find('-')+1
    st22=str(df["date"][len(df["date"])-1])[start22: ]
    end22=st22.find("-")
    monthh=st22[:end22]

    start33=st22.find('-')+1
    datee=st22[start33:]

    dend=datetime.date(int(yearr), int(monthh), int(datee))


    df1=df.copy(deep=True)
    mon=pd.DataFrame([dstart+timedelta(days=x+1) for x in range((dend-dstart).days+1)if(dstart+timedelta(days=x)).weekday()==6])
    mon=mon.rename(columns={0:"dates"})
    Mon=df1[df1["date"].isin(mon["dates"])].reset_index(drop=True)
    print(mon)
        #
    df2=df.copy(deep=True)
    tue=pd.DataFrame([dstart+timedelta(days=x+2) for x in range((dend-dstart).days+1)
                                               if(dstart+timedelta(days=x)).weekday()==6])

    tue=tue.rename(columns={0:"dates"})
    Tue=df2[df2["date"].isin(tue["dates"])].reset_index(drop=True)
        #
    df3=df.copy(deep=True)
    wed=pd.DataFrame([dstart+timedelta(days=x+3) for x in range((dend-dstart).days+1)
                                               if(dstart+timedelta(days=x)).weekday()==6])

    wed=wed.rename(columns={0:"dates"})
    Wed=df3[df3["date"].isin(wed["dates"])].reset_index(drop=True)
        #
    df4=df.copy(deep=True)
    thu=pd.DataFrame([dstart+timedelta(days=x+4) for x in range((dend-dstart).days+1)
                                               if(dstart+timedelta(days=x)).weekday()==6])

    thu=thu.rename(columns={0:"dates"})
    Thu=df4[df4["date"].isin(thu["dates"])].reset_index(drop=True)
        #
    df5=df.copy(deep=True)
    fri=pd.DataFrame([dstart+timedelta(days=x+5) for x in range((dend-dstart).days+1)
                                               if(dstart+timedelta(days=x)).weekday()==6])

    fri=tue.rename(columns={0:"dates"})
    Fri=df5[df5["date"].isin(fri["dates"])].reset_index(drop=True)
        #
    df6=df.copy(deep=True)
    sat=pd.DataFrame([dstart+timedelta(days=x+6) for x in range((dend-dstart).days+1)
                                                   if(dstart+timedelta(days=x)).weekday()==6])

    sat=sat.rename(columns={0:"dates"})
    Sat=df6[df6["date"].isin(sat["dates"])].reset_index(drop=True)
        #
    df7=df.copy(deep=True)
    sun=pd.DataFrame([dstart+timedelta(days=x+7) for x in range((dend-dstart).days+1)
                                               if(dstart+timedelta(days=x)).weekday()==6])

    sun=sun.rename(columns={0:"dates"})
    Sun=df7[df7["date"].isin(sun["dates"])].reset_index(drop=True)

    Mon["time"]=pd.to_datetime(Mon["time"],format="%H:%M:%S")
    mon_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Mon.loc[Mon["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                mon_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                mon_median_list.append(median)

            n = n+1

    #print(mon_median_list)

    Tue["time"]=pd.to_datetime(Tue["time"],format="%H:%M:%S")
    tue_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Tue.loc[Tue["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                tue_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                tue_median_list.append(median)

            n = n+1
    #print(tue_median_list)

    Wed["time"]=pd.to_datetime(Wed["time"],format="%H:%M:%S")
    wed_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Wed.loc[Wed["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                wed_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                wed_median_list.append(median)

            n = n+1
    #print(wed_median_list)

    Thu["time"]=pd.to_datetime(Thu["time"],format="%H:%M:%S")
    thu_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Thu.loc[Thu["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                thu_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                thu_median_list.append(median)

            n = n+1
    #print(thu_median_list)


    Fri["time"]=pd.to_datetime(Fri["time"],format="%H:%M:%S")
    fri_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Fri.loc[Fri["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                fri_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                fri_median_list.append(median)

            n = n+1
    #print(fri_median_list)

    Sat["time"]=pd.to_datetime(Sat["time"],format="%H:%M:%S")
    sat_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Sat.loc[Sat["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                sat_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                sat_median_list.append(median)

            n = n+1
    #print(sat_median_list)

    Sun["time"]=pd.to_datetime(Sun["time"],format="%H:%M:%S")
    sun_median_list = []
    for i in range(24):
        n=0

        while(n<=59):
            lis = []
            if i <=9:
                ti = "0"+str(i)
            elif i>9:
                ti = str(i)


            if n<=9:
                ni= "0"+str(n)
            elif n>9:
                ni=str(n)

            timestamp = ti+":"+ni+":00"
            #print(timestamp)
            for l in Sun.loc[Sun["time"].dt.strftime("%H:%M:%S")== timestamp]["add_forward_totalize"]:
                    #print(l)
                lis.append(l)

            if len(lis)%2 == 0:
                list_index1 = len(lis)/2
                list_index2 = len(lis)/2+1
                median = (lis[int(list_index1)]+lis[int(list_index2)])/2
                sun_median_list.append(median)
            elif len(lis)%2 != 0:
                list_index = int(len(lis)/2)+1
                median = lis[list_index]
                sun_median_list.append(median)

            n = n+1
    #print(sun_median_list)

    mon_pattern= {'time': Mon["time"][:1440],
                'median': mon_median_list}
    mon_pattern=pd.DataFrame(mon_pattern, columns = ['time', 'median'])

    tue_pattern= {'time': Tue["time"][:1440],
                'median': tue_median_list}
    tue_pattern=pd.DataFrame(tue_pattern, columns = ['time', 'median'])

    wed_pattern= {'time': Wed["time"][:1440],
                'median': wed_median_list}
    wed_pattern=pd.DataFrame(wed_pattern, columns = ['time', 'median'])

    thu_pattern= {'time': Thu["time"][:1440],
            'median': thu_median_list}
    thu_pattern=pd.DataFrame(thu_pattern, columns = ['time', 'median'])

    fri_pattern= {'time': Fri["time"][:1440],
            'median': fri_median_list}
    fri_pattern=pd.DataFrame(fri_pattern, columns = ['time', 'median'])

    sat_pattern= {'time': Sat["time"][:1440],
            'median': sat_median_list}
    sat_pattern=pd.DataFrame(sat_pattern, columns = ['time', 'median'])

    sun_pattern= {'time': Sun["time"][:1440],
            'median': sun_median_list}
    sun_pattern=pd.DataFrame(sun_pattern, columns = ['time', 'median'])

    week=pd.concat([mon_pattern,tue_pattern,wed_pattern,thu_pattern,fri_pattern,sat_pattern,sun_pattern]).reset_index(drop=True)

    week.to_csv("week_pattern"+str(h+47)+".csv",index=False)
