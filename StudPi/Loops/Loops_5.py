print("Enter the first real number: ")
num_x = int(input())
print("Enter the first imaginary number: ")
num_y = int(input())
print("Enter the second real number: ")
num2_x = int(input())
print("Enter the second imaginary number: ")
num2_y = int(input())

num = complex(num_x, num_y)
num2 = complex(num2_x, num2_y)

prod = num + num2

print("Sum of given complex numbers are", prod)