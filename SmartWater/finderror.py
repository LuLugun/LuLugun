import pandas as pd
import numpy as np
import statistics
#for datan in range(560,597):
for datan in range(573,574):
    csvn = "218520800"+str(datan)+".csv"
    df = pd.read_csv(csvn)
    time = df['rcvtime']
    n = 1
    tt = 0
    all = 0
    for i in time:
        n  = n+1
        if tt == 24:
            tt = 0
        if int(str(i)[7]+str(i)[8]) != tt and n > 12:
            tt = tt+1
            n = 1
        elif int(str(i)[7]+str(i)[8]) != tt and n<=12:
            if tt <=9:
                tn = "0"+str(tt)
            else:
                tn = str(tt)
            print("1080"+str(i)[4]+str(i)[5]+str(i)[6]+tn,":",13-n)
            all = all + (13-n)
            #print(str(i)[8])
            tt = tt+1
            n = 1
    print(all)
