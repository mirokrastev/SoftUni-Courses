def get_primes(ll):
    for num in ll:
        if num <= 1: continue
        for divider in range(2, num):
            if num % divider == 0:
                break
        else:
            yield num