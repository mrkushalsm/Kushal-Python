sum = 1
i = 1
while True:
    if sum == 1:
        print(i, "is not infinitely large")
        i += 1
        sum = i
    else:
        if sum % 2 == 0:
            sum /= 2
        else:
            sum = (sum * 3) + 1

