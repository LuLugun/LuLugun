import mysql.connector as mysql # 載入mysql函示庫
import pandas as pd # 載入pandas函示庫
import time # 載入time函示庫
from NBAMYSQL import *
from SELECT import *
from INSERT import *
from SET import *
from DELET import *
import matplotlib.pyplot as plt # plt 用於顯示圖片
import matplotlib.image as mpimg # mpimg 用於讀取圖片
import numpy as np

print("連結資料庫.......")
time.sleep(2)  # 延遲輸出2秒
mysqldb,cursor = conn(username,password,database)  #使用預先設計好的conn函式來連結資料庫
print("連結成功")
time.sleep(1)  # 延遲輸出1秒
end1 = 0

while(end1 != 1):
    img = mpimg.imread('title.jpg')  # 顯示指令圖片
    plt.imshow(img) # 顯示圖片
    plt.axis('off') # 不顯示座標軸
    plt.show()
    try:
        n1 = int(input("請輸入操作代碼:"))  # 輸入操作代碼
        if(n1>0 and n1<6):  #判斷操作代碼,執行相應的動作
            if(n1 == 1):
                select(mysqldb,cursor)  # 輸入欄位與表格 在表格後加上where即可增加搜尋條件
            elif(n1 == 2):
                insert(mysqldb,cursor)  # 輸入欄位與表格和欄位內的內容
            elif(n1 == 3):
                set(mysqldb,cursor)  # 輸入表格,參考欄位和參考欄位的值,再加上想修改的欄位與值
            elif(n1 == 4):
                delet(mysqldb,cursor)  #輸入欄位與表格和欄位內的內容
            elif(n1 == 5):
                print("斷開資料庫連結中")
                end1 = 1  # 將變數end1設為1來離開迴圈
            else:
                print("錯誤代碼,請確認後重新輸入")
        else:
            print("錯誤代碼,請確認後重新輸入")
    except Exception as e:
        print(e)

        
cursor.close()  # 中斷資料庫連結
mysqldb.close()
print("資料庫已關閉")
