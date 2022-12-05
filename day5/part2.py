from utils import read_input

from part1 import Stack, Warehouse


class NewStack(Stack):
    def place_containers(self, containers):
        containers.reverse()
        return super().place_containers(containers)


class NewWarehouse(Warehouse):
    def __init__(self, stacks_input, stack_model=NewStack):
        super().__init__(stacks_input, stack_model)


if __name__ == '__main__':
    # filename = "example.txt"
    filename = "input.txt"
    warehouse = NewWarehouse(read_input(filename))
    moves = [move for move in read_input(filename) if move.startswith("move")]
    for move in moves:
        warehouse.make_a_move(move)
    print(warehouse.get_stacks_tops())
