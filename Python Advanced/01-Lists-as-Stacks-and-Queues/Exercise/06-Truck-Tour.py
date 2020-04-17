from collections import deque

import copy
num = int(input())
sequence = [[int(x)for x in input().split()] for i in range(num)]
counter = 0
so_far = 0
combo = False

while counter != len(sequence):
    copy_l = deque(copy.copy(sequence[counter:] + sequence[:counter]))
    while True:
        so_far += copy_l[0][0] - copy_l[0][1]
        if so_far < 0:
            so_far = 0
            ranger = 0
            break
        copy_l.popleft()
        if not copy_l:
            combo = True
            break
    if combo:
        print(counter)
        exit()
    counter += 1