import mysql.connector as mysql
import pandas as pd
import time
from NBA import *
from SELECT import *
from INSERT import *
from SET import *
from DELET import *


print("連結資料庫.......")
time.sleep(2)
mysqldb,cursor = conn(username,password,database)
print("連結成功")
time.sleep(1)
end1 = 0
choose = '''
============================================
| 操作代碼列表                              |
| 1:搜尋                                   |
| 2:新增                                   |
| 3:修改                                   |
| 4:刪除                                   |
| 5:斷開連結                                |
============================================'''


while(end1 != 1):
    print(choose)
    try:
        n1 = int(input("請輸入操作代碼:"))
        if(n1>0 and n1<6):
            if(n1 == 1):
                select(mysqldb,cursor)
            elif(n1 == 2):
                insert(mysqldb,cursor)
            elif(n1 == 3):
                set(mysqldb,cursor)
            elif(n1 == 4):
                delet(mysqldb,cursor)
            elif(n1 == 5):
                print("斷開資料庫連結中")
                end1 = 1
            else:
                print("錯誤代碼,請確認後重新輸入")
        else:
            print("錯誤代碼,請確認後重新輸入")
    except Exception as e:
        print(e)

        
cursor.close()
mysqldb.close()
print("資料庫已關閉")
