from part1 import prepare_input


def check_overlap(range_a, range_b):
    for i in range_a:
        if i in range_b:
            return True
    return False


if __name__ == '__main__':
    total = 0
    for x, y in prepare_input("input.txt"):
        if check_overlap(x, y):
            total += 1
    print(total)
