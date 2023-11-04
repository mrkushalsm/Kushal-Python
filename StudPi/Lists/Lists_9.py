list_1 = []
print("Enter 10 numbers: ")
for i in range(10):
    list_1.append(int(input()))

for i in range(10):
    for j in range(10 - 1 - i):
        if list_1[j] > list_1[j + 1]:
            temp = list_1[j]
            list_1[j] = list_1[j + 1]
            list_1[j + 1] = temp

print("Sorted List: ")
print(list_1)
