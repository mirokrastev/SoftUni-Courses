def even_odd(*args):
    d = {'even': 0, 'odd': 1}

    command = args[-1]
    nums = args[:-1]

    return [i for i in nums if i % 2 == d[command]]