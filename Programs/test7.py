T = int(input())
if T < 4:
    print("Yes")
else:
    for i in range(T):
        block_len = int(input())
        block_elements = input()
        elements_list = block_elements.split()
        block = []
        for i in range(block_len):
            block.append(int(elements_list[i]))

        if block[0] > block[3] and block[-2] > block[3]:
            print("Yes")
        else:
            print("No")