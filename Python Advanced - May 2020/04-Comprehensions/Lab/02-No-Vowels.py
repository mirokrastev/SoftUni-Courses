l = [i for i in input() if i.lower() not in {'a', 'o', 'u', 'e', 'i'}]
print("".join(l))