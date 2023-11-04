# Redo this without string functions

import math

list_A = []
print("Enter 20 numbers:")
for i in range(0, 20):
    list_A.append(int(input()))

list_B = []
for i in range(0, len(list_A)):
    num = list_A[i]
    num_2 = str(int(math.pow(num, 2)))
    num_temp = str(num)
    if num_2.endswith(num_temp):
        list_B.append(num)

print(list_B)
