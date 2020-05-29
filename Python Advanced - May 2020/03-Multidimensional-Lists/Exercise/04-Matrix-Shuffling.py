def add_matrix():
    arg = input().split()
    matrix.append(arg)


def swap_matrix_el(coordinate):
    first_inx, second_inx = coordinate[0][1]
    third_inx, fourth_inx = coordinate[1][1]
    matrix[first_inx][second_inx] = coordinate[1][0]
    matrix[third_inx][fourth_inx] = coordinate[0][0]


def print_matrix():
    [print(*i, sep=' ') for i in matrix]


rows, columns = [int(i) for i in input().split()]
matrix = []
[add_matrix() for i in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] == 'swap':
        try:
            one, two, tree, four = map(int, command[1:])
            coordinates = {
                0: [matrix[one][two], (one, two)],
                1: [matrix[tree][four], (tree, four)],
            }
            swap_matrix_el(coordinates)
            print_matrix()
        except:
            print('Invalid input!')
    else:
        print('Invalid input!')