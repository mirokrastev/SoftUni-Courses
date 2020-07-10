def type_check(var_type):
    def fn(function):
        def wrapper(*args):
            if not isinstance(*args, var_type):
                return 'Bad Type'

            return function(*args)
        return wrapper
    return fn