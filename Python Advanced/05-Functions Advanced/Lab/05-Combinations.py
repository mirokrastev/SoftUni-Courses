def permutations(index, values):
    if index == len(values):
        print("".join(values))
        return

    for i in range(index, len(values)):
        values[index], values[i] = values[i], values[index]
        permutations(index + 1, values)
        values[index], values[i] = values[i], values[index]

permutations(0, list(input()))