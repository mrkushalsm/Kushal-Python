list_1 = []
print("Enter 10 numbers: ")
for i in range(10):
    list_1.append(int(input()))

for i in range(10):
    for j in range(10 - i - 1):
        if list_1[j] > list_1[j + 1]:
            temp = list_1[j]
            list_1[j] = list_1[j + 1]
            list_1[j + 1] = list_1[j]
print(list_1)
print("The second largest number in the list_3 is", list_1[len(list_1) - 2])
