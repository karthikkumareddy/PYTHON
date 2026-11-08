# sub1 = float(input("Subject 1 Marks (Out of 100): "))
# sub2 = float(input("Subject 2 Marks (Out of 100): "))
# sub3 = float(input("Subject 3 Marks (Out of 100): "))
# sub4 = float(input("Subject 4 Marks (Out of 100): "))
# sub5 = float(input("Subject 5 Marks (Out of 100): "))

# total_marks = sub1 + sub2 + sub3 + sub4 + sub5
# max_marks = 500
# percentage = (total_marks / max_marks) * 100

# print("\n--- Marksheet Report ---")
# print(f"Total Marks Scored: {total_marks} / {max_marks}")
# print(f"Percentage Obtained: {percentage:.2f}%")

#Project Budget Calculator
Total_budget = int(input("Enter your toatal budget"))
Development_cost = Total_budget * 0.45
Marketing_cost = Total_budget * 0.35
buffer_cost = Total_budget * 0.25
print("\n--- Budget Distribution Report ---")
print(f"Total Budget: {Total_budget}")
print(f"Development Cost (45%): {Development_cost}")
print(f"Marketing Cost (35%): {Marketing_cost}")
print(f"Buffer Cost (20%): {buffer_cost}")

marketing_higher = Marketing_cost > Development_cost
print("\n--- Comparison Result ---")
print(f"Is Marketing Cost > Development Cost?:{marketing_higher}")

