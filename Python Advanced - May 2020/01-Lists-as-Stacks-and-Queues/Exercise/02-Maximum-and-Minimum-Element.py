s = []
num = int(input())


def push_el(arg):
    s.append(arg)


def delete_el(arg):
    if s:
        s.pop()


def print_max_el(arg):
    if s:
        print(max(s))


def print_min_el(arg):
    if s:
        print(min(s))


mapping = {
    1: push_el,
    2: delete_el,
    3: print_max_el,
    4: print_min_el,
}

for i in range(num):
    args = input().split()
    direction = int(args[0])
    arg = int(args[1]) if len(args) == 2 else None
    mapping[direction](arg)

print(", ".join(map(str, s[::-1])))