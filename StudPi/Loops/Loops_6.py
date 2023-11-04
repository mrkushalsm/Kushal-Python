print("Enter the first distance (in feet and inches): ")
feet_1 = float(input())
inches_1 = float(input())
print("Enter the second distance (in feet and inches): ")
feet_2 = float(input())
inches_2 = float(input())

feet = feet_1 + feet_2
inches = inches_1 + inches_2

if inches >= 12:
    feet += inches // 12
    inches = inches % 12

print("Total distance =", feet, "feet and", inches, "inches")