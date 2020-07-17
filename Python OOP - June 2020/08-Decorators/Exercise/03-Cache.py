def cache(func):
    def wrapper(arg):
        result = func(arg)
        wrapper.log[arg] = result

        return result
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)