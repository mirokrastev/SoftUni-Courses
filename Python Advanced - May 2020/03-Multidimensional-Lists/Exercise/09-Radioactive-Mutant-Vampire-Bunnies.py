def add_matrix():
    global player_position

    arg = input()
    matrix.append([])
    for i in arg:
        matrix[-1].append(i)
        if i == 'P':
            player_position = (len(matrix) - 1, len(matrix[-1]) - 1)


def validate(command):
    global player_position, death
    old_position = player_position
    matrix[player_position[0]][player_position[1]] = '.'

    change_coordinate = {
        'L': (player_position[0], player_position[1]-1),
        'R': (player_position[0], player_position[1]+1),
        'U': (player_position[0]-1, player_position[1]),
        'D': (player_position[0]+1, player_position[1])
    }

    player_position = change_coordinate[command]
    if player_position[0] <= -1 or player_position[1] <= -1:
        player_position = old_position
        win_game()

    try:
        if matrix[player_position[0]][player_position[1]] == '.':
            matrix[player_position[0]][player_position[1]] = 'P'
            validate_bunny()
        else:
            death = True
            validate_bunny()
    except IndexError:
        player_position = old_position
        win_game()


def validate_bunny():
    bunny_locations = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 'B':
                bunny_locations.append((row, column))
    move_bunny(bunny_locations)


def move_bunny(bunny_coordinates):
    global death

    while bunny_coordinates:
        bunny_location = bunny_coordinates.pop(0)
        bunny_coord = {
            0: (bunny_location[0]-1, bunny_location[1]),
            1: (bunny_location[0], bunny_location[1]-1),
            2: (bunny_location[0], bunny_location[1]+1),
            3: (bunny_location[0]+1, bunny_location[1])
        }

        for row, col in bunny_coord.values():
            try:
                if row >= 0 and col >= 0:
                    if matrix[row][col] == 'P':
                        death = True
                    matrix[row][col] = 'B'
            except IndexError: continue

    if death:
        end_game()


def end_game():
    [print(*i, sep='') for i in matrix]
    print(f'dead: {player_position[0]} {player_position[1]}')
    exit()


def win_game():
    validate_bunny()
    [print(*i, sep='') for i in matrix]
    print(f'won: {player_position[0]} {player_position[1]}')
    exit()


rows, columns = map(int, input().split())
player_position = ()
death = False
matrix = []
[add_matrix() for i in range(rows)]
commands = input()
[validate(i) for i in commands]