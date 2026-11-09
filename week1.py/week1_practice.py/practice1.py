n = int(input("enter the three digit number(ex:123)"))
n1 = n
last_digit = n % 10
middle_digit = n // 10
midd_last_digit = middle_digit % 10
first_digit = middle_digit // 10
sum = last_digit + midd_last_digit + first_digit
print(sum)
