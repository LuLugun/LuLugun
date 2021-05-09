import pandas as pd
import numpy as np
df=pd.read_csv("034week_pattern.csv")

add_forward_totalize = df["median"]
ts = df["time"]
dd = df["day"]
n = 0
maxn = 0
time = 0
try:
    for day in range(7):
        for i in range(48):
            if round(add_forward_totalize[day*48+i],3) == 0:
                #print(day*96+i,ts[day*96+i])
                n = n+1
            else:
                if n != 0:
                    if n > maxn:
                        maxn = n
                        time = day*48+i-n
                        #print(ts[day*96+i-n],n,dd[time])
                n = 0
        if maxn>0:
            print(ts[time],maxn,dd[time])
        maxn = 0
        n = 0
except Exception as e:
    print(e)
