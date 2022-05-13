import pandas as pd
import numpy as np
from datetime import datetime



for cc in range(1,59):
    cs = str(cc)+ ".csv"
    df=pd.read_csv(cs)

    #print(df)

    df['ts']=pd.to_datetime(df['ts'],format="%Y/%m/%d %H:%M:%S")

    date=df['ts'].dt.month.between(10,12,inclusive=True)
    df_date=df.loc[date]


    frame_id=df_date.groupby("meter_id")
    if cc <=9:
        meter_idt = "C10840800"+str(cc)
    else:
        meter_idt = "C1084080"+str(cc)
    
    x1=frame_id.get_group(meter_idt)
    x1.index = range(len(x1))

    #print(x2)
    n=0
    add_forward_totalize_list=[]
    try:
        for i in x1["forward_totalize"]:
            add_forward_totalize=(x1["forward_totalize"][n+1])-(x1["forward_totalize"][n])
            n=n+1
            add_forward_totalize_list.append(add_forward_totalize)
    except Exception as e:
        print(e)
    add_forward_totalize_list=["NaN"]+add_forward_totalize_list
    #print(add_forward_totalize_list)



    n=0

    add_reverse_totalize_list=[]
    try:
        for i in x1["reverse_totalize"]:
            add_reverse_totalize=(x1["reverse_totalize"][n+1])-(x1["reverse_totalize"][n])
            n=n+1
            add_reverse_totalize_list.append(add_reverse_totalize)
    except Exception as e:
        print(e)
    add_reverse_totalize_list=["NaN"]+add_reverse_totalize_list


    n=0

    add_flow_status_list=[]
    try:
        for i in x1["flow_status"]:
            add_flow_status=(x1["flow_status"][n+1])-(x1["flow_status"][n])
            n=n+1
            add_flow_status_list.append(add_flow_status)
    except Exception as e:
        print(e)
    add_flow_status_list=["NaN"]+add_flow_status_list


    x1['add_forward_totalize'],x1['add_reverse_totalize'],x1['add_flow_status']=[add_forward_totalize_list,add_reverse_totalize_list,add_flow_status_list]
    #print(len(x2.index))
    #print(len(x2))
    #x2['time'] = [x2.index]

    #print(x2)
    csv = str(cc)+"_data.csv"
    x1.to_csv(csv,index=False)
