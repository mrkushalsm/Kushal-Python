import math
binary = int(input("Enter a binary number: "))
temp = binary
count = 0
while temp != 0:
    temp = temp // 10
    count += 1

sum = 0
temp2 = binary
for i in range(0, count):
    sum += int((temp2 % 10) * math.pow(2, i))
    temp2 = temp2 // 10

print(sum)