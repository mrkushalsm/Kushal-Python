num = int(input("Enter a number: "))
first_num = 0
count = 1
while first_num < num:
    if first_num * (first_num + 1) == num:
        print(num, "is a pronic number")
        exit()
    else:
        first_num += 1
print(num, "is not a pronic number")
"""

Alternative method:-

while first_num < num:
    if first_num * (first_num + 1) == num:
        count -=1
    first_num += 1
if count == 0:
    print(num, "is a pronic number")
else:
    print(num, "is a not pronic number")
"""