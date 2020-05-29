def add_matrix():
    global p, coals_matrix

    arg = input().split()
    for player in range(rows_columns):
        if arg[player] == 's':
            p = (len(matrix), player)
        elif arg[player] == 'c':
            coals_matrix += 1
    matrix.append(arg)


def move_player(before_moving):
    global p, coals_mined, coals_matrix, death

    if p[0] <= -1 or p[1] <= -1 or p[0] >= len(matrix) or p[1] >= len(matrix):
        p = before_moving
        matrix[p[0]][p[1]] = 's'
        return

    if matrix[p[0]][p[1]] == 'c':
        coals_mined += 1
        coals_matrix -= 1
    elif matrix[p[0]][p[1]] == 'e':
        print(f'Game over! {p}')
        exit()

    matrix[p[0]][p[1]] = 's'


rows_columns = int(input())
move_commands = input().split()
matrix = []
p = (0, 0)
coals_matrix = 0
coals_mined = 0
[add_matrix() for i in range(rows_columns)]

for command in move_commands:
    before_moving = p
    if command == 'left':
        p = (p[0], p[1]-1)
    elif command == 'right':
        p = (p[0], p[1]+1)
    elif command == 'down':
        p = (p[0]+1, p[1])
    elif command == 'up':
        p = (p[0]-1, p[1])

    matrix[before_moving[0]][before_moving[1]] = '*'

    move_player(before_moving)

if not coals_matrix:
    print(f'You collected all coals! {p}')
elif coals_matrix:
    print(f'{coals_matrix} coals left. {p}')