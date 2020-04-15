fire_cell = input().replace(' ', '').replace('=', '#').split('#')
water = int(input())
effort = 0
total_fire = 0
counter = 1
cells = []
garbage_collector = ''
for i in fire_cell:
    if counter % 2 == 0:
        i = int(i)
        fire_cell.insert(counter-1, [garbage_collector, i])
        fire_cell.pop(counter)
    else:
        garbage_collector = i
    counter += 1
counter = 0
for _ in fire_cell:
    if _ != type(list):
        fire_cell.pop(counter)
    counter += 1
for l in range(len(fire_cell)):
    if fire_cell[l][0] == 'Low' and 0 < fire_cell[l][1] < 51 and water >= fire_cell[l][1]:
        water -= fire_cell[l][1]
        effort += (25 * fire_cell[l][1]) / 100
        total_fire += fire_cell[l][1]
        cells.append(str(fire_cell[l][1]))
    elif fire_cell[l][0] == 'Medium' and 51 <= fire_cell[l][1] < 81 and water >= fire_cell[l][1]:
        water -= fire_cell[l][1]
        effort += (25 * fire_cell[l][1]) / 100
        total_fire += fire_cell[l][1]
        cells.append(str(fire_cell[l][1]))
    elif fire_cell[l][0] == 'High' and 81 <= fire_cell[l][1] < 126 and water >= fire_cell[l][1]:
        water -= fire_cell[l][1]
        effort += (25 * fire_cell[l][1]) / 100
        total_fire += fire_cell[l][1]
        cells.append(str(fire_cell[l][1]))
counter = 0
print('Cells:')
for l in cells:
    print(f' - {l}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')