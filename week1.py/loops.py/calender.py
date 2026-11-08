day = int(input("enter a day (1-31)"))
month = int (input("enter a month (1-12)"))
year = int(input("enter a year"))
months_large_days = [1,3,5,7,8,10,12]
months_small_days = [4,6,9,11]
is_leap = (year % 4 == 0 and year %100 != 0) or (year % 400 == 0)
if month in months_large_days:
    max_day = 31
elif month in months_small_days:
    max_day = 30
elif month == 2:
    if is_leap:
        max_day = 29
    else:
        max_day = 28    
else:
    max_day = 0
if max_day == 0 or day <= 0 or day > max_day or month <= 0 or month > 12 or year <= 0:
    print("invalid enter please enter correct formate")

else:
    if day < max_day:
            day = day +1
    elif month == 12:
        month = 1
        year = year +1
        day = 1
    else:
        day = 1
        month = month + 1
        
    print(f"Next Date is: {day}-{month}-{year}")
   