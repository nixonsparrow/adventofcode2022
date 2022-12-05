from utils import read_input


class NotEnoughContainers(IndexError):
    pass


class Stack:
    def __init__(self, nr, containers):
        self.nr = nr
        self.containers = containers

    def __repr__(self):
        return f"Stack ({self.nr}): {self.containers}"

    def pick_containers(self, count=1):
        if count > len(self.containers):
            raise NotEnoughContainers
        containers = []
        for i in range(count):
            containers.append(self.containers.pop())

        return containers

    def place_containers(self, containers):
        self.containers += containers
        return self.containers


class Warehouse:
    def __init__(self, stacks_input, stack_model=Stack):
        self.stacks = self.create_stacks(stacks_input, stack_model)

    def __str__(self):
        return f"{self.stacks}"

    @staticmethod
    def create_stacks(stack_input, stack_model):
        pre_stacks = {}
        for row in stack_input:
            if "[" not in row:
                for i in row.split():
                    pre_stacks.update({int(i): []})
                break

        for row in stack_input:
            if "[" in row:  # building stacks
                for i in range(len(row)):
                    position = i * 4 + 1
                    try:
                        if row[position].strip():
                            pre_stacks[i + 1] += [row[position]]
                    except IndexError:
                        pass
            else:
                break

        stacks = []
        for nr, containers in pre_stacks.items():
            containers.reverse()
            stacks.append(stack_model(nr, containers))
        return stacks

    def make_a_move(self, move):
        parts = move.split()
        quantity, nr_from, nr_to = int(parts[1]), int(parts[3]), int(parts[5])
        stack_from, stack_to = self.find_stack(nr_from), self.find_stack(nr_to)
        containers = stack_from.pick_containers(quantity)
        stack_to.place_containers(containers)

    def find_stack(self, nr):
        for stack in self.stacks:
            if stack.nr == nr:
                return stack

    def get_stacks_tops(self):
        return ''.join([top.containers[-1] for top in self.stacks])


if __name__ == '__main__':
    # filename = "example.txt"
    filename = "input.txt"
    warehouse = Warehouse(read_input(filename))
    moves = [move for move in read_input(filename) if move.startswith("move")]
    for move in moves:
        warehouse.make_a_move(move)
    print(warehouse.get_stacks_tops())
