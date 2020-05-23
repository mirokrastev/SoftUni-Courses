initial_list = [int(i) for i in input().split()]
negative = list(filter(lambda x: x < 0, initial_list))
positive = list(filter(lambda x: x > 0, initial_list))
print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')