one = [i for i in input().split(', ')]
two = [i for i in input().split(', ')]
d = {i:two.pop(0) for i in one}
[print(f'{k} -> {v}') for k,v in d.items()]