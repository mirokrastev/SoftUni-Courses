categories = input().split(', ')
bunker = {category: {} for category in categories}
n = int(input())

for _ in range(n):
    tokens = input().split(' - ')
    category = tokens[0]
    item = tokens[1]
    item_info = tokens[2].split(';')
    quantity, quality = int(item_info[0].split(':')[1]), int(item_info[1].split(':')[1])
    if category in bunker:
        bunker[category][item] = {'quantity': quantity, 'quality': quality}

count_items = sum([bunker[x][y]['quantity'] for x in bunker for y in bunker[x]])
sums_quality = sum([bunker[x][y]['quality'] for x in bunker for y in bunker[x]])
average_quality = sums_quality / len(categories)

print(f'Count of items: {count_items}')
print(f'Average quality: {average_quality:.2f}')

[print(f'{category} -> {", ".join(bunker[category].keys())}') for category in bunker]