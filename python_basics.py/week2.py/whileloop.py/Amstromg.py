l= input("enter the number")
n = int(l)
n1 = n
total= 0
digit = len(l)
while n > 0:
    last_digit = n % 10
    total = total + (last_digit ** digit)
    n = n // 10
if n1 == total:
    print("Amstromg Number")
else:
    print("Not Amstromg Number")