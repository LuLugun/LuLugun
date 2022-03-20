import os
import datetime
import pandas as pd
import untangle
import pymysql
try:
    os.mkdir('vd_csv')
except FileExistsError as e:
    print(str(e)[0:13])
    if str(e)[0:14] == '[WinError 183]':
        print('no')
        pass