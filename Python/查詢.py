def search(c,b):  # 定義函數search
    i = 0  # 設變數i來計算行數
    for x in b:  # for迴圈列出檔案內容
        if c in x:  # 如果查詢內容c在變數x裡輸出查詢內容的位置
            y = x.split(",")  # 利用split將字串以移除空白鍵的方式建立清單
            for z in y:  # for迴圈列出清單內容
                if z == c:  # 若z等於查詢內容則輸出行數與字數
                    i = i+1
                    print(x)
    return(i)
                
day = input("天數")
a = input("輸入要讀入的檔案:")  # 輸入要讀入的檔案名

while True:  # 設立無限迴圈
    with open(a,"r") as b:  # 利用with as開關檔案
        search1 = input("輸入要查詢的內容:")  # 輸入要查詢的內容
        i = search(search1,b)  # 呼叫函數search查詢輸入內容行數與字數
        print(i)
        day1 = int(day) * 96
        if int(i) < int(day1) :
            print("資料缺失:"+str(int(day1) - int(i)))
