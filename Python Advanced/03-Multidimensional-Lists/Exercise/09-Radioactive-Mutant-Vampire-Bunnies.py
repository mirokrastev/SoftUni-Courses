matrix = []

def add_matrix():
    global player_position

    arg = input()
    matrix.append([])
    for i in arg:
        matrix[-1].append(i)
        if i == 'P':
            player_position = [len(matrix) - 1, len(matrix[-1]) - 1]

def validate(command):
    matrix[player_position[0]][player_position[1]] = '.'
    if command == 'L':
        if player_position[1] - 1 >= 0:
            move_left()
        else:
            win_game()
    elif command == 'R':
        if player_position[1] + 1 < len(matrix[0]):
            move_right()
        else:
            win_game()
    elif command == 'U':
        if player_position[0] - 1 >= 0:
            move_up()
        else:
            win_game()
    elif command == 'D':
        if player_position[0] + 1 < len(matrix):
            move_down()
        else:
            win_game()

def move_left():
    global death

    player_position[1] -= 1
    if matrix[player_position[0]][player_position[1]] == '.':
        matrix[player_position[0]][player_position[1]] = 'P'
        validate_bunny()
    else:
        death = True
        validate_bunny()

def move_right():
    global death

    player_position[1] += 1
    if matrix[player_position[0]][player_position[1]] == '.':
        matrix[player_position[0]][player_position[1]] = 'P'
        validate_bunny()
    else:
        death = True
        validate_bunny()

def move_up():
    global death

    player_position[0] -= 1
    if matrix[player_position[0]][player_position[1]] == '.':
        matrix[player_position[0]][player_position[1]] = 'P'
        validate_bunny()
    else:
        death = True
        validate_bunny()

def move_down():
    global death

    player_position[0] += 1
    if matrix[player_position[0]][player_position[1]] == '.':
        matrix[player_position[0]][player_position[1]] = 'P'
        validate_bunny()
    else:
        death = True
        validate_bunny()

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
        bunny_locations = bunny_coordinates.pop(0)
        top = (bunny_locations[0] - 1, bunny_locations[1])
        left = (bunny_locations[0], bunny_locations[1] - 1)
        right = (bunny_locations[0], bunny_locations[1] + 1)
        bottom = (bunny_locations[0] + 1, bunny_locations[1])

        if top[0] >= 0:
            if matrix[top[0]][top[1]] == 'P':
                death = True
            matrix[top[0]][top[1]] = 'B'
        if left[1] >= 0:
            if matrix[left[0]][left[1]] == 'P':
                death = True
            matrix[left[0]][left[1]] = 'B'
        if right[1] < len(matrix[0]):
            if matrix[right[0]][right[1]] == 'P':
                death = True
            matrix[right[0]][right[1]] = 'B'
        if bottom[0] < len(matrix):
            if matrix[bottom[0]][bottom[1]] == 'P':
                death = True
            matrix[bottom[0]][bottom[1]] = 'B'
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

rows, columns = [int(i) for i in input().split()]
player_position = []
death = False
[add_matrix() for i in range(rows)]
commands = input()
[validate(i) for i in commands]