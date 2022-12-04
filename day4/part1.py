from utils import read_input


def encode_ranges(pair_of_ranges):
    a, b = pair_of_ranges.split(',')[0], pair_of_ranges.split(',')[1]
    return range(int(a.split('-')[0]), int(a.split('-')[1]) + 1), range(int(b.split('-')[0]), int(b.split('-')[1]) + 1)


def prepare_input(the_input):
    for pair in read_input(the_input):
        yield encode_ranges(pair)


def check_if_range_includes_other_range(range_a, range_b):
    included = 0
    for i in range_a:
        if i in range_b:
            included += 1
    return included == len(range_a)


def check_ranges(range_a, range_b):
    if not check_if_range_includes_other_range(range_a, range_b):
        if not check_if_range_includes_other_range(range_b, range_a):
            return False
    return True


if __name__ == '__main__':
    total = 0
    for x, y in prepare_input("input.txt"):
        if check_ranges(x, y):
            total += 1
    print(total)
