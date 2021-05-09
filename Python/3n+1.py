while(True):
    n = int(input("請輸入數字:"))
    if n != 0:
        print(n,end=' ')
    else:
        break
    while(int(n) != 1):
        if n % 2 == 0:
            n = n/2
            print(int(n),end=' ')
        elif n % 2 != 0:
            n = 3*n+1
            print(int(n),end=' ')
    print("")
print("結束程式")

