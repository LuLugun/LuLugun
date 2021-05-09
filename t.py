import pyodbc
import pandas as pd
import numpy as np
server = '59.125.208.103,33311' 
database = 'twcwm_TPE' 
username = 'syscom' 
password = 'syscom12345'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
sql = '''select [interface_id],[rcvtime],[value_c],[value_i] from [dbo].[mtrread_l3_10803] where [interface_id] = '000978761684' '''
df = pd.read_sql(sql,cnxn)
print(len(df))
