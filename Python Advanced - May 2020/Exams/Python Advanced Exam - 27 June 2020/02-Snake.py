def add_matrix():
    global snake_coord

    arg = list(input())

    if 'B' in arg:
        if not burrows_coord[0]:
            burrows_coord[0] = [len(matrix), arg.index('B')]
        else:
            burrows_coord[1] = [len(matrix), arg.index('B')]

    if 'S' in arg:
        snake_coord = [len(matrix), arg.index('S')]

    matrix.append(arg)


def coordinates(coord):
    return {'right': [coord[0], coord[1] + 1], 'left': [coord[0], coord[1] - 1],
            'up': [coord[0] - 1, coord[1]], 'down': [coord[0] + 1, coord[1]]}


def move_snake(side):
    global snake_coord, food_quantity

    snake_coord = coordinates(snake_coord)[side]

    if snake_coord[0] <= -1 or snake_coord[1] <= -1:
        print('Game over!')
        return info()

    try:
        if matrix[snake_coord[0]][snake_coord[1]] == 'B':
            matrix[snake_coord[0]][snake_coord[1]] = '.'
            if burrows_coord[0] == snake_coord:
                snake_coord = burrows_coord[1]

            elif burrows_coord[1] == snake_coord:
                snake_coord = burrows_coord[0]

        elif matrix[snake_coord[0]][snake_coord[1]] == '*':
            food_quantity += 1

        matrix[snake_coord[0]][snake_coord[1]] = 'S'
    except IndexError:
        print('Game over!')
        return info()


def info():
    print(f'Food eaten: {food_quantity}')
    [print(*i, sep='') for i in matrix]
    exit()


rows_columns = int(input())
matrix = []
snake_coord = []
food_quantity = 0
burrows_coord = [[], []]
[add_matrix() for i in range(rows_columns)]

while True:
    inp = input()

    matrix[snake_coord[0]][snake_coord[1]] = '.'

    move_snake(inp)

    if food_quantity >= 10:
        print('You won! You fed the snake.')
        info()