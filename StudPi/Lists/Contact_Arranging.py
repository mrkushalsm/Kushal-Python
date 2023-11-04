names = ["Ria", "Aman", "Priya", "Rahul", "Arnav"]
numbers = [123, 456, 789, 101112, 131415]

for i in range(0, 5):
    for j in range(0, 5 - i - 1):
        if names[j] > names[j + 1]:
            name_temp = names[j]
            number_temp = numbers[j]
            names[j] = names[j + 1]
            numbers[j] = numbers[j + 1]
            names[j + 1] = name_temp
            numbers[j + 1] = number_temp

print(names)
print(numbers)
