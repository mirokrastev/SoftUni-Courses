from _collections import deque
que = deque()

def supermarket(a):
    if a == 'End':
        print(f'{len(que)} people remaining.')
        exit()
    if a != 'Paid':
        que.append(a)
    if a == 'Paid':
        [print(i) for i in que]
        [que.popleft() for _ in range(len(que))]


while True:
    supermarket(input())