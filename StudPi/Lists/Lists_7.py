# Under Work

list_1 = [7, 5, 2, 1, 10, 8, 4, 2, 5, 1]
list_2 = [6, 7, 10, 6, 3, 7, 5, 10, 6, 8]
common = []
for i in range(10):
    for j in range(10):
        if list_1[i] == list_2[j]:
            common.append(list_2[j])

print(common)
# [7, 7, 5, 10, 10, 8, 5]

count = 0
for i in range(len(common)):
    for j in range(len(common)):
        if common[i] == common[j]:
            count += 1
    if count >= 1:
        print(common[i])
    count = 0