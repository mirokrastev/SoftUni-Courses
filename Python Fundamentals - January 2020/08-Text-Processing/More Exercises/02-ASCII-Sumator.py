a = input()
b = input()
string = input()
var = 0

for i in string:
    if ord(i) in range(ord(a) + 1, ord(b)):
        var += ord(i)
print(var)