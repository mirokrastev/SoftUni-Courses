d = {}


def fn(a):
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for k,v in d.items():
        print(f'{k} - {v} times')


l = [float(i) for i in input().split()]
fn(l)