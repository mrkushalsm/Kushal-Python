# Under Work
"""
print("Enter three numbers: ")
num1 = int(input())
b = int(input())
num3 = int(input())

if num1 < b and num1 < num3:
    if b < num3:
        print(num1, ",", b, ",", num3)
    elif num3 < b:
        print(num1, ",", num3, ",", b)
    elif b == num3:
        print(num1, ",", num3, ",", b)
elif b < num1 and b < num3:
    if num1 < num3:
        print(b, ",", num1, ",", num3)
    elif num3 < num1:
        print(b, ",", num3, ",", num1)
    elif num1 == num3:
        print(b, ",", num3, ",", num1)
elif num3 < num1 and num3 < b:
    if num1 < b:
        print(num3, ",", num1, ",", b)
    elif b < num1:
        print(num3, ",", b, ",", num1)
    elif num1 == b:
        print(num3, ",", b, ",", num1)
else:
    print("All the numbers are equal")
"""
