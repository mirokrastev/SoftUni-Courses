loading_bar = int(input())
def fn(a):
    counter = 0
    printer = ''
    d = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    for i in range(10, a + 10, 10):
        d.pop(counter)
        d.insert(counter, '%')
        counter += 1
    printer = ''.join(d)
    if a == 100:
        print('100% Complete!')
        print(f'[{printer}]')
    else:
        print(f'{a}% [{printer}]')
        print('Still loading...')
fn(loading_bar)