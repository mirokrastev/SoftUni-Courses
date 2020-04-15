n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num < 0:
        negative.append(num)
    if num >= 0:
        positive.append(num)
out = input()
if out == 'even':
    print(even)
elif out == 'odd':
    print(odd)
elif out == 'negative':
    print(negative)
elif out == 'positive':
    print(positive)