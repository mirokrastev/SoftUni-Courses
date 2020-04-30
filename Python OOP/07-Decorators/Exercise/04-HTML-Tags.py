def tags(tag):
    def fn(func):
        def wrapper(*args):
            result = func(*args)
            return f'<{tag}>{result}</{tag}>'

        return wrapper
    return fn