import pandas as pd
import numpy as np
import statistics


def get_mode(arr):
    mode = [];
    arr_appear = dict((a, arr.count(a)) for a in arr);  # 統計各個元素出現的次數
    if max(arr_appear.values()) == 1:  # 如果最大的出現為1
        return  # 則沒有眾數
    else:
        for k, v in arr_appear.items():  # 否則，出現次數最大的數字，就是眾數
            if v == max(arr_appear.values()):
                mode.append(k)
    return mode





df = pd.read_csv("107_NTU_131080304053.csv")
fp = open("107_NTU_131080304053.txt","a")
add_forward = df['value_i']
time = df['rcvtime']
list1 = []
t=0
z=0
p=0
y=0
same= []
same1 = 0
for i in range(1,17280-120):
    mode = []
    for l in range(i,120+i):
        mode.append(round(add_forward[l-1],3))
    #print(mode)
    
    y = 0
    for o in mode:
        if o == 0:
            z=1
        elif o!=0 :
            z = 0
            p=0
        if z == 1:
            #print ("幹")
            p=p+1
            list1.append(p)
    if list1 != []:
        y = max(list1)
        list1 = []
    if i%5202==0:
        print("loading "+str(int(i*100/17280))+"%.......")
    if y < 3:
        #print(mode)
        a = get_mode(mode)
        #print(a)
        t = 0
        p=0
        #print(mode)
        for x in range(len(mode)):
            if mode[x] == a[0]:
                t=t+1
                aa = x+i+1
        print (round(t*(100/240),2))
        if round(t*(100/240),2) >= 70:
            for j in range(len(mode)):
                if time[j+i+1] in same:
                    #print ("幹")
                    break
                else:
                    if mode[j] == a[0]:
                        #print (time[i+j+l])
                        #print (mode)
                        #print (round(t*(100/240),2))
                        #print (a)
                        fp.write(time[j+i+1])
                        fp.write("\n")
                        same.append(time[j+i+1])
            
        
fp.close()
    
