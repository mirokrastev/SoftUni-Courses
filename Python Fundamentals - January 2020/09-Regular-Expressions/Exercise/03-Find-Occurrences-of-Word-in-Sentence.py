from re import findall
sentence = input().lower()
search_word = input().lower()
pattern = f'\\b{search_word}\\b'
reg = len(findall(pattern, sentence))
print(reg)