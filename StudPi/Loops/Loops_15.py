list = []
print("Enter 10 numbers: ")
for i in range(10):
    list.append(int(input()))

print("The elements with one even digit are: ", end="")
for i in range(10):
    if list[i] % 2 == 0:
        print(list[i], "", end="")
