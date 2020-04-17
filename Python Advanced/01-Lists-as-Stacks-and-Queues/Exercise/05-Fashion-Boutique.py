from collections import deque


def fn(clothes_boxes, capacity_rack):
    total_boxes = [[]]
    so_far = 0
    while clothes_boxes:
        popped = clothes_boxes.pop()
        if popped + so_far > capacity_rack:
            clothes_boxes.append(popped)
            total_boxes.append([])
            so_far = 0
        else:
            total_boxes[-1].append(popped)
            so_far += popped
    return len(total_boxes)

clothes_boxes = deque(int(i) for i in input().split())
capacity_rack = int(input())
print(fn(clothes_boxes, capacity_rack))