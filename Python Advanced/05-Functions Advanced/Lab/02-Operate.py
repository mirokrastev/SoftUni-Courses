def operate(*args):
    operator = args[0]
    args = args[1:]
    if operator == "+":
        result = 0
        for arg in args:
            result += arg
    elif operator == "-":
        result = 0
        for arg in args:
            result -= arg
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    elif operator == "/":
        result = 1
        for arg in args:
            result /= arg

    return result