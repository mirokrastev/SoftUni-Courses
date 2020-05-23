command = input()
initial_list = [int(i) for i in input().split()]

if command == 'Odd':
    print(sum([int(i) * len(initial_list) for i in initial_list if i % 2 == 1]))
else:
    print(sum([int(i) * len(initial_list) for i in initial_list if i % 2 == 0]))