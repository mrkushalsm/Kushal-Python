phone_no = input("Enter your phone number: ")
if phone_no[3] == "-" and phone_no[7] == "-":
    print("The phone number entered is a valid format!")
    if len(phone_no) == 12:
        print("The phone number entered is valid!")
    else:
        print("The phone number entered is not valid!")
else:
    print("The phone number entered is not a valid format!")
    