count = "y"
while count == "y":
    sex = int(input("1.英制 2.公制 ..."))
    if sex == 1:
        unit = int(input("(1) 碼 (2) 英呎 (3) 英吋 ..."))  #紀錄要輸入的長度單位
        if unit == 1:
            value = int(input("請輸入長度(英制、碼)="))
            print(value,"碼 = ",value*3,"英呎 = ",value*36,"英吋 = ",value*0.9144,"公尺 =",value*9.144,"公寸 =",value*91.44,"公分 =",value*914.4,"公釐")
        if unit == 2:
            value = int(input("請輸入長度(英制、英呎)="))
            print(value*0.3,"碼 = ",value,"英呎 = ",value*12,"英吋 = ",value*0.3048,"公尺 =",value*3.048,"公寸 =",value*30.48,"公分 =",value*304.8,"公釐")
        if unit == 3:
            value = int(input("請輸入長度(英制、英吋)="))
            print(value*0.028,"碼 = ",value*0.083,"英呎 = ",value,"英吋 = ",value*0.0254,"公尺 =",value*0.245,"公寸 =",value*2.54,"公分 =",value*25.4,"公釐")

    if sex == 2:
        unit = int(input("(1) 公尺 (2) 公寸 (3) 公分 (4) 公釐 ..."))  #紀錄要輸入的長度單位
        if unit == 1:
            value = int(input("請輸入長度(公制、公尺)="))
            print(value*1.0937,"碼 = ",value*3.281,"英呎 = ",value*39.37,"英吋 = ",value,"公尺 =",value*10,"公寸 =",value*100,"公分 =",value*1000,"公釐")
        if unit == 2:
            value = int(input("請輸入長度(公制、公寸)="))
            print(value*0.10937,"碼 = ",value*0.3281,"英呎 = ",value*3.937,"英吋 = ",value*0.1,"公尺 =",value,"公寸 =",value*10,"公分 =",value*100,"公釐")
        if unit == 3:
            value = int(input("請輸入長度(公制、公分)="))
            print(value*0.010937,"碼 = ",value*0.03281,"英呎 = ",value*0.3937,"英吋 = ",value*0.01,"公尺 =",value*0.1,"公寸 =",value,"公分 =",value*10,"公釐")
        if unit == 4:
            value = int(input("請輸入長度(公制、公釐)="))
            print(value*0.0010937,"碼 = ",value*0.003281,"英呎 = ",value*0.03937,"英吋 = ",value*0.001,"公尺 =",value*0.01,"公寸 =",value*0.1,"公分 =",value,"公釐")
            
    count = input("是否繼續(y/n)...")
    
