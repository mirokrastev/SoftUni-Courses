lenght = int(input())
width = int(input())
height = int(input())

total_apartment_volume = height * width * lenght
total_boxes_volume = 0

is_free = True

boxes_count = input()

while not boxes_count == 'Done':
    boxes_count = int(boxes_count)
    total_boxes_volume += boxes_count

    if total_boxes_volume > total_apartment_volume:
        is_free = False
        break
    boxes_count = input()

if is_free:
    diff = total_apartment_volume - total_boxes_volume
    print(f'{diff} Cubic meters left.')
else:
    diff = total_boxes_volume - total_apartment_volume
    print(f'No more free space! You need {diff} Cubic meters more.')