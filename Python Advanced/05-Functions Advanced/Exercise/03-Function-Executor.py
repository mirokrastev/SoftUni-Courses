def func_executor(*args):
    result = []
    for i in range(len(args)):
        func = args[i][0]
        arg = args[i][1]
        result.append(func(*arg))
    return result