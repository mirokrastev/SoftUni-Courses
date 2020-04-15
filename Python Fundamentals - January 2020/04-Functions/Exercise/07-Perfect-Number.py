def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')
perfect_number(int(input()))