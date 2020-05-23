matrix = []

def add_matrix():
    arg = input().split()
    matrix.append(arg)


def fn(row_one, col_one, row_two, col_two):
    first_eval = matrix[row_one][col_one]
    second_eval = matrix[row_two][col_two]

    matrix[row_one][col_one] = second_eval
    matrix[row_two][col_two] = first_eval

    [print(*i, sep=' ') for i in matrix]

def inp_process(arg):
    row_one = int(arg[1])
    col_one = int(arg[2])
    row_two = int(arg[3])
    col_two = int(arg[4])

    if all([row_one <= len(matrix) - 1, row_two <= len(matrix) - 1]) and \
            all([col_one <= len(matrix[0]) - 1, col_two <= len(matrix[0]) - 1]):
        fn(row_one, col_one, row_two, col_two)
    else:
        print('Invalid input!')

rows, columns = list(map(int, input().split()))
[add_matrix() for i in range(rows)]

while True:
    inp = input().split()
    command = inp[0]
    if command == 'END':
        exit()
    if command == 'swap':
        if len(inp) == 5:
            inp_process(inp)
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')