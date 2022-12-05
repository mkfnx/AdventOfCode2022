import re
from common import exec_solution


def stacks_from_drawing(drawing):
    drawing_parts = drawing.split('\n')
    stack_contents = drawing_parts[:-1]
    stack_numbers = drawing_parts[-1]
    stacks_count = int(stack_numbers.split(' ')[-1])

    stacks = []
    for i in range(stacks_count):
        stacks.append([])

    for line in stack_contents:
        i = 0
        while i < len(line):
            item_chunk = line[i:i + 3]
            if item_chunk[1].isalpha():
                stacks[i // 4].insert(0, item_chunk[1])
            i += 4

    return stacks


def supply_stacks_1(file_content):
    drawing, instructions = file_content.split('\n\n')
    stacks = stacks_from_drawing(drawing)

    for line in instructions.split('\n'):
        instruction_chunks = line.split(' ')
        items_count = int(instruction_chunks[1])
        from_stack = int(instruction_chunks[3])
        to_stack = int(instruction_chunks[5])

        for i in range(items_count):
            crate = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(crate)

    return ''.join([stack[-1] for stack in stacks])


def supply_stacks_2(file_content):
    drawing, instructions = file_content.split('\n\n')
    stacks = stacks_from_drawing(drawing)

    for line in instructions.split('\n'):
        instruction_chunks = line.split(' ')
        items_count = int(instruction_chunks[1])
        from_stack = int(instruction_chunks[3])
        to_stack = int(instruction_chunks[5])

        crates = stacks[from_stack - 1][-items_count:]
        del stacks[from_stack - 1][-items_count:]
        stacks[to_stack - 1].extend(crates)

    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    exec_solution(supply_stacks_1)
    exec_solution(supply_stacks_2)
