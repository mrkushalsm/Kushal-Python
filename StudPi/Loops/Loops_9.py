import math
num = int(input("Enter a number: "))
temp = num
count = 0
while temp != 0:
    temp = temp // 10
    count += 1

temp_2 = num
reverse_num = 0
for i in range(1, count + 1):
    digit = temp_2 % 10
    reverse_num += int(math.pow(10, (count - i))) * digit
    temp_2 = temp_2 // 10

print("The reverse of", num, "is", reverse_num)