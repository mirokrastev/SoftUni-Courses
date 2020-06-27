def add_matrix():
    global plane_coord, targets, raw_targets

    inp = input().split()
    matrix.append(inp)
    if 'p' in inp:
        plane_coord = [len(matrix) - 1, inp.index('p')]
    if 't' in inp:
        targets += inp.count('t')
        raw_targets += inp.count('t')


def coordinates(matrix):
    return {'right': [matrix[0], matrix[1] + 1], 'left': [matrix[0], matrix[1] - 1],
            'up': [matrix[0] - 1, matrix[1]], 'down': [matrix[0] + 1, matrix[1]]}


def shoot_plane(position, index):
    global targets
    local_coord = plane_coord

    for i in range(index):
        local_coord = coordinates(local_coord)[position]

    if local_coord[0] <= -1 or local_coord[1] <= -1: return

    try:
        if matrix[local_coord[0]][local_coord[1]] == 't':
            targets -= 1
        matrix[local_coord[0]][local_coord[1]] = 'x'
    except IndexError: return


def move_plane(position, index):
    global targets, plane_coord
    local_coord = plane_coord

    for i in range(index):
        local_coord = coordinates(local_coord)[position]

    if local_coord[0] <= -1 or local_coord[1] <= -1: return

    try:
        if matrix[local_coord[0]][local_coord[1]] != '.':
            return
        matrix[plane_coord[0]][plane_coord[1]] = '.'
        matrix[local_coord[0]][local_coord[1]] = 'p'
        plane_coord = local_coord
    except IndexError: return


rows_columns = int(input())
matrix = []
plane_coord = []
targets = 0
raw_targets = 0
[add_matrix() for i in range(rows_columns)]
commands_inp = int(input())

for i in range(commands_inp):
    command, position, index = input().split()

    if command == 'shoot':
        shoot_plane(position, int(index))
    elif command == 'move':
        move_plane(position ,int(index))

    if targets <= 0: break

if targets <= 0:
    print(f'Mission accomplished! All {raw_targets} targets destroyed.')
else:
    print(f' Mission failed! {targets} targets left.')
[print(*i, sep=' ') for i in matrix]