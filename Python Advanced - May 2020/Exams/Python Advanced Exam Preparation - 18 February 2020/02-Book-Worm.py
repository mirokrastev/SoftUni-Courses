def add_matrix():
    global worm_coord

    arg = list(input())
    if 'P' in arg:
        worm_coord = [len(matrix), arg.index('P')]
    matrix.append(arg)


def coordinates(coord):
    return {'right': [coord[0], coord[1] + 1], 'left': [coord[0], coord[1] - 1],
            'up': [coord[0] - 1, coord[1]], 'down': [coord[0] + 1, coord[1]]}


def move_worm(side):
    global worm_coord, initial_string

    local_coord = coordinates(worm_coord)[side]

    if local_coord[0] <= -1 or local_coord[1] <= -1:
        initial_string.pop() if initial_string else None
        return

    try:
        if matrix[local_coord[0]][local_coord[1]] != '-':
            initial_string.append(matrix[local_coord[0]][local_coord[1]])
        matrix[worm_coord[0]][worm_coord[1]] = '-'
        worm_coord = local_coord
        matrix[worm_coord[0]][worm_coord[1]] = 'P'
    except IndexError:
        initial_string.pop() if initial_string else None


initial_string = list(input())
rows_columns = int(input())
matrix = []
worm_coord = []
[add_matrix() for i in range(rows_columns)]
moves = int(input())

for i in range(moves):
    inp = input()
    move_worm(inp)

print("".join(initial_string))
[print(*i, sep='') for i in matrix]