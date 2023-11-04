count = 0
num = int(input("Enter the limit: "))
for i in range(2, num, 1):
    for j in range(2, i, 1):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, end=' ')
    count = 0
print()
