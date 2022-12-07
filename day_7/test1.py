from common import exec_solution


class Node:
    def __init__(self, name, size, parent, is_dir):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        self.size_added = False
        self.children = {}


DIR_SIZE_LIMIT = 100000

def add_dir_size_to_parent(current_dir, small_dirs):
    if current_dir.name != '/' and not current_dir.size_added:
        current_dir.parent.size += current_dir.size
        current_dir.size_added = True
        remove_dir_if_big(current_dir.parent, small_dirs)

        add_dir_size_to_parent(current_dir.parent, small_dirs)

def remove_dir_if_big(current_dir, small_dirs):
    if current_dir.size > DIR_SIZE_LIMIT and current_dir.name in small_dirs:
        del small_dirs[current_dir.name]

        if current_dir.parent:
            remove_dir_if_big(current_dir.parent, small_dirs)

def no_space_1(file_input):
    root = Node('/', 0, None, True)
    current_node = root
    small_dirs = {'/': root}

    for line in file_input.split('\n'):
        tokens = line.split(' ')
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                dir_name = tokens[2]
                if dir_name == '/':
                    add_dir_size_to_parent(current_node, small_dirs)
                    current_node = root
                elif dir_name == '..':
                    add_dir_size_to_parent(current_node, small_dirs)
                    current_node = current_node.parent
                else:
                    current_node = current_node.children[dir_name]
        elif tokens[0] == 'dir':
            dir_name = tokens[1]
            dir_node = Node(dir_name, 0, current_node, True)
            current_node.children[dir_name] = dir_node

            small_dirs[dir_name] = dir_node
        else:  # file line, starts with file size
            file_name = tokens[1]
            file_size = int(tokens[0])
            file_node = Node(file_name, file_size, current_node, False)
            current_node.children[file_name] = file_node
            current_node.size += file_size

            remove_dir_if_big(current_node, small_dirs)

    small_dir_size_sum = 0
    for node_name, node in small_dirs.items():
        small_dir_size_sum += node.size

    return small_dir_size_sum


def no_space_2(file_input):
    pass


if __name__ == '__main__':
    exec_solution(no_space_1)
    # 889223 too low
    # exec_solution(no_space_2)
