def reverse_text(string):
    index = len(string) - 1

    for i in range(index, -1, -1):
        yield string[i]