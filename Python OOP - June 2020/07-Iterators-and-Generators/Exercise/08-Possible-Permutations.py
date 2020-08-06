from itertools import permutations


def possible_permutations(ll):
    return (list(perm) for perm in permutations(ll))