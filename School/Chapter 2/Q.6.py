list1, sum = [], 0
for num in range(101):
    for num_sum in str(num):
        sum += int(num_sum)
    if num % 3 == 0 or str(num)[-1] == "0" or str(num)[-1] == "5":
        list1.append(num)
print(list1)
