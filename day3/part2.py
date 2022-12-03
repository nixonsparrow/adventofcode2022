from utils import read_input
from part1 import get_priority


def divide_groups(all_elves):
    groups = []
    group = []
    for elf in all_elves:
        group.append(elf)
        if len(group) == 3:
            groups.append(group)
            group = []
    return groups


def find_badge(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item


if __name__ == '__main__':
    # all_elves = read_input("example.txt")
    all_elves = read_input("input.txt")

    total = 0
    for team in divide_groups(all_elves):
        total += get_priority(find_badge(team))
    print(total)
