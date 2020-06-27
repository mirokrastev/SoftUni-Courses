def add_matrix():
    global santa_pos, good_kids, good_kids_raw

    arg = input().split()
    if 'S' in arg:
        santa_pos = [len(matrix), arg.index('S')]
    good_kids += arg.count('V')
    good_kids_raw += arg.count('V')
    matrix.append(arg)


def coordinates(matrix):
    return {'left': [matrix[0], matrix[1] - 1], 'right': [matrix[0], matrix[1] + 1],
            'up': [matrix[0] - 1, matrix[1]], 'down': [matrix[0] + 1, matrix[1]]}


def move_santa(coordinate):
    global santa_pos, presents, good_kids

    local_coord = coordinates(santa_pos)[coordinate]

    if local_coord[0] <= -1 or local_coord[1] <= -1:
        return

    try:
        if matrix[local_coord[0]][local_coord[1]] == 'V':
            good_kids -= 1
            presents -= 1
        if matrix[local_coord[0]][local_coord[1]] == 'C':
            matrix[santa_pos[0]][santa_pos[1]] = '-'
            matrix[local_coord[0]][local_coord[1]] = 'S'
            santa_pos = local_coord
            return cookie()

        matrix[santa_pos[0]][santa_pos[1]] = '-'
        matrix[local_coord[0]][local_coord[1]] = 'S'
        santa_pos = local_coord
    except IndexError: return


def cookie():
    global presents, good_kids

    for pos in coordinates(santa_pos):
        if presents <= 0: return

        local_coord = coordinates(santa_pos)[pos]
        if local_coord[0] <= -1 or local_coord[1] <= -1:
            continue

        try:
            if matrix[local_coord[0]][local_coord[1]] != '-':
                if matrix[local_coord[0]][local_coord[1]] == 'V': good_kids -= 1
                presents -= 1
                matrix[local_coord[0]][local_coord[1]] = '-'
        except IndexError: continue


presents = int(input())
rows_columns = int(input())
matrix = []
santa_pos = []
good_kids = 0
good_kids_raw = 0
[add_matrix() for i in range(rows_columns)]

while presents:
    inp = input()

    if inp == 'Christmas morning':
        break

    move_santa(inp)

if presents <= 0 and good_kids >= 1:
    print('Santa ran out of presents!')
[print(*i, sep=' ') for i in matrix]
if good_kids <= 0:
    print(f'Good job, Santa! {good_kids_raw} happy nice kid/s.')
else:
    print(f'No presents for {good_kids} nice kid/s.')