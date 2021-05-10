def fibonacci(a1,a2,x):
        if x == 1:  # x若等於1代表查詢第一項，則直接輸出a值
            print (a1)
        elif x == 2:  #x若等於2代表查詢第一項，則直接輸出a值
            print (a2)
        else:
            x = x-2  # 去掉第一項跟第二項
            for i in range(1,x+1):  # 利用for迴圈敘述費式函數
                a3 = a1 + a2  # 將a2的值指定給a1，a3的值指定給a2，a3還是取a1+a2
                a1 = a2
                a2 = a3
            print (a3)
y = fibonacci
# 使用while迴圈讓程式重複執行
while True:
    # 費式函數公式 第n項=第n-1項+第n-2項
    a = int(input("起始值第一項a1="))
    b = int(input("起始值第二項a2="))
    x = int(input("查詢費式第幾位="))
    # 設立函數fibonacci()
    y(a,b,x)
    # 若輸入非空白建則跳出迴圈結束程式
    a = input("輸入空白鍵繼續執行")
    if a != " ":
        break
print ("程式結束")
