def multiply(times):
    def decorator(function):
        def wrapper(params):
            return times * function(params)
        return wrapper
    return decorator