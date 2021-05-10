def binary(a):
    b = int(a)
    i = 0
    mask = 1
    while b != 0:
        if b & mask == mask:
            i = i+1
        b = b>>1
    return i
# 設a為輸入值
a = input("請輸入要判斷的數字")
# 將a轉換為二進位字串b
binary(a)
print (binary(a))
    
 
