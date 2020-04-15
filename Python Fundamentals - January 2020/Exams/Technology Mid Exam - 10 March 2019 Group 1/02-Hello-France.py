type_price = input().replace('->', '|').split('|')
budget = float(input())
counter = 1
garbage_collector = ''
profiter = []
profit = 0
for i in type_price:
    if counter % 2 == 0:
        i = float(i)
        type_price.insert(counter-1, [garbage_collector, i])
        type_price.pop(counter)
    else:
        garbage_collector = i
    counter += 1
counter = 0
for _ in type_price:
    if _ != type(list):
        type_price.pop(counter)
    counter += 1
for l in range(len(type_price)):
    if type_price[l][0] == 'Clothes' and type_price[l][1] < 50.01 and budget >= type_price[l][1]:
        budget -= type_price[l][1]
        d = (40 * type_price[l][1]) / 100
        profiter.append(f'{type_price[l][1] + d:.2f}')
        profit += d
    elif type_price[l][0] == 'Shoes' and type_price[l][1] < 35.01 and budget >= type_price[l][1]:
        budget -= type_price[l][1]
        d = (40 * type_price[l][1]) / 100
        profiter.append(f'{type_price[l][1] + d:.2f}')
        profit += d
    elif type_price[l][0] == 'Accessories' and type_price[l][1] < 20.51 and budget >= type_price[l][1]:
        budget -= type_price[l][1]
        d = (40 * type_price[l][1]) / 100
        profiter.append(f'{type_price[l][1] + d:.2f}')
        profit += d
for _ in profiter:
    budget += float(_)
print(*profiter)
print(f'Profit: {profit:.2f}')
if budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')