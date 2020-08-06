def read_next(*args):
    inx = 0

    while inx != len(args):
        for i in args[inx]:
            yield i
        inx += 1