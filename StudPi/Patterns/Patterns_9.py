a = 1
for i in range(2, 11, 2):
    for j in range(1, 7 - a):
        print(i, end=" ")
    a += 1
    print()
