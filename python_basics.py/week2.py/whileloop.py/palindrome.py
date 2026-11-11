n = int(input("enter a input"))
n1 = n
rev = 0
while n1 > 0:
    last_digit = n1 % 10
    rev = (rev * 10) + last_digit
    n1 = n1 // 10
if (rev == n):
    print("palindrome")
else:
    print("not palindrome")