def get_repeating_DNA(DNA):
    all_combs = []
    repeating_combs = []

    for i in range(len(DNA) - 9):
        sequence = DNA[i:i+10]
        if sequence not in all_combs:
            all_combs.append(sequence)
        else:
            repeating_combs.append(sequence) if sequence not in repeating_combs else None

    return repeating_combs