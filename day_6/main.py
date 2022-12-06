from common import exec_solution


def tuning(file_content, message_size):
    start = 0
    for i in range(message_size - 1, len(file_content)):
        s = set()
        for c in file_content[start:i + 1]:
            if c in s:
                break
            else:
                s.add(c)

        if len(s) == message_size:
            return i + 1

        start += 1


def tuning_1(file_content):
    return tuning(file_content, 4)


def tuning_2(file_content):
    return tuning(file_content, 14)


if __name__ == '__main__':
    exec_solution(tuning_1)
    exec_solution(tuning_2)
