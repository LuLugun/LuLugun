while True:
    a = int(input("輸入整數"))
    if a%15 == 0:
        print (str(a)+"is a multipleof 3 and5")
        break
    if a%3 == 0:
        print (str(a)+"is a multipleof 3")
        break
    if a%5 == 0:
        print (str(a)+"is a multipleof 5")
        break
    else:
        print (str(a)+"is not a multipleof 3 or 5")
