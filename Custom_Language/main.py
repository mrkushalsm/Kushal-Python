commands = ["add", "subtract", "multiply", "divide"]


def main():
    while True:
        lang_input = input("kushal> ")
        compute_command(lang_input)


def check_command(lang_input):
    global commands
    for command in commands:
        if lang_input.startswith(command):
            compute_command(lang_input)
    print("Invalid command!")


def compute_command(lang_input):
    tokens = lang_input.split()
    print(tokens)
    if tokens[0] == "add":
        add_command()
    elif tokens[0] == "subtract":
        subtract_command()
    elif tokens[0] == "multiply":
        multiply_command()
    elif tokens[0] == "divide":
        divide_command()


def add_command():
    pass


def subtract_command():
    pass


def multiply_command():
    pass


def divide_command():
    pass


if __name__ == '__main__':
    main()
