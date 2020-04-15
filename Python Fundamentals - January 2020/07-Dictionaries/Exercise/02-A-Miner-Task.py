d = {}

while True:
    resource = input()
    if resource == 'stop':
        for key, value in d.items():
            print(f'{key} -> {value}')
        exit()
    quantity = int(input())
    if resource not in d:
        d[resource] = 0
    d[resource] += quantity