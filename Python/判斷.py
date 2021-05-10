# 輸入要判斷的內容
a=input("輸入內容")
# 如果a都是數字 則輸出這是整數
if a.isdigit():
    print ("這是整數")
# 如果a由字母與數字組成 則判斷是否為布林 
elif a.isalnum():
    if a == str(True) or a == str(False):
        print ("這是布林")  # 若為布林輸出這是布林
    else:
        print ("這是字串")  # 若不為布林則輸出這是字串
# 剩餘情況為浮點數
else:
    print ("這是浮點數")
