with open("read.txt","r") as b:
    for x in b:
        a = x.split()
    i = 0
    for y in a:
        y = int(y)
        i = i+y
    print (i)
