from common import exec_solution

own_play_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def get_outcome_score(opponents_play, own_play):
    if opponents_play == 'A':
        if own_play == 'X':
            return 3
        elif own_play == 'Y':
            return 6
        else:
            return 0
    elif opponents_play == 'B':
        if own_play == 'X':
            return 0
        elif own_play == 'Y':
            return 3
        else:
            return 6
    else:  # opponent plays 'C'
        if own_play == 'X':
            return 6
        elif own_play == 'Y':
            return 0
        else:
            return 3


def rps_1(guide):
    total_score = 0
    for line in guide.split('\n'):
        plays = line.split(' ')
        opponents_play, own_play = plays
        round_score = own_play_score[own_play] + get_outcome_score(opponents_play, own_play)
        total_score += round_score

    return total_score


def get_own_play(opponents_play, desired_outcome):
    if opponents_play == 'A':
        if desired_outcome == 'X':
            return 'Z'
        elif desired_outcome == 'Y':
            return 'X'
        else:
            return 'Y'
    elif opponents_play == 'B':
        if desired_outcome == 'X':
            return 'X'
        elif desired_outcome == 'Y':
            return 'Y'
        else:
            return 'Z'
    else:  # opponent plays 'C'
        if desired_outcome == 'X':
            return 'Y'
        elif desired_outcome == 'Y':
            return 'Z'
        else:
            return 'X'


def rps_2(guide):
    total_score = 0
    for instructions_line in guide.split('\n'):
        opponents_play, desired_outcome = instructions_line.split(' ')
        own_play = get_own_play(opponents_play, desired_outcome)
        round_score = own_play_score[own_play] + get_outcome_score(opponents_play, own_play)
        total_score += round_score

    return total_score


if __name__ == "__main__":
    exec_solution(rps_1)
    exec_solution(rps_2)
