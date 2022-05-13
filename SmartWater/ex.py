import pandas as pd
import numpy as np
import statistics
df = pd.read_csv("04.csv")
lday = df['l_day']
add_forward = df['add_forward_totalize']
k=0
t=0
d=0
dp=0
a= []
lw=[]
total=[]

for i in lday:
    if i > 0 and k==0:
        lw = []
        print (t)
        for j in range(96):
            lw.append(add_forward[t-96+j])
            #print (add_forward[t-96+j])
        #print (lw)
        #print (len(lw))
        str1=str(lw[len(lw)-1])
        for j in str1:
            a.append(j)
        for j in a:
            if j!="0" or j!=".":
                break
            dp=dp+1
        for j in range(len(lw)):
            lw[j] = round(lw[j],dp)
        k = 1
        t=t+1
    elif i>0 and k==1:
        lw.append(add_forward[t])
        str1=str(lw[len(lw)-1])
        for j in str1:
            a.append(j)
        for j in a:
            if j!="0" or j!=".":
                break
            dp=dp+1
        for j in range(len(lw)):
            lw[j] = round(lw[j],dp)
        k = 1
        d = d+1
        t=t+1
    elif i==0 and k==1:  
        lw.append(add_forward[t-1])
        print (add_forward[t-1])
        print (lw)
        str1=str(lw[len(lw)-1])
        a = []
        for j in str1:
            a.append(j)
        for j in a:
            if j!="0" or j!=".":
                break
            dp=dp+1
        
        for j in range(len(lw)):
            lw[j] = round(lw[j],dp)
        k=0
            #print (lw)
        total.append(statistics.mode(lw))
    else:
        t=t+1
    
print (total)