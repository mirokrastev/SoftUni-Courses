def fn(item):
    s[-1].append(item)
    if sum(s[-1]) > capacity_of_rack:
        s[-1].pop()
        s.append([item])


clothes_box = [int(i) for i in input().split()]
capacity_of_rack = int(input())
s = [[]]

while clothes_box:
    fn(clothes_box.pop())

print(len(s))