goal = 10000
zapochvane = 0

while zapochvane < goal:
    stupki = input()
    if stupki == 'Going home':
        stupki = int(input())
        zapochvane += stupki
        more_steps = goal - zapochvane
        if zapochvane < goal:
            print(f'{more_steps} more steps to reach goal.')
        break
    stupki_int = int(stupki)
    zapochvane += stupki_int

if zapochvane >= goal:
    print(f'Goal reached! Good job!')