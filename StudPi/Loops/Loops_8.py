num = int(input("Enter a number: "))
num_backup = num
sum = 0
while num != 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of the digits of", num_backup, "is", sum)