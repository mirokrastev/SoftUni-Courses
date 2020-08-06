def cache(func):
    def wrapper(arg):
        result = func(arg)
        wrapper.log[arg] = result

        return result
    wrapper.log = {}
    return wrapper