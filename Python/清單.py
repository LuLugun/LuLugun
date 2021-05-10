# 提供範例解釋規則
print ("範例:123456789=>[1,2,3,4,5,6,7,8,9]")
# 輸入兩個要計算的字串
a = input("請輸入要計算的整數清單(1)=")
b = input("請輸入要計算的整數清單(2)=")
# 判斷字串是否都為整數
if  a.isdigit() and b.isdigit():
    # 將字串a轉換為清單x
    x = list(a)
    # 將字串b轉換為清單y
    y = list(b)
    # 利用map函數將指定的清單內每個物件從字串改變成整數
    x = list(map(int, x))
    y = list(map(int, y))
    # 使兩清單相黏在一起創造一個新的清單
    z = x + y
    # 使用sum函數計算清單x的總和
    c1 = sum(x)
    # 使用sum函數計算清單y的總和
    c2 = sum(y)
    # 使用sum函數計算清單z的總和
    c3 = sum(z)
    # 使用len函數計算清單z長度
    d = len(z)
    # 清單z的總和除以長度d為平均數
    e = c3/d
    # 使用for迴圈用i列出清單z的每個物件，將各項i平方，再用sum函數計算總和
    f = sum([i**2 for i in z])
    print (x)
    print (y)
    print ("清單(1)總和="+str(c1))
    print ("清單(2)總和="+str(c2))
    print ("清單相加的總和="+str(c3))
    print ("清單相加的平均數="+str(e))
    print ("兩清單中的最大值="+str(max(z)))
    print ("兩清單中的最小值="+str(min(z)))
    print ("兩清單各項平方總和="+str(f))
else:
    print ("你的輸入不符合規則")
