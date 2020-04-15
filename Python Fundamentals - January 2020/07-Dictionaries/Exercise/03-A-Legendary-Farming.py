d = {
    'shards': 0,
    'motes': 0,
    'fragments': 0,
}
junk = {}
printer = False

while True:
    inp = input().lower().split()

    for i in range(0, len(inp), 2):
        key = inp[i + 1]
        value = int(inp[i])
        if key not in d and key not in junk:
            junk[key] = 0
            junk[key] += value
        elif key not in d and key in junk:
            junk[key] += value
        elif key in d:
            d[key] += value
        if any([d['shards'] >= 250, d['motes'] >= 250, d['fragments'] >= 250]):
            if d['fragments'] >= 250:
                print('Valanyr obtained!')
                d['fragments'] -= 250
                printer = True
                break
            elif d['motes'] >= 250:
                print('Dragonwrath obtained!')
                d['motes'] -= 250
                printer = True
                break
            elif d['shards']:
                print('Shadowmourne obtained!')
                d['shards'] -= 250
                printer = True
                break
    if printer:
        sorted_dd = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        for i in range(len(sorted_dd)):
            print(f'{sorted_dd[i][0]}: {sorted_dd[i][1]}')
        sorted_junk = sorted(junk.items(), key=lambda x: x[0])
        for i in range(len(sorted_junk)):
            print(f'{sorted_junk[i][0]}: {sorted_junk[i][1]}')
        exit()