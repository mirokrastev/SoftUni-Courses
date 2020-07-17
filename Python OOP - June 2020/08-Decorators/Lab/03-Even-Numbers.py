def even_numbers(function):
    def wrapper(numbers):
        return [i for i in numbers if i % 2 == 0]

    return wrapper