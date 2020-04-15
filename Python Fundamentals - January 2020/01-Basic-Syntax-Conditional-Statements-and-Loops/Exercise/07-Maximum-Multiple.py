divisor = int(input())
bound = int(input())
num = divisor
bool = True

while num <= bound:
    num += divisor
print(num - divisor)