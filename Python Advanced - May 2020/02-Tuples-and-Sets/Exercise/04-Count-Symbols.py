text = input()
d = {}


def count_symbols(symbol):
    if symbol not in d:
        d[symbol] = 0
    d[symbol] += 1


[count_symbols(i) for i in text]

for k,v in sorted(d.items()):
    print(f'{k}: {v} time/s')