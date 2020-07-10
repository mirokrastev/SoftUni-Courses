def logged(function):
    def wrapper(*args):
        result = function(*args)
        return f'you called {function.__name__}{args}\n' \
               f'it returned {result}'
    return wrapper