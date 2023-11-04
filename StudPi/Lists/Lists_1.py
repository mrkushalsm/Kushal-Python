list = []
limit = int(input("Enter the limit: "))
print("Enter the numbers: ")
for i in range(limit):
    list.append(int(input()))

num = int(input("Enter a number: "))
index = int(input("Enter the position where you want to place the number: "))
list[index] = num

print("List is", list)