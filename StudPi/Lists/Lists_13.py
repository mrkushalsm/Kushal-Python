list1 = []
print("Enter 10 numbers: ")
for i in range(10):
    list1.append(int(input()))

print("The elements with one even digit are: ", end="")
for i in range(0, 10):
    num = str(list1[i])
    for j in num:
        if int(j) % 2 == 0:
            print(num, end=" ")
            break
