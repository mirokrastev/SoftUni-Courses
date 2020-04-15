n = int(input())
positive = []
negative = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
    if num <= -1:
        negative.append(num)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}')