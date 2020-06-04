def min_max_sum(inp):
    return f'The minimum number is {min(inp)}\n' \
           f'The maximum number is {max(inp)}\n' \
           f'The sum number is: {sum(inp)}'


inp = [int(i) for i in input().split()]
print(min_max_sum(inp))