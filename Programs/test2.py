from random import randrange

board_list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
free_fields = [(100, 100)]


def display_board(board):
    x = randrange(3)
    y = randrange(3)
    if board[x][y] != "X" and board[x][y] != "O":
        board[x][y] = "X"
        make_list_of_free_fields(board)
    else:
        display_board(board)

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0], board[0][1], board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0], board[1][1], board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0], board[2][1], board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")

    if victory_for(board, "X"):
        print("Computer wins!")
        exit(0)
    elif victory_for(board, "O"):
        print("You win!")
        exit(0)
    elif draw_move(board):
        print("Draw!")
        exit(0)
    else:
        free_fields.clear()
        enter_move(board)


def enter_move(board):
    num = input("Enter the number you wanna place \"O\": ")
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" or board[i][j] != "O":
                if board[i][j] == num:
                    board[i][j] = "O"
            else:
                print("Square already taken by opponent!")
                enter_move(board)

    make_list_of_free_fields(board)
    if victory_for(board, "X"):
        draw_move(board)
    elif victory_for(board, "O"):
        print("You win!")
        exit(0)
    elif draw_move(board):
        display_board(board)
    else:
        free_fields.clear()
        display_board(board)


def make_list_of_free_fields(board):
    for x in board:
        for y in x:
            if y != "X" and y != "O":
                free_fields.append((board.index(x), board[board.index(x)].index(y)))


def victory_for(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or (
            board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or (
            board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or (
            board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (
            board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or (
            board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or (
            board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or (
            board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False


def draw_move(board):
    if len(free_fields) == 1:
        return board, True


display_board(board_list)
