strings = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["blue", "red"], "green": ["yellow", "blue"]}
made_colors = []

while strings:
    first = strings.pop()
    last = "" if not strings else strings.pop(0)

    if first + last in main_colors:
        made_colors.append(first + last)
        main_colors.remove(first + last)
    elif last + first in main_colors:
        made_colors.append(last + first)
        main_colors.remove(last + first)
    elif first + last in secondary_colors:
        made_colors.append(first + last)

    elif last + first in secondary_colors:
        made_colors.append(last + first)

    else:
        first = first[:-1]
        last = last[:-1]
        if first:
            strings.insert(len(strings) // 2, first)
        if last:
            strings.insert(len(strings) // 2, last)

for color in made_colors:
    if secondary_colors.get(color):
        if any(x not in made_colors for x in secondary_colors[color]):
            made_colors.remove(color)
            del secondary_colors[color]

print(made_colors)