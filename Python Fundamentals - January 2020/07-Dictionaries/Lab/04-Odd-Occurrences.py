words = input().split()
d = {}

for i in words:
    word_lower = i.lower()
    if word_lower not in d:
        d[word_lower] = 0
    d[word_lower] += 1

for key, value in d.items():
    if value % 2 == 1:
        print(key, end=' ')