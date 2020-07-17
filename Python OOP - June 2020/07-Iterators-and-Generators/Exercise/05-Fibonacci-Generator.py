def fibonacci():
    previous_num = 0
    current_num = 1
    yield previous_num
    yield current_num

    while True:
        next_num = previous_num + current_num
        yield next_num
        previous_num, current_num = current_num, next_num