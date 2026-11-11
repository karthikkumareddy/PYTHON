correct_pwd = "placement2028"
user_pwd = ""

while user_pwd != correct_pwd:
    user_pwd = input("Enter password: ")
    if user_pwd != correct_pwd:
        print("Wrong password, try again!")

print("Access Granted!")
