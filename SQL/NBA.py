username = 'root'
password = '7777xxxx'
database = 'text'
host = '127.0.0.1'

import mysql.connector as mysql
import pandas as pd

def show(mysql, cursor):
    cursor.execute('''Show tables''')
    result = cursor.fetchall()
    print('已建立欄位: ', end = ' ')
    for i in result:
        print(i[0], end = ' ')

def conn(name, pword, db, mysqldb = None, cursor = None):
    try:  
        mysqldb = mysql.connect( 
                host = host,
                user = name,
                password = pword,
                database = db,
                raise_on_warnings = True,
                charset = 'utf8'
            )
    except Exception as e:
        print(e)
    else:
        if mysqldb.is_connected():
            print('資料庫名稱: ', db)
            cursor = mysqldb.cursor()
            show(mysqldb, cursor)
    return mysqldb, cursor


if __name__ == '__main__':
    try:
        mysqldb, cursor = conn(username, password, database)
        if (mysqldb or cursor) is None:
            print('Connected is error!')
    except Exception as e:
        print(e)

def sel(mysql, cursor, sql = None, number = 5):
    cursor.execute(sql)
    result = cursor.fetchall()
    fieldname = [i[0] for i in cursor.description]
    df = pd.DataFrame(result, columns = fieldname)
    print(df.head(number))


if __name__ == '__main__':
    sql = '''SELECT * from ships'''
    sel(mysqldb, cursor, sql)    

def ins(mysql,cursor,insert = None,select = None,number = 5):
    try:
        cursor.execute(insert[0],insert[1])
        mysql.commit()
    except Exception as e:
        print(e)
        mysql.rollback()
    else:
        sel(mysql,cursor,select,number)

def ins2(mysql,cursor,insert = None,select = None,number = 5):
    try:
        cursor.execute(insert)
        mysql.commit()
    except Exception as e:
        print(e)
        mysql.rollback()
    else:
        sel(mysql,cursor,select,number)


def advsel(mysqldb, cursor, find = None, tab = None, cond = None):
    try:
        if find: 
            sql = '''SELECT ''' + find
        else:
            sql = '''SELECT * '''
        if tab: 
            sql += ''' from ''' + tab
        if cond:
            sql += ''' where ''' + cond
    except Exception as e:
        print(e)
    else:
        cursor.execute(sql)
        result = cursor.fetchall()
        fieldname = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns = fieldname)
        print(df.head(100)) 
