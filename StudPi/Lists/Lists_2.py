list = []
limit = int(input("Enter the limit: "))
print("Enter the numbers: ")
for i in range(limit):
    list.append(int(input()))

num = int(input("Enter the number you want to find: "))
for i in range(limit):
    if list[i] == num:
        print("Found", num, "in list1", list)
        exit()
print("Could not find", num, "in list1", list)

