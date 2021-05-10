print ("數組1:")
x = []
while True:
    a = int(input())
    if a <=-9999:
        break
    x.append(a)
print ("數組2:")
y = []
while True:
    a = int(input())
    if a <=-9999:
        break
    y.append(a)
z = x+y
print(z)
print(sorted(z))
