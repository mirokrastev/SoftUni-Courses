interval_beginning = int(input())
interval_end = int(input())
magic_number = int(input())
combination_counter = 0

for a in range(interval_beginning, interval_end + 1):
    for b in range(interval_beginning, interval_end + 1):
        combination_counter += 1
        if a + b == magic_number:
            print(f'Combination N:{combination_counter} ({a} + {b} = {magic_number})')
            exit()
print(f'{combination_counter} combinations - neither equals {magic_number}')