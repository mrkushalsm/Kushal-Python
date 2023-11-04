from random import randrange

print(randrange(1, 4))

if (x, y) not in free_fields:
    print("Can't place there")
else:
    if board[i][j] == num:
        board[i][j] = "X"