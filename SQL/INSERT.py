import mysql.connector as mysql
import pandas as pd
import time
from NBA import *
def insert(mysqldb,cursor):
    try:
        table = input("請輸入想新增內容的表格:")
        title = input("請輸入想新增內容的欄位:").split(",")
        value = input("請輸入想新增內容:").split(",")
        keys = ",".join(str(i) for i in title)
        values = ",".join(str(i) for i in value)
        sql = '''insert into '''+table+''' ('''+keys+''')values('''+values+''')'''
        sel_sql = '''SELECT * from '''+table
        ins2(mysql = mysqldb,cursor = cursor,insert = (sql),select = sel_sql,number = 30)
    except Exception as e:
        print(e)
