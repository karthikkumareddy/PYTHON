n = int(input("enter the number"))
for i in range(1,n+1):
    for space in range(i,n+1):
        print(" ",end = " ")
    for star in range(i):
        print("*",end=" ")
    print()