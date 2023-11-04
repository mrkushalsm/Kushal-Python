"""
Pattern:-

1 2 3 4 5 6 7 8 9
  2 3 4 5 6 7 8
    3 4 5 6 7
      4 5 6
        5

"""

"""
string = ""
for key in range(0, 5):
    for j in range(1, 10 - (2 * key)):
        string += str(j + key) + " "
    for a in range(key):
        print("  ", end="")
    print(string)
    string = ""
"""

snake_x, snake_y = 1, 10
for i in range(0, 5):
    for a in range(i):
        print(" ", end="")
    for j in range(snake_x, snake_y):
        print(j, end="")
    print()
    snake_x += 1
    snake_y -= 1
