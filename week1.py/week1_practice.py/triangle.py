side1 = int(input("enter the side"))
side2= int(input("enter the side"))
side3 = int(input("enter the side"))
sum1 = side1 + side2
sum2 = side2 + side3
sum3 = side1 + side3
if sum1 > side3 and (side1 == side2 or side2 == side3 or side3 == side1):
    print("Isosceles Triangl")
elif sum1 == side3:
    print("Equalateral Triangle")
elif sum1 > side3 and sum2 > side1 and sum3 > side2:
    print("Scalene") 
else:
    print("invalid")