n = int(input("enter the number in seconds"))
hours = n // 3600
# minutes_in_seconds = n % 3600
minutes = n - (3600 * hours)
min = minutes // 60
seconds = minutes-(60 * min)
print(hours)
print(min)
print(seconds)
