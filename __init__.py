import os

if __name__ == '__main__':
    for x in range(4, 26):
        try:
            os.mkdir(f"day{x}")
        except FileExistsError:
            pass
        with open(f"day{x}/__init__.py", "w"):
            pass
        with open(f"day{x}/part1.py", "w") as file:
            file.write("from utils import read_input\n\nif __name__ == '__main__':\n    pass\n")
        with open(f"day{x}/part2.py", "w") as file:
            file.write("from utils import read_input\n\nif __name__ == '__main__':\n    pass\n")
        with open(f"day{x}/input.txt", "w"):
            pass
        with open(f"day{x}/example.txt", "w"):
            pass
