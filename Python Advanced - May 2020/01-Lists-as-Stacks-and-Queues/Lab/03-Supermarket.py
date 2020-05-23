from collections import deque


def push_to_q(arg):
    q.append(arg)


def print_customers():
    while q:
        print(q.popleft())


def print_remaining():
    print(f'{len(q)} people remaining.')
    exit()


q = deque()

while True:
    arg = input()
    if arg == 'End':
        print_remaining()
    elif arg == 'Paid':
        print_customers()
    else:
        push_to_q(arg)