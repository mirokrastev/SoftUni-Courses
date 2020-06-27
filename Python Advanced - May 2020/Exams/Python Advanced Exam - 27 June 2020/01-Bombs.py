from collections import deque


def calculate(bomb_effect, bomb_casing):
    sum_bombs = bomb_effect + bomb_casing

    if sum_bombs in char:
        dd[char[sum_bombs]] += 1
        bomb_casings.pop()
        bomb_effects.popleft()
    else:
        bomb_casings[-1] -= 5


def output():
    print(f'Bomb Effects: {", ".join(map(str, bomb_effects)) if bomb_effects else "empty"}')
    print(f'Bomb Casings: {", ".join(map(str, bomb_casings)) if bomb_casings else "empty"}')
    for k, v in sorted(dd.items()):
        print(f'{k}: {v}')
    exit()


bomb_effects = deque(int(i) for i in input().split(', '))
bomb_casings = deque(int(i) for i in input().split(', '))

char = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
dd = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}


while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]

    calculate(bomb_effect, bomb_casing)

    if dd['Datura Bombs'] >= 3 and dd['Cherry Bombs'] >= 3 and dd['Smoke Decoy Bombs'] >= 3:
        print(f'Bene! You have successfully filled the bomb pouch!')
        output()

print(f'You don\'t have enough materials to fill the bomb pouch.')
output()