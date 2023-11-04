for i in range(1, 6):
    char = ord('A')
    for j in range(1, 7 - i):
        print(chr(char), end=" ")
        char += 1
    print()
