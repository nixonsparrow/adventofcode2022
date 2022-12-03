from utils import read_input


def day1_input(day="1"):
    elves = []
    elf = 0
    for x in read_input(day=day):
        try:
            elf += int(x)
        except ValueError:
            elves += [elf]
            elf = 0
    if elf:
        elves += [elf]
    return elves


if __name__ == '__main__':
    my_input = day1_input("1")
    calories = 0
    for i in range(3):
        calories += max(my_input)
        my_input.pop(my_input.index(max(my_input)))
    print(calories)
