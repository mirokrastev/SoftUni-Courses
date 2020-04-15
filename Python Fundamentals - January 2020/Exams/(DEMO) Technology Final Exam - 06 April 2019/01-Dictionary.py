d = {}
main_string = input().split(' | ')
for i in main_string:
    l = i.split(':')
    key = l[0]
    value = l[1].lstrip()
    if key not in d:
        d[key] = []
    d[key].append(value)

words_string = input().split(' | ')
final_string = input()
if final_string == 'List':
    sorted_d = dict(sorted(d.items(), key=lambda x: x[0]))
    print(*sorted_d.keys(), sep=' ')
elif final_string == 'End':
    var = {}
    for i in words_string:
        if i in d:
            hui = d[i]
            sorted_hui = sorted(hui, key=lambda x: (-len(x)))
            var.update({i: sorted_hui})
    for l in words_string:
        if l in var:
            print(f'{l}')
            for v in var[l]:
                print(f' -{v}')