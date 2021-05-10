import mysql.connector as mysql
import pandas as pd
import time
from NBA import *
def set(mysqldb,cursor):
    try:
        table = input("請輸入想修改內容的表格:")
        title = input("請輸入想修改內容的參考欄位:")
        titlevalue = input("此欄位的值:")
        key = input("請輸入想修改的欄位:")
        value = input("此欄位的值:")
        sql = '''update '''+table+''' set '''+key+''' = '''+value+''' where '''+title+''' = '''+titlevalue
        sel_sql = '''SELECT * from '''+table
        ins2(mysql = mysqldb,cursor = cursor,insert = (sql),select = sel_sql,number = 30)
    except Exception as e:
        print(e)
