from collections import deque


def find_best_station(arg):
    copy_of_list = deque(stations[arg:] + stations[:arg])
    so_far = 0
    while copy_of_list:
        amount, distance = copy_of_list.popleft()
        so_far += amount - distance
        if so_far < 0:
            break
    return so_far


num = int(input())
stations = [[int(i) for i in input().split()] for i in range(num)]

for i in range(len(stations)):
    fn = find_best_station(i)
    if fn >= 0:
        print(i)
        exit()