def func_executor(*args):
    result = [func(*arg) for func, arg in args]
    return result