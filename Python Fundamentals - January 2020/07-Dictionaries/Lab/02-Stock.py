inp = input().split()
product_search = input().split()
d = {}

for i in range(0, len(inp), 2):
    key = inp[i]
    value = inp[i+1]
    d[key] = value

for i in product_search:
    if i in d.keys():
        print(f'We have {d[i]} of {i} left')
    else:
        print(f'Sorry, we don\'t have {i}')