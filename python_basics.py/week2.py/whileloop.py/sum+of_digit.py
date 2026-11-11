n = int(input("enter the three digit number(Ex123)"))
sum = 0
while n > 0:
    digit = n % 10
    sum = digit + sum
    n = n // 10
print(sum)
