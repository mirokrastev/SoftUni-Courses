tasks_with_priority = []

while True:
    command = input()

    if command == 'End':
        break

    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    note = tokens[1]
    tasks_with_priority.append((priority, note))


def sort_fn(element):
    return element[0]


sorted_tasks = (sorted(tasks_with_priority, key=sort_fn))
print([task[1] for task in sorted_tasks])