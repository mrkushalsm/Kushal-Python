# list1 = [3, 8, 2, 9, 1, 7, 6, 4, 5, 10]
list1 = [3, 8, 1, 9, 2, 7, 6, 4, 5, 10]

for i in range(0, len(list1)):
    large = list1[i]
    pos = i
    for j in range(i + 1, len(list1)):
        if list1[j] > large:
            large = list1[j]
            pos = j
    temp = list1[i]
    list1[i] = list1[pos]
    list1[pos] = temp

print(list1)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
print(list1)
list1.pop()
print(list1)
list1.remove(6)
print(list1)