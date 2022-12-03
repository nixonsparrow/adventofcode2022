import string
from utils import read_input


def split_rucksack(rucksack):
    return rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]


def find_similar_item(rucksack_a, rucksack_b):
    for item in rucksack_a:
        if item in rucksack_b:
            return item


def get_priority(item):
    if not item:
        return
    if not item.isupper():
        alphabet = list(string.ascii_lowercase)
        return alphabet.index(item) + 1
    else:
        alphabet = list(string.ascii_uppercase)
        return alphabet.index(item) + 27


if __name__ == '__main__':
    # x = read_input("example.txt")
    x = read_input("input.txt")
    total = 0
    for y in x:
        a, b = split_rucksack(y)
        c = get_priority(find_similar_item(a, b))
        if c:
            total += c
    print(total)
