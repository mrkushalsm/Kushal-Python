L = [3, 1, 4]
M = [1, 5, 9]
N = [L[0] + M[0], L[1] + M[1], L[2] + M[2]]
print(N)

# OR

L = eval(input("Enter list 1: "))
M = eval(input("Enter list 2: "))
N = []
for i in range(len(L)):
    N.append(L[i] + M[i])
print(N)
