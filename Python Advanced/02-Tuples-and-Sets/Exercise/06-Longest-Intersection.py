d = {}

def fn(a):
    first = a[0].split(',')
    second = a[1].split(',')
    set_one = set(i for i in range(int(first[0]), int(first[1])+1))
    set_two = set(i for i in range(int(second[0]), int(second[1])+1))
    intersection = set_one.intersection(set_two)
    if len(intersection) not in d:
        d[len(intersection)] = list(intersection)

num = int(input())
[fn(input().split('-')) for i in range(num)]
print(f'Longest intersection is {d[max(d.keys())]} with length {max(d.keys())}')