from os import system, name
import random

maze = [["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢", "▢"]]


snake_x = random.randint(0, 8)
snake_y = random.randint(0, 8)
maze[snake_x][snake_y] = "▣"

fruit_x = random.randint(0, 8)
fruit_y = random.randint(0, 8)
maze[fruit_x][fruit_y] = "●"

snake_extend_x, snake_extend_y = None, None


def game_map():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end=" ")
        print()


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def boundary_loop(cord):
    global snake_x, snake_y, snake_extend_x, snake_extend_y
    if cord == "x":
        if snake_x < 0 and snake_extend_x < 0:
            snake_x = len(maze) - 1
        elif snake_x > len(maze) - 1 and snake_extend_x > len(maze) - 1:
            snake_x = 0
    elif cord == "y":
        if snake_y < 0 and snake_extend_y < 0:
            snake_y = len(maze[snake_x]) - 1
        elif snake_y > len(maze[snake_x]) - 1 and snake_extend_y > len(maze[snake_x]) - 1:
            snake_y = 0


def eat_fruit(moved_key):
    if maze[snake_extend_x][snake_extend_y] == maze[fruit_x][fruit_y]:
        """if moved_key == "w":
            maze[snake_extend_x + 1][snake_extend_y] = "▣"
        elif moved_key == "a":
            maze[snake_extend_x][snake_extend_y + 1] = "▣"
        elif moved_key == "s":
            maze[snake_extend_x - 1][snake_extend_y] = "▣"
        elif moved_key == "d":
            maze[snake_extend_x][snake_extend_y - 1] = "▣"
        return True, snake_extend_x, snake_extend_y"""
        return True
    # return False, snake_extend_x, snake_extend_y
    return False


while True:
    clear()
    game_map()
    move_key = input("> ")
    maze[snake_x][snake_y] = "▢"
    # eat_fruit_check, snake_extend_x, snake_extend_y = eat_fruit(move_key)
    eat_fruit_check = eat_fruit(move_key)
    if move_key == "w":
        if eat_fruit_check:
            snake_extend_x = snake_x
        snake_x -= 1
        boundary_loop("x")
    elif move_key == "a":
        if eat_fruit_check:
            snake_extend_y = snake_y
        snake_y -= 1
        boundary_loop("y")
    elif move_key == "s":
        if eat_fruit_check:
            snake_extend_x = snake_x
        snake_x += 1
        boundary_loop("x")
    elif move_key == "d":
        if eat_fruit_check:
            snake_extend_y = snake_y
        snake_y += 1
        boundary_loop("y")
    elif move_key == "exit":
        exit()
    print(snake_x, ",", snake_y)
    maze[snake_x][snake_y] = "▣"
    maze[snake_extend_x][snake_extend_y] = "▣"
