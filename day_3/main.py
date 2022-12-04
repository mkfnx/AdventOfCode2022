from common import exec_solution


def get_char_val(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 1 + 26


def rucksack_reorg_1(rucksack_list):
    items_to_rearrange = []
    for items in rucksack_list.split('\n'):
        items_per_compartment = int(len(items) / 2)
        c1, c2 = items[:items_per_compartment], items[items_per_compartment:]

        for item in c1:
            if item in c2:
                items_to_rearrange.append(item)
                break

    return sum([get_char_val(i) for i in items_to_rearrange])


def rucksack_reorg_2(file_content):
    badges = []
    rucksack_list = file_content.split('\n')

    for i in range(0, len(rucksack_list), 3):
        r1, r2, r3 = rucksack_list[i], rucksack_list[i + 1], rucksack_list[i + 2]

        for item in r1:
            if item in r2 and item in r3:
                badges.append(item)
                break

    return sum([get_char_val(b) for b in badges])


if __name__ == "__main__":
    exec_solution(rucksack_reorg_1)
    exec_solution(rucksack_reorg_2)
