n = int(input("enter the number"))
is_prime = True
if n==2:
    is_prime = True

if n > 1:
    for i in range(2,n):
        if(n % i == 0):
            is_prime = False
else:
    is_prime = False
if is_prime == False:
    print(f"{n} is not prime number")
else:
    print(f"{n}  prime number")
