import re
d = []
pattern = r' ([a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+@[a-zA-Z]+-*[a-zA-Z]+([\.?][a-zA-Z]+-?[a-zA-Z]+)+)'
inp = input()

matches = [x[0] for x in re.findall(pattern, inp)]
print('\n'.join(matches))