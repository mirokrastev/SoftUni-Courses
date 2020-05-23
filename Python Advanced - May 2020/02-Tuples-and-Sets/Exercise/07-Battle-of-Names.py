num = int(input())
odd = set()
even = set()

for i in range(1, num+1):
    name = input()
    ascii_value = sum([ord(i) for i in name]) // i
    even.add(ascii_value) if ascii_value % 2 == 0 else odd.add(ascii_value)

max_odd = sum(odd)
max_even = sum(even)

if max_odd == max_even:
    print(*odd.union(even), sep=', ')
elif max_odd > max_even:
    print(*odd.difference(even), sep=', ')
elif max_odd < max_even:
    print(*odd.symmetric_difference(even), sep=', ')