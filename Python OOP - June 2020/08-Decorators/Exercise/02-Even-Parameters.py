def even_parameters(func):
    def wrapper(*args):
        try:
            if all(num % 2 == 0 for num in args):
                return func(*args)
            return f'Please use only even numbers!'
        except TypeError:
            return f'Please use only even numbers!'
    return wrapper