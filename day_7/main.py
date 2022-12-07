from common import exec_solution


class Node:
    def __init__(self, name, size, parent, is_dir):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        self.size_added = False
        self.children = {}


def print_msg(node, level):
    msg = ''
    tabs = '  ' * level

    if node.is_dir:
        msg = 'dir'
    else:
        msg = f'file, size={node.size:,}'

    print(f'{tabs}- {node.name} ({msg})')


def print_filesystem(root, level=0):
    print_msg(root, level)

    for c in root.children.values():
        print_filesystem(c, level + 1)


def build_tree(file_input):
    root = Node('/', 0, None, True)
    current_node = root

    for line in file_input.split('\n'):
        tokens = line.split(' ')
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                dir_name = tokens[2]
                if dir_name == '/':
                    current_node = root
                elif dir_name == '..':
                    current_node = current_node.parent
                else:
                    current_node = current_node.children[dir_name]
        elif tokens[0] == 'dir':
            dir_name = tokens[1]
            dir_node = Node(dir_name, 0, current_node, True)
            current_node.children[dir_name] = dir_node
        else:  # file line, starts with file size
            file_name = tokens[1]
            file_size = int(tokens[0])
            file_node = Node(file_name, file_size, current_node, False)
            current_node.children[file_name] = file_node
            current_node.size += file_size

    return root


def find_small_dirs(dir_node, small_dirs, max_dir_size):
    contents_size_sum = 0

    for node in dir_node.children.values():
        if not node.is_dir:
            contents_size_sum += node.size
        else:
            contents_size_sum += find_small_dirs(node, small_dirs, max_dir_size)

    dir_node.size = contents_size_sum

    if contents_size_sum <= max_dir_size:
        small_dirs.append(dir_node)

    return contents_size_sum


def no_space_1(file_input):
    root = build_tree(file_input)

    small_dirs = []
    find_small_dirs(root, small_dirs, 100000)

    small_dirs_sum = 0
    for d in small_dirs:
        small_dirs_sum += d.size

    return small_dirs_sum


def get_root_dir_size(root):
    contents_size_sum = 0

    for node in root.children.values():
        if not node.is_dir:
            contents_size_sum += node.size
        else:
            contents_size_sum += get_root_dir_size(node)

    return contents_size_sum


def get_dirs_with_size(root, required_size, dirs):
    contents_size_sum = 0

    for node in root.children.values():
        if not node.is_dir:
            contents_size_sum += node.size
        else:
            contents_size_sum += get_dirs_with_size(node, required_size, dirs)

    root.size = contents_size_sum

    if contents_size_sum >= required_size:
        dirs.append(root)

    return contents_size_sum


def no_space_2(file_input):
    root = build_tree(file_input)
    root_size = get_root_dir_size(root)
    free_space = 70000000 - root_size
    needed_space = 30000000 - free_space

    dirs_with_required_size = []
    get_dirs_with_size(root, needed_space, dirs_with_required_size)
    return min(dirs_with_required_size, key=lambda x: x.size).size


if __name__ == '__main__':
    exec_solution(no_space_1)
    exec_solution(no_space_2)
