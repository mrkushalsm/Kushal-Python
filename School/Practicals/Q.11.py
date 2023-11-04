sname = input("Enter student's name: ")
hmarks = int(input("Enter hindi marks: "))
emarks = int(input("Enter english marks: "))
mmarks = int(input("Enter maths marks: "))
pmarks = int(input("Enter physics marks: "))
cmarks = int(input("Enter chemistry marks: "))

tmarks = hmarks + emarks + mmarks + pmarks + cmarks

per = int((tmarks /  5) * 100)

if per >= 70:
    print("Passed!")
else:
    print("Failed!")
