string = input()
count_n = int(input())
def repeater(a, b):
    result = ''
    for i in range(b):
        result += a
    return result
print(repeater(string, count_n))