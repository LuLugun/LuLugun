# 輸入體重值單位kg
a = input("體重(kg):")
# 將a從字串變為浮點數來做計算
x = float(a)
# 輸入身高值單位cm
b = input("身高(cm):")
# 將b從字串變為浮點數並將單位轉換成公尺來做計算
y = float(b)/100
#B MI公式:體重(公斤) / 身高(公尺)*身高(公尺)
c=x/(y*y)
# 輸出BMI值好讓使用者知道更完善的身體數據
print("BMI:"+str(c))
# 如果C是小於18.5則屬於體重過輕，若不是且小於24則屬於體重正常，若不小於24則屬於體重過胖
if c < 18.5:
    print("體重過輕")
elif c < 24:
    print("體重正常")
else:
    print("體重過重")
