list1 = [11, 12, 13, 14, 15]
for i in range(len(list1) // 2):
    temp = list1[i]
    list1[i] = list1[len(list1) - i - 1]
    list1[len(list1) - i - 1] = temp

print(list1)