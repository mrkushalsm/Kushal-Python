num = int(input("Enter any 5-digit number: "))
temp = num
rem = 0
rev = 0
while(num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = int(num/10)

if temp == rev:
    print("The {} number is palindrome!".format(temp))
else:
    print("The {} number is not a palindrome!".format(temp))
