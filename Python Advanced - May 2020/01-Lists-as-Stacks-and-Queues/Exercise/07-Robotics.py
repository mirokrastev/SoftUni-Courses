from collections import deque


def print_robots(robot_index, material):
    l = initial_time
    print(f'{robots[robot_index][0]} - {material} [{l[0]:02d}:{l[1]:02d}:{l[2]:02d}]')


def increment_time():
    initial_time[2] += 1
    if initial_time[2] >= 60:
        initial_time[1] += 1
        initial_time[2] = 0
        if initial_time[1] >= 60:
            initial_time[0] += 1
            initial_time[1] = 0
            if initial_time[0] >= 24:
                initial_time[0] = 0

def fn(robot_index, material):
    print_robots(robot_index, material)
    robots[robot_index][2] = robots[robot_index][1]


robots = []

for i in input().split(';'):
    robot, time = i.split('-')
    robots.append([robot, int(time), 0])

initial_time = deque(int(i) for i in input().split(':'))
materials = deque()

while True:
    material = input()
    if material == 'End':
        break
    materials.append(material)

while materials:
    enter = True
    increment_time()
    material = materials.popleft()

    for robot_index in range(len(robots)):
        if robots[robot_index][2] >= 1:
            robots[robot_index][2] -= 1
        if robots[robot_index][2] == 0:
            if enter:
                fn(robot_index, material)
                enter = False

    if enter:
        materials.append(material)