while True:
        try:
            aadhar_no=input("Enter Your 12 Digit Aadhar Number : ")
            if(len(aadhar_no) != 12) or (aadhar_no.isalpha()):
                raise ValueError ("Please Enter a valid 12 digit aadhar Number")
            break
        except ValueError as m:
            print(m)
print(aadhar_no)