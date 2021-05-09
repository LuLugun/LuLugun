import mysql.connector as mysql
import pandas as pd
import time
from NBA import *
def delet(mysqldb,cursor):
    try:
        table = input("請輸入想刪除內容的表格:")
        title = input("請輸入想刪除內容的欄位:")
        titlevalue = input("此欄位的值:")
        sql = '''delete from '''+table+''' where '''+title+''' = '''+titlevalue
        sel_sql = '''SELECT * from '''+table
        ins2(mysql = mysqldb,cursor = cursor,insert = (sql),select = sel_sql,number = 30)
    except Exception as e:
        print(e)
