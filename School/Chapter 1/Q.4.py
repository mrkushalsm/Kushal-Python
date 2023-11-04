num1 = input("Enter number 1: ")
num2 = int(input("Enter number 2: "))
boolean_var = False

if num2 == 2:
    if int(num1[-1]) % 2 == 0:
        boolean_var = True
elif num2 == 3:
    sum = 0
    for num in num1:
        sum += int(num)
    if num % 3 == 0:
        boolean_var = True
elif num2 == 4:
    if num1[-2:] == "00" or int(num1[-2:]) % 4 == 0:
        boolean_var = True
elif num2 == 5:
    if num1[-1] == "0" or num1[-1] == "5":
        boolean_var = True
elif num2 == 6:
    if int(num1[-1]) % 2 == 0:
        sum = 0
        for num in num1:
            sum += int(num)
        if num % 3 == 0:
            boolean_var = True
elif num2 == 7:
    if ((2 * int(num1[-2:])) - (int(num1[:-2]))) % 7 == 0:
        boolean_var = True
elif num2 == 8:
    if num1[-3:] == "000" or int(num1[-3:]) % 8 == 0:
        boolean_var = True
elif num2 == 9:
    sum = 0
    for num in num1:
        sum += int(num)
    if num % 9 == 0:
        boolean_var = True
elif num2 == 10:
    if num1[-1] == "0":
        boolean_var = True
elif num2 == 11:
    first = num1[::2]
    second = num1[1::2]
    first_num, second_num = 0, 0
    for i in first:
        first_num += int(i)
    for i in second:
        second_num += int(i)
    if (first_num - second_num) % 11 == 0:
        boolean_var = True
elif num2 == 12:
    if num1[-2:] == "00" or int(num1[-2:]) % 4 == 0:
        sum = 0
        for num in num1:
            sum += int(num)
        if num % 3 == 0:
            boolean_var = True

if boolean_var:
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)
