inp = int(input())
chairs_list = 0
is_full = False

for i in range(1, inp + 1):
    chairs_inp = input().split()
    if len(chairs_inp[0]) > int(chairs_inp[1]):
        chairs_list += len(chairs_inp[0]) - int(chairs_inp[1])
    elif len(chairs_inp[0]) == int(chairs_inp[1]):
        continue
    elif len(chairs_inp[0]) < int(chairs_inp[1]):
        print(f'{int(chairs_inp[1]) - len(chairs_inp[0])} more chairs needed in room {i}')
        is_full = True
if not is_full:
    print(f'Game On, {chairs_list} free chairs left')