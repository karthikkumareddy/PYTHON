attendance = float(input("Enter your attendance percentage (0-100): "))
marks = float(input("Enter your marks (0-100): "))

# Outer if: Checks the attendance condition first
if attendance >= 75:
    print("You are eligible for the exam. Calculating your grade...")
    
    # Inner if-elif-else (Nested): Determines the grade based on marks
    if marks >= 90:
        print("Grade: A+ (Excellent)")
    elif marks >= 75:
        print("Grade: B (Good)")
    elif marks >= 35:
        print("Grade: C (Pass)")
    else:
        print("Grade: F (Fail) - Need to work harder!")

else:

    print("Sorry! Your attendance is below 75%. You are detained.")
