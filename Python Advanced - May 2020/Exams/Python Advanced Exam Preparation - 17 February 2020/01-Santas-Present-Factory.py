from collections import deque


def mix(material, magic_level):
    total_level = material * magic_level
    to_return = False

    if material == 0:
        materials.pop()
        to_return = True

    if magic_level == 0:
        magic_levels.popleft()
        to_return = True
        
    if to_return: return

    if total_level <= -1:
        total_level = material + magic_level
        materials.pop()
        magic_levels.popleft()
        materials.append(total_level)
        return

    if total_level in presents_map:
        presents[presents_map[total_level]] += 1
        materials.pop()
        magic_levels.popleft()
        return

    magic_levels.popleft()
    materials[-1] += 15


materials = deque(int(i) for i in input().split())
magic_levels = deque(int(i) for i in input().split())
presents_map = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
presents = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

while materials and magic_levels:
    material = materials[-1]
    magic_level = magic_levels[0]
    mix(material, magic_level)

if (presents['Doll'] and presents['Wooden train']) or (presents['Teddy bear'] and presents['Bicycle']):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

print(f'Materials left: {", ".join(map(str, reversed(materials)))}') if materials else None
print(f'Magic left: {", ".join(map(str, magic_levels))}') if magic_levels else None

for k, v in sorted(presents.items()):
    if v >= 1:
        print(f'{k}: {v}')