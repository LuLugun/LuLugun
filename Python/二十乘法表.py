# 設定輸入值進入迴圈重複執行
b = input("按下空白建")
while b == " ":
    # 輸入要查詢的數值，並將輸入值字串改為整數
    a = int(input("輸入要查詢的數字(1~20):"))
    # 若輸入值不再查詢範圍則跳出迴圈結束程式
    if a not in range(1,21):
        break
    # 列出1~20作為乘數使用
    for x in range(1,21):
        # 設變數i作為乘法迴圈跳出的計數器
        print (str(a)+"*"+str(x)+"="+str(a*x))
print ("程式結束")

