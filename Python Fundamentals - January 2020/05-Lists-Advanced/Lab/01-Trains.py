wagons_n = int(input())
train = [0] * wagons_n

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split()
    instruction = tokens[0]

    if instruction == 'add':
        count = int(tokens[1])
        train[-1] += count
    elif instruction == 'insert':
        count = int(tokens[2])
        index = int(tokens[1])
        train[index] += count
    elif instruction == 'leave':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] -= count
print(train)