import pandas as pd
import numpy as np
import statistics

df = pd.read_csv("107_NTU_131080304064.csv")
time = df['rcvtime']
fp = open("nmsl.txt","a")
d = 0
t=0
data = []

for i in time:
    data.append(format(i,'.0f'))
    #print(format(i,'.0f'))
#print (len(data))
#print(data[40225])
current = time[0]
  

for i in time:
    
    if i == current:
        #print(current,":",i)
        current = current+100
        str1 = str(current)
        
        if str1[9]=="6" and str1[10] == "0":
            current = current+4000
            #print("1")
        str1 = str(current)
        if str1[7]=="2" and str1[8] == "4":
            current = current+760000
        if str1[5]=="3" and str1[6]=="2" and( str1[4]=="1" or str1[4]=="3" or str1[4]=="5" or str1[4]=="7"or str1[4]=="8"or (str1[3]=="1"and str1[4]=="0") or (str1[3]==1 and str1[4]=="2")) :
            #print("1:",current)
            current = current+69000000-100
            #print("2:",current)
            #print("2")
        elif str1[5]=="3" and str1[6]=="1" and (str1[4]=="4" or str1[4]=="6" or str1[4]=="9" or (str1[4]=="1" and str1[3]=="1")) :
            
            current = current+70000000-100
            #print("2:",current)
            #print("3")
        elif str1[5]=="2" and str1[6]=="9" and str1[4]=="2" :
            #print("1:",current)
            current = current+72000000-100
            #print("2:",current)
            #print("4")

    elif current <= i:
        g=0
        while(g==0):
            
            d = d+1
            
            str1 = str(current)
            if str1[9]=="6" and str1[10] == "0":
                current = current+4000
            str1 = str(current)
            if str1[7]=="2" and str1[8] == "4":
                current = current+760000
            if str1[5]=="3" and str1[6]=="2" and (str1[4]=="1" or str1[4]== "3" or str1[4]== "5" or str1[4]== "7"or str1[4]== "8"or (str1[3]=="1"and str1[4]=="0") or (str1[3]==1 and str1[4]=="2")) :
                
                print("1:",current,i)
                current = current+69000000-100
                #print("2:",current)
            elif str1[5]=="3" and str1[6]=="1" and (str1[4]=="4" or str1[4]=="6" or str1[4]=="9" or (str1[4]=="1" and str1[3]=="1")) :
                print("2:",current,i)
                current = current+70000000-100
                #print("1:",current)
            elif str1[5]=="2" and str1[6]=="9" and str1[4]=="2" :
                #print("1:",current)
                current = current+72000000-100
                #print("2:",current)
            if current != i:
                fp.write(str(current))
                fp.write("\n")
            current = current + 100
        
            if current >= i:
                g=1
                current = current + 100
                str1 = str(current)
                if str1[9]=="6" and str1[10] == "0":
                    current = current+4000
                str1 = str(current)
                if str1[7]=="2" and str1[8] == "4":
                    current = current+760000
                if str1[5]=="3" and str1[6]=="2" and (str1[4]=="1" or str1[4]=="3" or str1[4]=="5" or str1[4]=="7"or str1[4]=="8"or (str1[3]=="1"and str1[4]=="0") or (str1[3]==1 and str1[4]=="2")):
                    #print("1:",current)
                    current = current+69000000-100
                    #print("2:",current)
                elif str1[5]=="3" and str1[6]=="1" and (str1[4]=="4" or str1[4]=="6" or str1[4]=="9" or (str1[4]=="1" and str1[3]=="1")):
                    #print("1:",current)
                    current = current+70000000-100
                    #print("2:",current)
                elif str1[5]=="2" and str1[6]=="9" and str1[4]== "2" :
                    #print("1:",current)
                    current = current+72000000-100
                    #print("2:",current)
print ('~~~~~~~~~~~~~~~~~~~')
print (d)
fp.close()
