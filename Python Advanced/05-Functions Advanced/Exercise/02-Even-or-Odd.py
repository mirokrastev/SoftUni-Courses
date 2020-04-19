def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == 'even':
        return [i for i in numbers if i % 2 == 0]
    else:
        return [i for i in numbers if i % 2 == 1]