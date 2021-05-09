import pandas as pd
import numpy as np

df=pd.read_csv("025week_pattern.csv")
print("25")
day = df["day"]
add = df["median"]
d = day[0]
n = 0
maxn = 100
mind = 0
for i in range(337):
    if day[i] != d:
        print(d,":",n)
        if maxn > n:
            maxn = n
            mind = d
        n = 0
        d = day[i]
    n = n+add[i]
        
    
print("最小用水日",mind,":",maxn)
