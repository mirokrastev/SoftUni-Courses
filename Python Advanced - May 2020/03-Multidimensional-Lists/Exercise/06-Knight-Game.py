def add_matrix():
    arg = [i for i in input()]
    matrix.append(arg)


def make_indexes(row, column):
    return check_knight(
        {
            0: (row-2, column-1),
            1: (row-2, column+1),
            2: (row-1, column-2),
            3: (row-1, column+2),
            4: (row+1, column-2),
            5: (row+1, column+2),
            6: (row+2, column-1),
            7: (row+2, column+1)
        }
    )


def check_knight(coordinate):
    hit_knight = 0
    for row, col in coordinate.values():
        if row <= -1 or col <= -1:
            continue
        try:
            if matrix[row][col] == 'K':
                hit_knight += 1
        except: continue

    return hit_knight


rows = int(input())
matrix = []
[add_matrix() for i in range(rows)]
position = tuple()
deleted_knights = 0

while True:
    result = 0
    for row in range(rows):
        for column in range(len(matrix)):
            current_index = matrix[row][column]
            if current_index == 'K':
                var = make_indexes(row, column)
                if var > result:
                    result = var
                    position = (row, column)

    if result == 0:
        break

    matrix[position[0]][position[1]] = 'O'
    deleted_knights += 1

print(deleted_knights)