string = input().split()
string = list(map(int, string))
num = int(input())

for i in range(num):
    string.remove(min(string))
print(string)