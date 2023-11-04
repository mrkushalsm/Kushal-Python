t1 = ()
print("Enter 5 numbers: ")
for i in range(5):
    num = int(input())
    t1 += (num, )

max_num = t1[0]
for i in range(1, 5):
    if t1[i] > max_num:
        max_num = t1[i]

print("The maximum number in tuple is", max_num)
