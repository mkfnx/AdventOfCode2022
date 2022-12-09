from common import exec_solution


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'


def rope_bridge_1(file_input):
    tail_visited = set()
    head_pos, tail_pos = Position(), Position()
    tail_visited.add(str(tail_pos))

    for head_movements in file_input.split('\n'):
        movement_direction, steps = head_movements.split(' ')

        for i in range(int(steps)):
            previous_head = Position(head_pos.x, head_pos.y)

            if movement_direction == 'L':
                head_pos.x -= 1
            elif movement_direction == 'R':
                head_pos.x += 1
            elif movement_direction == 'U':
                head_pos.y += 1
            else:  # D
                head_pos.y -= 1

            diff_x = head_pos.x - tail_pos.x
            diff_y = head_pos.y - tail_pos.y
            previous_tail_pos = Position(tail_pos.x, tail_pos.y)

            if (diff_x == 0 and diff_y == 0) or (abs(diff_x) + abs(diff_y) == 1) or (
                    abs(diff_x) == 1 and abs(diff_y) == 1):
                continue
            else:
                tail_pos.x, tail_pos.y = previous_head.x, previous_head.y

            if previous_tail_pos.x != tail_pos.x or previous_tail_pos.y != tail_pos.y:
                tail_visited.add(str(tail_pos))

    return len(tail_visited)


def rope_bridge_2(file_input):
    tail_visited = set()
    knots = [Position(11, 5) for i in range(10)]
    tail_visited.add(str(knots[9]))

    for head_movements in file_input.split('\n'):
        movement_direction, steps = head_movements.split(' ')

        for i in range(int(steps)):
            previous_head = Position(knots[0].x, knots[0].y)

            if movement_direction == 'L':
                knots[0].x -= 1
            elif movement_direction == 'R':
                knots[0].x += 1
            elif movement_direction == 'U':
                knots[0].y += 1
            else:  # D
                knots[0].y -= 1

            for ti in range(1, len(knots)):
                diff_x = knots[ti - 1].x - knots[ti].x
                diff_y = knots[ti - 1].y - knots[ti].y
                previous_tail_pos = Position(knots[ti].x, knots[ti].y)

                if (diff_x != 0 and diff_y != 0) and (abs(diff_x) + abs(diff_y) > 2):
                    previous_head.x, previous_head.y = knots[ti].x, knots[ti].y
                    if diff_x > 0 and diff_y > 0:
                        knots[ti].x += 1
                        knots[ti].y += 1
                    elif diff_x > 0 > diff_y:
                        knots[ti].x += 1
                        knots[ti].y -= 1
                    elif diff_x < 0 and diff_y < 0:
                        knots[ti].x -= 1
                        knots[ti].y -= 1
                    else:  # diff_x < 0 and diff_y > 0
                        knots[ti].x -= 1
                        knots[ti].y += 1
                elif (diff_x == 0 and diff_y == 0) or (abs(diff_x) + abs(diff_y) == 1) or (
                        abs(diff_x) == 1 and abs(diff_y) == 1):
                    continue
                else:
                    if diff_y == 0:
                        if diff_x == -2:
                            knots[ti].x -= 1
                        elif diff_x == 2:
                            knots[ti].x += 1
                    elif diff_x == 0:
                        if diff_y == -2:
                            knots[ti].y -= 1
                        elif diff_y == 2:
                            knots[ti].y += 1
                    elif diff_y == 1:
                        if diff_x == -2:
                            knots[ti].x -= 1
                            knots[ti].y += 1
                        elif diff_x == 2:
                            knots[ti].x += 1
                            knots[ti].y += 1
                    elif diff_y == -1:
                        if diff_x == -2:
                            knots[ti].x -= 1
                            knots[ti].y -= 1
                        elif diff_x == 2:
                            knots[ti].x += 1
                            knots[ti].y -= 1
                    elif diff_x == 1:
                        if diff_y == -2:
                            knots[ti].x += 1
                            knots[ti].y -= 1
                        elif diff_y == 2:
                            knots[ti].x += 1
                            knots[ti].y += 1
                    elif diff_x == -1:
                        if diff_y == -2:
                            knots[ti].x -= 1
                            knots[ti].y -= 1
                        elif diff_y == 2:
                            knots[ti].x -= 1
                            knots[ti].y += 1
                if ti == 9 and (previous_tail_pos.x != knots[ti].x or previous_tail_pos.y != knots[ti].y):
                    tail_visited.add(str(knots[ti]))

    return len(tail_visited)


if __name__ == '__main__':
    exec_solution(rope_bridge_1)
    exec_solution(rope_bridge_2)
