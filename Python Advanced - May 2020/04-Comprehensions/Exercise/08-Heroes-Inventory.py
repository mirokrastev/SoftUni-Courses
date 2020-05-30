d = {}
[d.update({i: []}) for i in input().split(', ')]
d_two = {i: 0 for i in d}

while True:
    inp = input().split('-')
    if inp[0] == 'End':
        break
    name, item, price = inp
    if item not in d[name]:
        d[name].append(item)
        d_two[name] += int(price)

[print(f'{k} -> Items: {len(v)}, Cost: {d_two[k]}') for k,v in d.items()]