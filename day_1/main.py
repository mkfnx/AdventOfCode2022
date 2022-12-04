from common import exec_solution


def calorie_counting_1(item_calories_list):
    max_calories = 0

    for elf_calories in item_calories_list.split("\n\n"):
        elf_calories_sum = sum([int(cal) for cal in elf_calories.split("\n")])
        if elf_calories_sum > max_calories:
            max_calories = elf_calories_sum

    return max_calories


def calorie_counting_2(item_calories_list):
    top_calories = []

    for elf_calories in item_calories_list.split("\n\n"):
        elf_calories_sum = sum([int(cal) for cal in elf_calories.split("\n")])
        top_calories.append(elf_calories_sum)

    top_calories.sort(reverse=True)

    calories_sum = 0
    for i in range(3):
        calories_sum += top_calories[i]

    return calories_sum


if __name__ == '__main__':
    exec_solution(calorie_counting_1)
    exec_solution(calorie_counting_2)
