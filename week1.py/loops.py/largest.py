a = int(input("first number (a): "))
b = int(input("second number(b): "))
c = int(input("third number (c): "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"largest number: {largest}")
