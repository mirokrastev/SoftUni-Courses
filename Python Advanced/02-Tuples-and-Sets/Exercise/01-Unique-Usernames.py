s = set()

def fn(a):
    s.add(a)

num = int(input())
[fn(input()) for i in range(num)]
[print(i) for i in s]