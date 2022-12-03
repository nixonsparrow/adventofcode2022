def read_input(filename=None, day=None):
    filename = filename if filename else f"day{day}.txt"
    with open(filename, "r") as file:
        return file.read().split("\n")
