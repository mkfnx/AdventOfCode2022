def exec_solution(func):
    try:
        with open('example.txt') as file:
            file_content = file.read()
            print(f'sample: {func(file_content)}')

        with open('input.txt') as file:
            file_content = file.read()
            print(f'result: {func(file_content)}')
    except FileNotFoundError as E:
        print(E)
    except ValueError:
        print('Error with file content')
