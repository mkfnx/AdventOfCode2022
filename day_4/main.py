from common import exec_solution


def camp_cleanup_1(file_content):
    full_overlaps = 0

    for pair in file_content.split('\n'):
        p1, p2 = pair.split(',')

        s1, e1 = [int(i) for i in p1.split('-')]
        s2, e2 = [int(i) for i in p2.split('-')]

        if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
            full_overlaps += 1

    return full_overlaps


def camp_cleanup_2(file_content):
    no_overlap = 0
    pairs_count = 0

    for pair in file_content.split('\n'):
        pairs_count += 1
        pair_1, pair_2 = pair.split(',')

        start_1, end_1 = [int(i) for i in pair_1.split('-')]
        start_2, end_2 = [int(i) for i in pair_2.split('-')]

        if end_1 < start_2 or end_2 < start_1 or start_1 > end_2 or start_2 > end_1:
            no_overlap += 1

    return pairs_count - no_overlap


if __name__ == '__main__':
    exec_solution(camp_cleanup_1)
    exec_solution(camp_cleanup_2)
