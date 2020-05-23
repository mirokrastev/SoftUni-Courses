num = int(input())
s = set()

for i in range(num):
    name = input()
    s.add(name)
    
[print(i) for i in s]