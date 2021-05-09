import pandas as pd
import numpy as np

for d in range(24,25):
    if d <=9:
        std = "0"+str(d)
    elif d>9:
        std = str(d)
    csv = "new_"+std+"_indexed.csv"
    print(csv)
    df=pd.read_csv(csv)

    day_list = []

    day = 2
    for i in range(91):
        for l in range(96):
            day_list.append(day)
        if day ==7:
            day = 0
        day = day+1

    #print(day_list)
    df["day"] = day_list
    print(df)
    outcsv = std+".csv"
    df.to_csv(outcsv,index=False)
