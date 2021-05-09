import pandas as pd
import numpy as np
import statistics

df = pd.read_csv("4_data.csv")
time = df['ts']
no = df['not']
a=0
b=0
c=0
x=0
for i in range(8831-96):
    for j in range(1+i,i+97):
        if no[j] ==2:
            a = a+1
        elif no[j]==3:
            b=b+1
        elif no[j]==4:
            c=c+1
    #print (a,b,c)
    f=0.998472218*a+1.147430929*b+1.254124732*c
    #print (f)
    if f >= 96 and f<120:
        #print (i)
        print (time[i],"低風險")
    elif f>=120 and f<150:
        print (time[i],"中風險")
    elif f>=150:
        print (time[i],"高風險")
    a=0
    b=0
    c=0
