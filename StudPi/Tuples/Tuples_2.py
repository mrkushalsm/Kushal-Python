t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
# t3 = (1, 2, 3, 4, 5, 1, 3, 5, 7, 9)
t3 = ()

for i in range(0, 10):
    if i < 5:
        t3 += (t1[i], )
    else:
        t3 += (t2[len(t2) - i], )

print(t3)