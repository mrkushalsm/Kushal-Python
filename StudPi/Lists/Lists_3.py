name = []
phone_no  = []
limit = int(input("Enter a limit: "))
for i in range(limit):
    name.append(input("Enter a name: "))
    phone_no.append(int(input("Enter their phone number: ")))
print()

for i in range(limit):
    print("Name:", name[i])
    print("Phone No. :", phone_no[i])
