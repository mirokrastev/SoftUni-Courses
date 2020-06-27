from collections import deque


def match_genders(male, female):
    global matched
    to_return = False

    if male <= 0:
        males.pop()
        to_return = True

    if female <= 0:
        females.popleft()
        to_return = True

    if to_return: return

    if male % 25 == 0:
        males.pop()
        males.pop() if males else None
        to_return = True

    if female % 25 == 0:
        females.popleft()
        females.popleft() if females else None
        to_return = True

    if to_return: return

    if male != female:
        females.popleft()
        males[-1] -= 2
        return

    males.pop()
    females.popleft()
    matched += 1


males = [int(i) for i in input().split()]
females = deque(int(i) for i in input().split())
matched = 0

while males and females:
    male = males[-1]
    female = females[0]
    match_genders(male, female)

print(f'Matches: {matched}')
print(f'Males left: {", ".join(map(str, reversed(males)))if males else "none"}')
print(f'Females left: {", ".join(map(str, females))if females else "none"}')