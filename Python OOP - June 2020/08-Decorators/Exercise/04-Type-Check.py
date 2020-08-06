def type_check(type):
    def fn(function):
        def wrapper(*args):
            if not isinstance(*args, type):
                return 'Bad Type'
            return function(*args)
        return wrapper
    return fn