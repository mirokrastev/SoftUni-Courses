def multiply(times):
    def decorator(function):
        def wrapper(param):
            return times * function(param)
        return wrapper
    return decorator