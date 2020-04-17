string = input()
s = []
[s.insert(0, i) for i in string]
print("".join(s))