matrix = []

def add_matrix():
    global coals, start_position
    arg = input().split()
    matrix.append([])
    for i in arg:
        matrix[-1].append(i)
        if i == 'c':
            coals += 1
        elif i == 's':
            start_position = (len(matrix) - 1, len(matrix[-1]) - 1)

square_matrix = int(input())
commands = input().split()

coals = 0
start_position = tuple()

[add_matrix() for i in range(square_matrix)]

def end_game():
    global start_position
    print(f'Game over! {start_position}')
    exit()

def mine_coal():
    global coals, start_position
    coals -= 1
    matrix[start_position[0]][start_position[1]] = 's'

    if coals == 0:
        print(f"You collected all coals! {start_position}")
        exit()

def normal_move():
    global start_position
    matrix[start_position[0]][start_position[1]] = 's'

def fn(move):
    global start_position
    while move:
        current_command = move.pop(0)
        if current_command == 'up':
            if start_position[0] - 1 >= 0:
                matrix[start_position[0]][start_position[1]] = '*'
                start_position = (start_position[0] - 1, start_position[1])
                if matrix[start_position[0]][start_position[1]] == 'e':
                    end_game()
                elif matrix[start_position[0]][start_position[1]] == 'c':
                    mine_coal()
                else:
                    normal_move()
        elif current_command == 'down':
            if start_position[0] + 1 < len(matrix):
                matrix[start_position[0]][start_position[1]] = '*'
                start_position = (start_position[0] + 1, start_position[1])
                if matrix[start_position[0]][start_position[1]] == 'e':
                    end_game()
                elif matrix[start_position[0]][start_position[1]] == 'c':
                    mine_coal()
                else:
                    normal_move()
        elif current_command == 'left':
            if start_position[1] - 1 >= 0:
                matrix[start_position[0]][start_position[1]] = '*'
                start_position = (start_position[0], start_position[1] - 1)
                if matrix[start_position[0]][start_position[1]] == 'e':
                    end_game()
                elif matrix[start_position[0]][start_position[1]] == 'c':
                    mine_coal()
                else:
                    normal_move()
        elif current_command == 'right':
            if start_position[1] + 1 < len(matrix):
                matrix[start_position[0]][start_position[1]] = '*'
                start_position = (start_position[0], start_position[1] + 1)
                if matrix[start_position[0]][start_position[1]] == 'e':
                    end_game()
                elif matrix[start_position[0]][start_position[1]] == 'c':
                    mine_coal()
                else:
                    normal_move()

fn(commands)

print(f'{coals} coals left. {start_position}')