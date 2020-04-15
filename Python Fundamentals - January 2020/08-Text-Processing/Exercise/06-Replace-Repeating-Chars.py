text = input()
i = 0

while i < len(text) - 1:
    if text[i] == text[i+1]:
        text = text.replace(f'{text[i]}{text[i+1]}', text[i])
        i = 0
    else:
        i += 1
print(text)