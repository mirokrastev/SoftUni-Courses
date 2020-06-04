def numbers(num):
    global positive, negative

    if num >= 0:
        positive += num
    else:
        negative += num


arg = [int(i) for i in input().split()]
positive = 0
negative = 0
[numbers(i) for i in arg]

print(negative)
print(positive)

if positive > abs(negative):
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')