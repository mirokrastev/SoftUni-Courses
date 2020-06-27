def add_matrix():
    global bunny_coord

    arg = input().split()
    matrix.append([])
    if 'B' in arg:
        bunny_coord = [len(matrix)-1, arg.index('B')]

    for i in arg:
        try:
            i = int(i)
        except ValueError: pass
        matrix[-1].append(i)


def coordinates(matrix):
    return {'right': [matrix[0], matrix[1] + 1], 'left': [matrix[0], matrix[1] - 1],
            'up': [matrix[0] - 1, matrix[1]], 'down': [matrix[0] + 1, matrix[1]]}


def sum_given_coordinate(coordinate, coords):
    local = coordinates(coords)[coordinate]
    if local[0] <= -1 or local[1] <= -1: return -9999999
    try:
        if matrix[local[0]][local[1]] == 'X': return -9999999
    except IndexError: return -9999999

    result = matrix[local[0]][local[1]]

    while True:
        local = coordinates(local)[coordinate]

        if local[0] <= -1 or local[1] <= -1: return result

        try:
            result += matrix[local[0]][local[1]]
        except (IndexError, TypeError): return result


rows_columns = int(input())
matrix = []
bunny_coord = []
[add_matrix() for i in range(rows_columns)]
move_var = {0: 'right', 1: 'left', 2: 'up', 3: 'down'}
ll = []

for key in move_var:
    ll.append(sum_given_coordinate(move_var[key], bunny_coord))

best_coord = move_var[ll.index(max(ll))]
print(best_coord)

while True:
    bunny_coord = coordinates(bunny_coord)[best_coord]
    if bunny_coord[0] <= -1 or bunny_coord[1] <= -1: break

    try:
        if matrix[bunny_coord[0]][bunny_coord[1]] == 'X': break
    except IndexError: break

    print(bunny_coord)
print(max(ll))