from common import exec_solution


def treetop_1(file_input):
    forest = [[int(t) for t in line] for line in file_input.split('\n')]
    row = forest[0]
    perimeter = len(forest) * 2 + (len(row) - 2) * 2
    internal_visible = set()

    for i in range(1, len(forest) - 1):
        tallest = forest[i][0]
        for j in range(1, len(row) - 1):
            if forest[i][j] > tallest:
                internal_visible.add(f'{i},{j}')
                tallest = forest[i][j]

    for i in range(1, len(forest) - 1):
        tallest = forest[i][len(row) - 1]
        for j in range(len(row) - 2, 0, -1):
            if forest[i][j] > tallest:
                internal_visible.add(f'{i},{j}')
                tallest = forest[i][j]

    for j in range(1, len(forest) - 1):
        tallest = forest[0][j]
        for i in range(1, len(row) - 1):
            if forest[i][j] > tallest:
                internal_visible.add(f'{i},{j}')
                tallest = forest[i][j]

    for j in range(1, len(forest) - 1):
        tallest = forest[len(forest) - 1][j]
        for i in range(len(row) - 2, 0, -1):
            if forest[i][j] > tallest:
                internal_visible.add(f'{i},{j}')
                tallest = forest[i][j]

    return perimeter + len(internal_visible)


def treetop_2(file_input):
    forest = [[int(t) for t in line] for line in file_input.split('\n')]
    row = forest[0]

    scenic_score = 0

    for ii in range(1, len(forest) - 1):
        for jj in range(1, len(row) - 1):
            score_ltr = 0
            score_rtl = 0
            score_ttb = 0
            score_btt = 0

            for j in range(jj + 1, len(row)):
                score_ltr += 1
                if forest[ii][j] >= forest[ii][jj]:
                    break

            for j in range(jj - 1, -1, -1):
                score_rtl += 1
                if forest[ii][j] >= forest[ii][jj]:
                    break

            for i in range(ii + 1, len(forest)):
                score_ttb += 1
                if forest[i][jj] >= forest[ii][jj]:
                    break

            for i in range(ii - 1, -1, -1):
                score_btt += 1
                if forest[i][jj] >= forest[ii][jj]:
                    break

            scenic_score = max(score_ltr * score_rtl * score_ttb * score_btt, scenic_score)

    return scenic_score


if __name__ == '__main__':
    exec_solution(treetop_1)
    exec_solution(treetop_2)
