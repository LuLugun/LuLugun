import pandas as pd
import numpy as np
import statistics
for datan in range(560,561):
    csvn = "218520800"+str(datan)+".csv"
    #df = pd.read_csv(csvn)
    df = pd.read_csv("131071204333.csv")
    value = df['value_i']
    n = 0
    for i in value:
        if i == 0:
            n = n+1
    if (100/len(value)*n)>=0:
        print(len(value)/100*n)
        print(csvn)
