def even_numbers(function):
    def wrapper(numbers):
        return [num for num in numbers if num % 2 == 0]
    return wrapper