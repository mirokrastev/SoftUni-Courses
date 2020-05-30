def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)


def change_matrix(command, c_one, c_two, value):
    if c_one <= -1 or c_two <= -1:
        print('Invalid coordinates')
        return

    try:
        if command == 'Add':
            matrix[c_one][c_two] += value
        elif command == 'Subtract':
            matrix[c_one][c_two] -= value
    except IndexError:
        print('Invalid coordinates')


def print_matrix(matrix):
    [print(*i, sep=' ') for i in matrix]


rows_columns = int(input())
matrix = []
[add_matrix() for i in range(rows_columns)]

while True:
    arg = input()
    if arg == 'END':
        print_matrix(matrix)
        break

    command, c_one, c_two, value = arg.split()

    change_matrix(command, int(c_one), int(c_two), int(value))