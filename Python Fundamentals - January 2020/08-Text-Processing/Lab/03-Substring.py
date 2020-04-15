filter_word = input()
inp_raw = input()

while filter_word in inp_raw:
    inp_raw = inp_raw.replace(filter_word, '')
print(inp_raw)