import pandas as pd
import numpy as np
df = pd.read_csv("107_NTU_131080304047.csv")
value = df['value_i']
day_value = 0
min_value = 100
max_value = 0
for week in range(16):
    print("max:",max_value,"min:",min_value)
    min_value = 100
    max_value = 0
    
    for day in range(7):
        #print(day,day_value)
        if day_value>max_value:
            max_value = day_value
        if day_value<min_value:
            min_value = day_value
            
        day_value = 0
        for i in range(1,1441):
            #print(day,(6*1440)+i+(week*7*1440)+(day*1440),value[(6*1440)+i+(week*7*1440)+(day*1440)])
            day_value = day_value + value[(6*1440)+i+(week*7*1440)+(day*1440)]
            
