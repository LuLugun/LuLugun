import mysql.connector as mysql
import pandas as pd
import time
from NBA import *


def select(mysqldb,cursor):
    try:
        tab = input("請輸入想搜尋的表格:")
        find = input("請輸入想搜尋的欄位:")
        advsel(mysqldb, cursor, find, tab)
    except Exception as e:
        print(e)
