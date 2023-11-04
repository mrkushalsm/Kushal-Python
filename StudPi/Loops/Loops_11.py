num = int(input("Enter a number: "))
temp = num
count = 0
while temp != 0:
    temp = temp // 10
    count += 1

print("The count of digits excluding the first and last digit in", num, "is", (count - 2))