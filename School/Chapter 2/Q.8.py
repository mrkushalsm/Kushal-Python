fibonacci, n1, n2 = (), 0, 1
count = 0
while count < 9:
    fibonacci += (n1,)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print(fibonacci)
