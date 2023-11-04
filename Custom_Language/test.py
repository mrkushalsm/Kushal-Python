# x^2 - 3x - 4

while True:
    a = 0
    b = 0
    c = 0
    equation = input("Enter your quadratic equation: ")
    equation_split = equation.split()
    if equation_split[0][0: equation_split[0].index("x")] == "":
        a = 1
    else:
        a = int(equation_split[0][0: equation_split[0].index("x")])

    if equation_split[2][0: equation_split[2].index("x")] == "":
        b = int(equation_split[1] + str(1))
    else:
        b = int(equation_split[1] + equation_split[2][0: equation_split[2].index("x")])

    c = int(equation_split[3] + equation_split[4])

    equation_split.pop(1)
    equation_split.pop(1)

    for i in range(1, (abs(a * c) + 1)):
        for j in range(i, (abs(a * c) + 1)):
            if i * j == abs(a * c):
                if int("-" + str(i)) + j == b:
                    if int("-" + str(i)) * j == (a * c):
                        equation_split.insert(1, "-")
                        equation_split.insert(2, str(i) + "x")
                        equation_split.insert(3, "+")
                        equation_split.insert(4, str(j) + "x")
                        break
                elif i + int("-" + str(j)) == b:
                    if i * int("-" + str(j)) == (a * c):
                        equation_split.insert(1, "+")
                        equation_split.insert(2, str(i) + "x")
                        equation_split.insert(3, "-")
                        equation_split.insert(4, str(j) + "x")
                        break
                elif int("-" + str(i)) + int("-" + str(j)):
                    if int("-" + str(i)) * int("-" + str(j)) == (a * c):
                        equation_split.insert(1, "-")
                        equation_split.insert(2, str(i) + "x")
                        equation_split.insert(3, "-")
                        equation_split.insert(4, str(j) + "x")
                        break
                elif i + j == b:
                    if i * j == (a * c):
                        equation_split.insert(1, "+")
                        equation_split.insert(2, str(i) + "x")
                        equation_split.insert(3, "+")
                        equation_split.insert(4, str(j) + "x")
                        break

    print(equation_split)

    equation_final = "x(x - " + equation_split[2][0: equation_split[2].index("x")] + equation_split[3]