d = list(map(int, input().split(', ')))
positive = []
negative = []
even = []
odd = []
[positive.append(i) if i >= 0 else negative.append(i) for i in d]
[even.append(i) if i % 2 == 0 else odd.append(i) for i in d]
print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')