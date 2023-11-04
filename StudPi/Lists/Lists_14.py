list_1 = []
print("Enter 10 numbers: ")
for i in range(10):
    list_1.append(int(input()))

snake_x = int(input("Enter a position"))
for i in range(snake_x, 10):
    for j in range(snake_x, 10 - 1 - i):
        if list_1[j] > list_1[j + 1]:
            temp = list_1[j]
            list_1[j] = list_1[j + 1]
            list_1[j + 1] = temp

print("Maximum number is", list_1[len(list_1) - 1])
print("Minimum number is", list_1[snake_x])
